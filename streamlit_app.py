import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_folium import st_folium
from streamlit_player import st_player,_SUPPORTED_EVENTS
from streamlit_option_menu import option_menu
import folium
import datetime
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title=("Görüntü İşleme ve Blokzinciri Tabanlı Bir İyileştirilmiş Optik Okuma ve Sınav Değerlendirme Sistemi"),page_icon=":camera:",layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_cznnfmoz.json")
lottie_coding2 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_3vkWd6xCBt.json")
lottie_coding3 = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_WdTEui.json")
lottie_coding4 = load_lottieurl("https://assets2.lottiefiles.com/temp/lf20_JNpJ0D.json")
lottie_coding5 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_18QlHa.json")
lottie_coding6 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_BfBOY9JOfS.json")
lottie_coding7 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_gk6xltea.json")

tabs=["Ana Sayfa","Yüz Tanıma","Optik Okuma","Hakkımda"]

page = st.sidebar.radio("Menü",tabs)

if page == "Ana Sayfa":
    #st_player("https://soundcloud.com/heba-aboeit/dedublu-man-belki-akustik",
     #height=10, volume=st.slider("Ses Düzeyi", 0.0, 1.0, 0.1, .01), playing= st.checkbox("Sesi Ayarla ve Müziği Çal", False),
             #)
    st.markdown("<h1 style='text-align:center;'>Görüntü İşleme ve Blokzinciri Tabanlı Bir İyileştirilmiş Optik Okuma ve Sınav Değerlendirme Sistemi</h1",unsafe_allow_html=True)
    st.write("---")
    st_lottie(lottie_coding4, height=150, key="coding")
    st.header("Projenin Önemi")
    st.text(
                """Proje önerisiyle özellikle ulusal çapta yapılan merkezi sınavların ve bu sınavlara giren adayların güvenliğini 
sağlamak amaçlanmıştır. Sınavlara girecek olan adaylar sınav salonuna girmeden önce yüz tanıması gerçekleştirilerek ;
güvenlik açısından problem sağlayacak kaçak girişlerin önüne geçilmesini sağlayacaktır. Aynı şekilde adaylar sınavın 
bitiminde optik cevap formlarını kameraya taratarak hem cevaplarını sonradan değişme tehlikesine karşı saklayacak , 
hem de yapılan uygulama taradığı optik formu değerlendirip puanlayacak. Ayrıca aday sınav çıkışında doğru yanlış 
sayısını net olarak görebilecek. Tüm bu kaydedilen fotoğraflar yenilikçi blokzinciri teknolojisi yardımıyla 
değişmeksizin saklanmış olacak. Tasarlanacak olan uygulama özgün bir uygulama olduğundan teknolojik dışa 
bağımlılığımızı azaltacak ve ülkemizin özellikle yenilikçi teknolojilerde global ölçüde var olmasını sağlayacak. 
Süreç içerisinde hazırlanacak olan sistem yapılacak güncellemelerle geliştirilebilir.

                """
            )
    st_lottie(lottie_coding5, height=100, key="coding5")
    st.header("Amaç ve Hedefler")
    st.text(
            """Proje önerisinin amaçlarının başında güvenlik gelmektedir. Görüntü işleme tekniklerinin kusursuz olarak
işlemesi sayesinde yüz tanıma işlemi yapılarak sınava kaçak aday girmesini engellemeyi hedefliyoruz.Böylece merkezi 
sınavlara görevli olarak tayin edilen yedek gözetmen, gözetmen, salon başkanı ve bina sınav sorumlusunun inisiyatifine 
kalmadan bilgisayar destekli olarak aday doğrulaması yapılacaktır. Özellikle içinde bulunduğumuz pandemi şartları 
düşünüldüğünde sınava maske ile katılacak olan adaylar yüzlerinin belli bir kısmını gizleyebilmektedir. Geliştirilecek
olan yazılımın maskeli şekilde sınava gelen adayın gözlerini dahi görmesi, yüz tanımanın gerçekleştirilmesi yeterli 
olacaktır. Ayrıyeten bu yüz taramaları sistem tarafından kaydedilip olası bir itiraz durumunda sınavı yapan kurum 
tarafından delil olarak kullanılabilecektir. Yüz taramalarını kaydetmek mümkün olduğu gibi bir diğer önemli nokta da 
aday cevaplarının gizlilik ve güvenliğidir. Bu bakımdan adayların sınavlarının bitiminde optik formu ile birlikte 
kamerada anlık görüntüsü alınacak , yine bu optik form da blokzincir teknolojisi yardımıyla değiştirilmeksizin 
kaydedilecek.Sistemin hedeflediği noktalardan bir tanesi de değerlendirmedir. Aday optik formunu sınav çıkışında 
kameraya okuttuğu için arkaplanda çalışmakta olan yazılımımız optik formu değerlendirecek, adayı daha sınav salonundan
çıkmadan kaç doğru kaç yanlışı olduğunu beyan edecektir. Sınav binalarına sistemimizle entegre bir kiosk cihazı 
konularak adaylara basılı bir sonuç belgesi bile verilebilecektir. Proje farklı işletim sistemlerinde denenerek 
en optimal olanına karar verilecek, ve sistem kararlı hale getirilecektir.
            """
            )
    st_lottie(lottie_coding5, height=100, key="coding6")
    st.header("Proje Yöntemi")
    st.text(
            """Hazırlanacak sistem ile aday cevap kağıdının ve yaptığı işaretlemelerin görüntüsü sınavı bitirmesini
takiben blokzinciri teknolojisi ile kayıt altına alınacak ve adayın yaptığı işaretlemeler ile adaya ait olan kitapçık
numarasının cevap anahtarı karşılaştırılıp ; adaya sınav sonunda kaç yanlış ve kaç doğrusunun olduğunu bildirir bir 
çıktı verilebilecektir. Python programlama dili ve OpenCV açık kaynaklı kütüphanesi kullanılarak oluşturulacak yazılım 
sayesinde adayın yüz tanıması ve optik okuması yani görüntü işlemesi gerçekleştirilip , blokzincirine kaydedilecek;
böylece hem aday anında cevaplarını öğrenecek , hem de cevapların kendisine ait olduğunu herhangi bir değişim 
yapılamayacağı garanti altına alınacaktır. İlk 3 aylık döneminde, literatür taraması yapılacak ve yüz tanıma ve optik
okuma alanında yapılan çalışmalar detaylıca  incelenecektir. 3. Ay ile 5. Aylarda Makine Öğrenimi teknikleri ve 
yüz tanıma modelleri incelenerek denenecek. En verimli olan model kullanılmak üzere seçilecektir. 5. Ay ile 7. Aylarda 
kullanılacak olan web arayüzü için incelemeler yapılacak , web uygulama iskeletleri (frameworkleri) arasından en kararlı 
olan seçilecek, diğer yandan ise algoritmalar oluşturulup arayüze gömecek hale getirilecektir. 7. ve 9. Aylar arasında 
ise arayüz , modeller ve algoritmalar ile ilgili tüm denemeler yapılıp  veri tabanını genişletmek adına farklı 
görsellerin tarama çalışması yapılacaktır. Son 4 ayda ise tüm bu çalışmalar ışığında yapılan çalışmalar değerlendirilip 
sonuçlar analiz edilecek ; Bilimsel/Akademik yayınlar yazılmaya başlanacaktır.
            """
            )
    st_lottie(lottie_coding6, height=300, key="coding7")

