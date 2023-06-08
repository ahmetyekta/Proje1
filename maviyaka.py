import çalışan
class MaviYaka(çalışan.Calisan): #mavi yaka sınıfı calisan sınıfından kalıtım
    def __init__(self,tc,isim,soyisim,yas,cinsiyet,uyruk,sektor,tecrube,maas,yipranma_payi): #yapıcı metot
        super().__init__(tc,isim,soyisim,yas,cinsiyet,uyruk,sektor,tecrube,maas) #kalıtım aldığımız sınıfın yapıcı metotu
        self.__yipranma_payi=yipranma_payi #yipranma payi private değişkeni

    def get_yipranma_payi(self): #yipranma payi almak için get metodu
        return self.__yipranma_payi
    def set_yipranma_payi(self,yipranma_payi): #yipranma payi yapmak için set metodu
        self.__yipranma_payi=yipranma_payi

    def zam_hakki(self): #zam hakki metodu
        zam=0 #zam değişkeni
        if self.get_tecrube()<24: #tecrube 24 den küçükse
            zam=self.__yipranma_payi*10 #zam yipranma payi*10
        elif self.get_tecrube()>=24 and self.get_tecrube()<48 and self.get_maas()<15000: #tecrube 24 ile 48 arasında ve maas 15000 den küçükse
            zam=(self.get_maas()*self.__tecrube/100)/2 + (self.__yipranma_payi*10) #zam (maas*tecrube/100)/2 + (yipranma payi*10)
        elif self.get_tecrube()>=48 and self.get_maas()>25000: #tecrube 48 den büyük ve maas 25000 den büyükse
            zam=(self.get_maas()*self.get_tecrube()/100)/3 + (self.__yipranma_payi*10) #zam (maas*tecrube/100)/3 + (yipranma payi*10)
        else: #eş
            zam=0 #zam 0
        return zam #yeni maas maas+zam
