import çalışan

class BeyazYaka(çalışan.Calisan):  # beyaz yaka sınıfı calisan sınıfından kalıtım
    def __init__(self, tc, isim, soyisim, yas, cinsiyet, uyruk, sektor, tecrube, maas, prim):  # yapıcı metot
        self.__prim = prim  # tesvik primi private değişkeni
        super().__init__(tc, isim, soyisim, yas, cinsiyet, uyruk, sektor, tecrube,
                         maas)  # kalıtım aldığımız sınıfın yapıcı metotu

    def get_prim(self):  # tesvik primi almak için get metodu
        return self.__prim

    def set_prim(self, tesvik_primi):  # tesvik primi yapmak için set metodu
        self.__prim = tesvik_primi

    def zam_hakki(self):  # zam hakki metodu
        zam = 0  # zam değişkeni
        if self.get_tecrube() < 24:  # tecrube 24 den küçükse
            zam = self.__prim  # zam tesvik primi
        elif self.get_tecrube() >= 24 and self.get_tecrube() < 48 and self.get_maas() < 15000:  # tecrube 24 ile 48 arasında ve maas 15000 den küçükse
            zam = ((
                               self.__maas % self.get_tecrube()) / 100) * 5 + self.__prim  # zam (maas*tecrube/100)*5 + tesvik primi
        elif self.get_tecrube() >= 48 and self.get_maas() < 25000:  # tecrube 48 den büyük ve maas 25000 den büyükse
            zam = ((
                               self.get_maas() % self.get_tecrube()) / 100) * 4 + self.__prim  # zam (maas*tecrube/100)*4 + tesvik primi
        else:  # eşitse
            zam = 0  # zam 0
        return zam  # yeni maas maas+zam

    def __str__(self):  # str metodu ile calisan sınıfı için bilgileri yazdırma işlemi
        self.set_yeni_maas(self.get_maas() + self.zam_hakki())  # yeni maas maas+zam
        return f"isim: {self.get_isim()} soyisim: {self.get_soyisim()} tecrube: {self.get_tecrube()} yeni maas: {self.get_yeni_maas()}"
