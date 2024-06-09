import cv2
import numpy as np
import utils


########################################################################
webCamFeed = True
pathImage = "2.jpeg"
cap = cv2.VideoCapture(1)
cap.set(10,160)
heightImg = 700
widthImg  = 700
questions=5
choices=5
ans= [1,2,0,2,4]
########################################################################


count=0

while True:

    if webCamFeed:success, img = cap.read()
    else:img = cv2.imread(pathImage)
    img = cv2.resize(img, (widthImg, heightImg)) # Resmi Yeniden Boyutlandır
    imgFinal = img.copy()
    imgBlank = np.zeros((heightImg,widthImg, 3), np.uint8) # GEREKİRSE HATA AYIKLAMANIN TEST EDİLMESİ İÇİN BOŞ BİR GÖRÜNTÜ OLUŞTURUR
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # RESMİ GRİ TONLARA ÇEVİRİR
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1) # GAUSSİAN (PÜRÜZSÜZLEŞTİRME) BULANIKLIĞI TEKNİĞİ EKLİYORUZ
    imgCanny = cv2.Canny(imgBlur,10,70) # CANNY (KENAR BELİRLEME) TEKNİĞİ UYGULUYORUZ

    try:
        ## Tüm Sınırları BUL
        imgContours = img.copy() # (GÖRÜNTÜ ALMAK İÇİN KOPYALIYORUZ)
        imgBigContour = img.copy() # (GÖRÜNTÜ ALMAK İÇİN KOPYALIYORUZ)
        contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # KENAR PİKSELLERİNİ KONTURLARA(SINIRLARA) BİRLEŞTİRME 
        cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10) # BULUNAN TÜM KONTURLERİ(SINIR) ÇİZİYOR
        rectCon = utils.rectContour(contours) # DİKDÖRTGEN KONTUR(SINIR)LAR İÇİN FİLTRE UYGULUYOR
        biggestPoints= utils.getCornerPoints(rectCon[0]) # EN BÜYÜK DİKDÖRTGENİN DIŞ SINIRLARINI ALIYOR
        gradePoints = utils.getCornerPoints(rectCon[1]) # İKİNCİ BÜYÜK DİKDÖRTGENİN DIŞ SINIRLARINI ALIYOR

        

        if biggestPoints.size != 0 and gradePoints.size != 0:

            # EN BÜYÜK DİKDÖRTGENİN KÖŞELERİNİ İŞLEME
            biggestPoints=utils.reorder(biggestPoints) # KÖŞELERİ İŞLİYOR
            cv2.drawContours(imgBigContour, biggestPoints, -1, (0, 255, 0), 20) # EN BÜYÜK SINIRI ÇİZİYOR
            pts1 = np.float32(biggestPoints) # NOKTALARI İŞLEME HAZIRLIYOR
            pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # NOKTALARIN YÜKSEKLİK VE GENİŞLİKLERİNİ BELİRLEYEREK İŞLİYOR
            matrix = cv2.getPerspectiveTransform(pts1, pts2) # NOKTALARI BİR MATRİSE ÇEVİRİYOR
            imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg)) # PERSPEKTİF ÇARPITMASI UYGULUYOR

            # İKİNCİ BÜYÜK DİKDÖRTGENİN KÖŞELERİNİ İŞLEME
            cv2.drawContours(imgBigContour, gradePoints, -1, (255, 0, 0), 20) # EN BÜYÜK SINIRI ÇİZİYOR
            gradePoints = utils.reorder(gradePoints) # KÖŞELERİ İŞLİYOR
            ptsG1 = np.float32(gradePoints)  # NOKTALARI İŞLEME HAZIRLIYOR
            ptsG2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])  # NOKTALARI İŞLEME HAZIRLIYOR
            matrixG = cv2.getPerspectiveTransform(ptsG1, ptsG2)# NOKTALARI BİR MATRİSE ÇEVİRİYOR
            imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150)) # PERSPEKTİF ÇARPITMASI UYGULUYOR

            # EŞİK UYGULAMASI YAPMAK
            imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY) # GRİ TONLARINA ÇEVİR
            imgThresh = cv2.threshold(imgWarpGray, 170, 255,cv2.THRESH_BINARY_INV )[1] # TERS VE EŞİK UYGULAMASI YAPILIYOR

            boxes = utils.splitBoxes(imgThresh) # TEKLİ KUTU YAPIYOR
            #cv2.imshow("isaret testi ", boxes[3])
            countR=0
            countC=0
            myPixelVal = np.zeros((questions,choices)) # HER KUTUNUN SIFIR OLMAYAN DEĞERLERİNİ ALIYOR
            for image in boxes:
                #cv2.imshow(str(countR)+str(countC),image)
                totalPixels = cv2.countNonZero(image)
                myPixelVal[countR][countC]= totalPixels
                countC += 1
                if (countC==choices):countC=0;countR +=1

            # KULLANICI CEVAPLARINI BULUP LİSTEYE ÇEVİRME
            myIndex=[]
            for x in range (0,questions):
                arr = myPixelVal[x]
                myIndexVal = np.where(arr == np.amax(arr))
                myIndex.append(myIndexVal[0][0])
            #print("USER ANSWERS",myIndex)

            # DOĞRU CEVAPLARI BULMAK İÇİN DEĞERLERİ KARŞILAŞTIRMA
            grading=[]
            for x in range(0,questions):
                if ans[x] == myIndex[x]:
                    grading.append(1)
                else:grading.append(0)
            #print("GRADING",grading)
            score = (sum(grading)/questions)*100 # FINAL NOTU
            #print("SCORE",score)

            # CEVAPLARI GÖRÜNTÜLEME
            utils.showAnswers(imgWarpColored,myIndex,grading,ans) # CEVAPLARI İŞARETLİYOR
            utils.drawGrid(imgWarpColored) # IZGARA ÇİZİYOR
            imgRawDrawings = np.zeros_like(imgWarpColored) # RESİM BOYUTUNA GÖRE YENİ BOŞ BİR GÖRÜNTÜ OLUŞTURUYOR
            utils.showAnswers(imgRawDrawings, myIndex, grading, ans) # YENİ RESMİ ÇİZİYOR
            invMatrix = cv2.getPerspectiveTransform(pts2, pts1) # TERS MATRİSE DÖNÜŞTÜR
            imgInvWarp = cv2.warpPerspective(imgRawDrawings, invMatrix, (widthImg, heightImg)) # PİKSELLERİ TAŞIYARAK TERSE ÇEVİRİYOR

            # SONUCU GÖRÜNTÜLEME
            imgRawGrade = np.zeros_like(imgGradeDisplay,np.uint8) # SONUÇ ALANI BÜYÜKLÜĞÜNDE BOŞ BİR ALAN OLUŞTUR
            cv2.putText(imgRawGrade,str(int(score))+"%",(100,100)
                        ,cv2.FONT_HERSHEY_TRIPLEX,4,(255,0,0),10) # FONT VE RENGİ BELİRLEYİP YENİ RESME SONUCU EKLİYOR
            invMatrixG = cv2.getPerspectiveTransform(ptsG2, ptsG1) # TERS MATRİSE DÖNÜŞTÜRÜYOR
            imgInvGradeDisplay = cv2.warpPerspective(imgRawGrade, invMatrixG, (widthImg, heightImg)) # PİKSELLERİ TAŞIYARAK TERSE ÇEVİRİYOR

            # TÜM CEVAPLARI VE FİNAL SONUCUNU GÖRÜNTÜLEME
            imgFinal = cv2.addWeighted(imgFinal, 1, imgInvWarp, 1,0)
            imgFinal = cv2.addWeighted(imgFinal, 1, imgInvGradeDisplay, 1,0)

            # TÜM İŞLEMLERİ GÖRÜNTÜLEME
            imageArray = ([img,imgGray,imgCanny,imgContours],
                          [imgBigContour,imgThresh,imgWarpColored,imgFinal])
            cv2.imshow("Final Sonucu", imgFinal)
    except:
        imageArray = ([img,imgGray,imgCanny,imgContours],
                      [imgBlank, imgBlank, imgBlank, imgBlank])

    # GÖRÜNTÜ BAŞLIKLARINI YAZMA
    lables = [["Orjinal","GriTonlar","SiyahBeyazKenarlar","SINIRcizgileri"],
              ["DikdortgenKoseleri","SiyahBeyazCerceve","RenkliCerceve","Final"]]

    stackedImage = utils.stackImages(imageArray,0.55,lables)
    cv2.imshow("Sonuc",stackedImage)

    
    # 'S TUŞUNA BASINCA KAYDETME'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(r'C:\Users\serca\OneDrive\Masaüstü\Recognition-master\Scanned\myImage\Final'+str(count)+".jpeg",imgFinal)
        cv2.rectangle(stackedImage, ((int(stackedImage.shape[1] / 2) - 230), int(stackedImage.shape[0] / 2) + 50),
                      (1100, 350), (255, 255, 0), cv2.FILLED)
        cv2.putText(stackedImage, "Kaydedildi!", (int(stackedImage.shape[1] / 2) - 200, int(stackedImage.shape[0] / 2)),
                    cv2.FONT_HERSHEY_TRIPLEX, 3, (0, 0, 255), 5, cv2.LINE_AA)
        cv2.imshow('Sonuc', stackedImage)
        cv2.waitKey(300)
        count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break