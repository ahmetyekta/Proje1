import insan, işsiz, çalışan, maviyaka, beyazyaka
import pandas as pd
# pandas kütüphanesi
def main():
    insan1 = insan.Insan(17596148564, "Ahmet", "Erdemli", 23, "Bay", "Türkiye")    # insan sınıfı için 1. nesne
    insan2 = insan.Insan(68745965412, "Sıla", "Ozden", 45, "Bayan", "Türkiye")     # insan sınıfı için 2. nesne
    print(insan1)                                                                  # insan1 için __str__ metodu
    print(insan2)                                                                  # insan2 için __str__ metodu
    print("-" * 100)  # 100 tane - karakteri
    issiz1 = işsiz.Issiz(47215635489, "Berzan", "Erdal", 22, "Bay", "Türkiye", [2, 5, 5])   # issiz sınıfı için 1. nesne
    issiz2 = işsiz.Issiz(95178954523, "Darari", "Taş", 27, "Bay", "Türkiye", [10, 12, 0])   # issiz sınıfı için 2. nesne
    issiz3 = işsiz.Issiz(68541236597, "İlayda", "Tör", 39, "Bayan", "Türkiye", [5, 10, 2])  # issiz sınıfı için 3. nesne
    print(issiz1)  # issiz1 için __str__ metodu
    print(issiz2)  # issiz2 için __str__ metodu
    print(issiz3)  # issiz3 için __str__ metodu
    print("-" * 100)  # 100 tane - karakteri
    calisan1 = çalışan.Calisan(48595135785, "Mehmet", "Erdemli", 40, "Bay", "Türkiye", "yazılım", 20,
                               10000)  # calisan sınıfı için 1. nesne
    calisan2 = çalışan.Calisan(75315985236, "Ali", "Rustemli", 45, "Bay", "Türkiye", "yazılım", 25,
                               12000)  # calisan sınıfı için 2. nesne
    calisan3 = çalışan.Calisan(15935785468, "Merve", "Genç", 50, "Bayan", "Türkiye", "yazılım", 30,
                               14000)  # calisan sınıfı için 3. nesne
    print(calisan1)   # calisan1 için __str__ metodu
    print(calisan2)   # calisan2 için __str__ metodu
    print(calisan3)   # calisan3 için __str__ metodu
    print("-" * 100)  # 100 tane - karakteri
    maviyaka1 = maviyaka.MaviYaka(25896374108, "Yakup", "Yürekli", 55, "Bay", "Türkiye", "yazılım", 35, 26000,
                                    0.2)  # maviyaka sınıfı için 1. nesne
    maviyaka2 = maviyaka.MaviYaka(14785236902, "Veysel", "Bilici", 60, "Bay", "Türkiye", "yazılım", 40, 30000,
                                    0.25) # maviyaka sınıfı için 2. nesne
    maviyaka3 = maviyaka.MaviYaka(36902587415, "Gizem", "Can", 65, "Bayan", "Türkiye", "yazılım", 45, 35000,
                                    0.5)  # maviyaka sınıfı için 3. nesne
    print(maviyaka1)  # maviyaka1 nesnesi için __str__ metodu
    print(maviyaka2)  # maviyaka2 nesnesi için __str__ metodu
    print(maviyaka3)  # maviyaka3 nesnesi için __str__ metodu
    print("-" * 100)  # 100 tane - karakteri
    beyazyaka1 = beyazyaka.BeyazYaka(12365498705, "Abdulkadir", "Geylani", 70, "Bay", "Türkiye", "yazılım", 50, 24000,
                                       250)  # beyazyaka sınıfı için 1. nesne
    beyazyaka2 = beyazyaka.BeyazYaka(78945632158, "Enes", "Güllütaze", 75, "Bay", "Türkiye", "yazılım", 55, 26000,
                                       500)  # beyazyaka sınıfı için 2. nesne
    beyazyaka3 = beyazyaka.BeyazYaka(52631456879, "Yaren", "Kara", 80, "Bayan", "Türkiye", "yazılım", 60, 35000,
                                       2500)  # beyazyaka sınıfı için 3. nesne
    print(beyazyaka1)  # beyazyaka1 nesnesi için __str__ metodu
    print(beyazyaka2)  # beyazyaka2 nesnesi için __str__ metodu
    print(beyazyaka3)  # beyazyaka3 nesnesi için __str__ metodu
    print("-" * 100)   # 100 tane - karakteri
    neseneler = ["Çalışan", "Çalışan", "Çalışan", "MaviYaka", "MaviYaka", "MaviYaka", "BeyazYaka", "BeyazYaka",
                 "BeyazYaka"]
    tcler = [calisan1.get_tc(), calisan2.get_tc(), calisan3.get_tc(), maviyaka1.get_tc(),
             maviyaka2.get_tc(), maviyaka3.get_tc(), beyazyaka1.get_tc(), beyazyaka2.get_tc(),
             beyazyaka3.get_tc()]
    isimler = [calisan1.get_isim(), calisan2.get_isim(), calisan3.get_isim(), maviyaka1.get_isim(), maviyaka2.get_isim(),
             maviyaka3.get_isim(), beyazyaka1.get_isim(), beyazyaka2.get_isim(), beyazyaka3.get_isim()]
    soyisimler = [calisan1.get_soyisim(), calisan2.get_soyisim(), calisan3.get_soyisim(), maviyaka1.get_soyisim(),
                maviyaka2.get_soyisim(), maviyaka3.get_soyisim(), beyazyaka1.get_soyisim(), beyazyaka2.get_soyisim(),
                beyazyaka3.get_soyisim()]
    yaslar = [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), maviyaka1.get_yas(), maviyaka2.get_yas(),
              maviyaka3.get_yas(), beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()]
    cinsiyetler = [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), maviyaka1.get_cinsiyet(),
                   maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(), beyazyaka1.get_cinsiyet(),
                   beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()]
    uyruklar = [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), maviyaka1.get_uyruk(),
                maviyaka2.get_uyruk(), maviyaka3.get_uyruk(), beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(),
                beyazyaka3.get_uyruk()]
    sektorler = [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), maviyaka1.get_sektor(),
                 maviyaka2.get_sektor(), maviyaka3.get_sektor(), beyazyaka1.get_sektor(), beyazyaka2.get_sektor(),
                 beyazyaka3.get_sektor()]
    tecrubeler = [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), maviyaka1.get_tecrube(),
                  maviyaka2.get_tecrube(), maviyaka3.get_tecrube(), beyazyaka1.get_tecrube(), beyazyaka2.get_tecrube(),
                  beyazyaka3.get_tecrube()]
    maaslar = [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), maviyaka1.get_maas(),
               maviyaka2.get_maas(), maviyaka3.get_maas(), beyazyaka1.get_maas(), beyazyaka2.get_maas(),
               beyazyaka3.get_maas()]
    yıpranmalar = [0, 0, 0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(), maviyaka3.get_yipranma_payi(),
                   0, 0, 0]
    primler = [0, 0, 0, 0, 0, 0, beyazyaka1.get_prim(), beyazyaka2.get_prim(), beyazyaka3.get_prim()]
    yenimaaslar = [calisan1.get_yeni_maas(), calisan2.get_yeni_maas(), calisan3.get_yeni_maas(),
                   maviyaka1.get_yeni_maas(), maviyaka2.get_yeni_maas(), maviyaka3.get_yeni_maas(),
                   beyazyaka1.get_yeni_maas(), beyazyaka2.get_yeni_maas(), beyazyaka3.get_yeni_maas()]

    tablo = {"nesneler": neseneler, "tcler": tcler, "isimler": isimler, "soyisimler": soyisimler, "yaslar": yaslar,
             "cinsiyetler": cinsiyetler, "uyruklar": uyruklar, "sektorler": sektorler, "tecrubeler": tecrubeler,
             "maaşlar": maaslar, "yıpranmalar": yıpranmalar, "primler": primler, "yenimaaşlar": yenimaaslar}
    df = pd.DataFrame(tablo)  # tabloyu dataframe e çevirme
    print(df)  # dataframe i yazdırma
    print("-" * 100)  # 100 tane - karakteri
    """Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş ortalamalarını her grup için hesaplayınız ve yazdırınız."""
    print("Çalışanlar için tecrübe ortalaması: ", df[df["nesneler"] == "Çalışan"]["tecrubeler"].mean())
    print("Çalışanlar için yeni maaş ortalaması: ", df[df["nesneler"] == "Çalışan"]["yenimaaşlar"].mean())
    print("Mavi yaka için tecrübe ortalaması: ", df[df["nesneler"] == "MaviYaka"]["tecrubeler"].mean())
    print("Mavi yaka için yeni maaş ortalaması: ", df[df["nesneler"] == "MaviYaka"]["yenimaaşlar"].mean())
    print("Beyaz yaka için tecrübe ortalaması: ", df[df["nesneler"] == "BeyazYaka"]["tecrubeler"].mean())
    print("Beyaz yaka için yeni maaş ortalaması: ", df[df["nesneler"] == "BeyazYaka"]["yenimaaşlar"].mean())
    print("-" * 100)  # 100 tane - karakteri
    # Maaşı 15000TL üzerinde olanların toplam sayısını bulunuz.
    print("Maaşı 15000TL üzerinde olanların toplam sayısı: ", len(df[df["maaşlar"] > 15000]))
    print("-" * 100)  # 100 tane - karakteri
    # Yeni maaşlara göre DataFrame’i küçükten büyüğe sıralayınız ve yazdırınız.
    print(df.sort_values(by="yenimaaşlar"))
    print("-" * 100)  # 100 tane - karakteri
    # Yeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanları, tc ve yeni_maaş sütunlarını seçerek gösteriniz ve yazdırınız.
    print(df[df["yenimaaşlar"] > 10000][2:5][["tcler", "yenimaaşlar"]])
    print("-" * 100)  # 100 tane - karakteri
    # Var olan DataFrame’den isim, soyisim, sektör ve yeni maaşı içeren yeni bir DataFrame elde ediniz ve yazdırınız.
    print(df[["isimler", "soyisimler", "sektorler", "yenimaaşlar"]])
    print("-" * 100)  # 100 tane - karakteri


if __name__ == "__main__":
    main()