if page == "Yüz Tanıma":
    st.markdown("<h1 style='text-align:center;'>Yüz Tanıma Uygulaması</h1",unsafe_allow_html=True)
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Nasıl Çalışır?")
            st.write("##")
            st.text(
                """
                Yüz tanıma uygulaması arka planda çalışan Python 
                programlama dili ile yazılmış algoritma ile aşağıdaki 
                sırayla işlemler gerçekleştirilir :

                - Algoritmaya yüzleri içeren fotoğraflar tanımlanır.

                - Yazılım yüz tanıma modellerini kullanarak yüzü yorumlar.

                - Yüzü tanıyorsa ismini , tanımıyor ise 'Bilinmiyor' yazar.

                - 'S' tuşu ile kayıt yapılır, 'Q' tuşu ile çıkış yapılır.

                """
            )

            button = st.button("<<<<<< Yüz Tanımayı Başlat >>>>>>")

            if button == True:
                with st.spinner("Yüz Tanıma Uygulaması Başlatılıyor, Lütfen Bekleyiniz..."):
                    from YüzTanımaWebcam import *
       
        with right_column:
            st_lottie(lottie_coding, height=400, key="coding")
    




elif page == "Optik Okuma":
    st.markdown("<h1 style='text-align:center;'>Optik Okuma Uygulaması</h1",unsafe_allow_html=True)
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Nasıl Çalışır?")
            st.write("##")
            st.text(
                """
               Optik Okuma uygulaması arka planda çalışan Python 
                programlama dili ile yazılmış algoritma ile aşağıdaki 
                sırayla işlemler gerçekleştirilir :

                - İşaretlenmiş standart optik formlar kameraya taratılır.

                - Yazılım OpenCV kütüphanesinin farklı tekniklerini
                  kullanarak kağıtta belli noktaları işaretler.

                - Kağıtta alttaki not bölümüne sonuç yazılacaktır.

                - 'S' tuşu ile kayıt yapılır, 'Q' tuşu ile çıkış yapılır.

                """
            )
            button = st.button("<<<<<<< Optik Okumayı Başlat >>>>>>")

            if button == True:
                with st.spinner("Optik Okuma Uygulaması Başlatılıyor, Lütfen Bekleyiniz..."):
                    from Optik import *
        
        with right_column:
            st_lottie(lottie_coding2, height=400, key="coding")


elif page == "Hakkımda":
    st.markdown("<h1 style='text-align:center;'>Hakkımda</h1",unsafe_allow_html=True)
    st_lottie(lottie_coding3, height=100, key="coding")
    st.write("---")
    st.markdown("Görüntü İşleme ve Blokzinciri Tabanlı Bir İyileştirilmiş Optik Okuma ve Sınav Değerlendirme Sistemi")
    st.write("v.0.0.1")
    left_column, right_column = st.columns(2)
    with right_column:
        st.subheader("""[Bitlis Eren Üniversitesi](https://www.beu.edu.tr/)\n [Fen Edebiyat Fakültesi](https://www.beu.edu.tr/akademik/fakulteler/fen-edebiyat-fakultesi) - - - [Matematik Bölümü](https://www.beu.edu.tr/akademik/fakulteler/fen-edebiyat-fakultesi/bolumler/matematik-bolumu)""") 
        m = folium.Map(location=[38.47821657569942, 42.16371597536874], zoom_start=16)
        folium.Marker(
            [38.47821657569942, 42.16371597536874],
            popup="Bitlis Eren Üniversitesi",
            tooltip="Bitlis Eren Üniversitesi"
        ).add_to(m)
        st_data = st_folium(m, width=500, height=250)
    with left_column:
        st.subheader("""**Danışman = [Doç. Dr. Selçuk TOPAL](https://www.beu.edu.tr/personel/s.topal@beu.edu.tr)""")
        st.subheader("""**Araştırmacı = [Sercan SARP](https://www.linkedin.com/in/sercan-sarp/)""")
        st_lottie(lottie_coding7, height=150, width=300, key="coding7")
        