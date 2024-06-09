import cv2
import dlib

detector=dlib.get_frontal_face_detector()
model=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap=cv2.VideoCapture(1) 

while True: 
    _,frame=cap.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=detector(gri)
    for face in faces:
        points=model(gri,face)
        print(points)

        for i in range(68):
            x,y=(points.part(i).x , points.part(i).y)
            cv2.circle(frame,(x,y),3,(255,0,0),-1)
    
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()