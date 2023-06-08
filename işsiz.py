import insan

class Issiz(insan.Insan): #issiz sınıfı insan sınıfından kalıtım
    def __init__(self,tc,isim,soyisim,yas,cinsiyet,uyruk,geçmiş_tecrübe): #yapıcı metot
        super().__init__(tc,isim,soyisim,yas,cinsiyet,uyruk) #kalıtım aldığımız sınıfın yapıcı metotu
        self.__gecmis_tecrube= geçmiş_tecrübe   #gecmis tecrube private değişkeni
        self.__statu=str() #statu private değişkeni
        self.statu_bul()

    def get_gecmis_tecrube(self): #gecmis tecrube almak için get metodu
        return self.__gecmis_tecrube
    def set_gecmis_tecrube(self,gecmis_tecrube): #gecmis tecrube yapmak için set metodu
        self.__gecmis_tecrube=gecmis_tecrube
    def statu_bul(self): #statu bulmak için metot
        mavi_yaka=self.__gecmis_tecrube[0]*0.2 #mavi yaka etkisi
        beyaz_yaka=self.__gecmis_tecrube[1]*0.35 #beyaz yaka etkisi
        yonetici=self.__gecmis_tecrube[2]*0.45 #yonetici etkisi
        if mavi_yaka>beyaz_yaka and mavi_yaka>yonetici: #mavi yaka en büyükse
            self.__statu="mavi yaka" #statu mavi yaka
        elif beyaz_yaka>mavi_yaka and beyaz_yaka>yonetici: #beyaz yaka en büyükse
            self.__statu="beyaz yaka" #statu beyaz yaka
        elif yonetici>mavi_yaka and yonetici>beyaz_yaka: #yonetici en büyükse
            self.__statu="yonetici" #statu yonetici
        else: #eşitse
            self.__statu="yönetici" #statu yönetici
    def __str__(self): #str metodu ile issiz sınıfı için bilgileri yazdırma işlemi
        return f"isim: {self.get_isim()} soyisim: {self.get_soyisim()} statu: {self.__statu}"
