class Insan:

    def __init__(self,tc,isim,soyisim,yas,cinsiyet,uyruk):        #yapıcı metot
        self.__tc=tc                                              #tc private değişkeni
        self.__isim=isim                                          #isim private değişkeni
        self.__soyisim=soyisim                                    #soyisim private değişkeni
        self.__yas=yas                                            #yas private değişkeni
        self.__cinsiyet=cinsiyet                                  #cinsiyet private değişkeni
        self.__uyruk=uyruk                                        #uyruk private değişkeni

    def get_tc(self):                                             #tc almak için get metodu
        return self.__tc
    def set_tc(self,tc):                                          #tc yapmak için set metodu
        self.__tc=tc

    def get_isim(self):                                           #isim almak için get metodu
        return self.__isim
    def set_isim(self,isim):                                      #isim yapmak için set metodu
        self.__isim=isim

    def get_soyisim(self):                                        #soyisim almak için get metodu
        return self.__soyisim
    def set_soyisim(self,soyisim):                                #soyisim yapmak için set metodu
        self.__soyisim=soyisim

    def get_yas(self):                                            #yas almak için get metodu
        return self.__yas
    def set_yas(self,yas):                                        #yas yapmak için set metodu
        self.__yas=yas

    def get_cinsiyet(self):                                       #cinsiyet almak için get metodu
        return self.__cinsiyet
    def set_cinsiyet(self,cinsiyet):                              #cinsiyet yapmak için set metodu
        self.__cinsiyet=cinsiyet

    def get_uyruk(self):                                          #uyruk almak için get metodu
        return self.__uyruk
    def set_uyruk(self,uyruk):                                    #uyruk yapmak için set metodu
        self.__uyruk=uyruk

    def __str__(self):                                           #str metodu ile insan sınıfı için bilgileri yazdırma işlemi
        return f"tc: {self.__tc} isim:{self.__isim} soyisim:{self.__soyisim} yas:{self.__yas} cinsiyet:{self.__cinsiyet} uyruk:{self.__uyruk}"
