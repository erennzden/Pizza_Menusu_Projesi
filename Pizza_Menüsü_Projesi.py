import csv
from datetime import datetime
import time

open("Menu.txt", "w")
file = open("Menu.txt", "w", encoding="utf-8")
file.write("Lütfen Bir Pizza Tabanı Seçiniz:\n")
file.close()
file = open("Menu.txt", "a", encoding="utf-8")
file.write("1: Klasik\n")
file.write("2: Margarita\n")
file.write("3: Türk Pizza\n")
file.write("4: Dominos Pizza\n")
file.write("\n\nSeçeceğiniz Sos:\n")
file.write("11: Zeytin\n")
file.write("12: Mantarlar\n")
file.write("13: Keçi Peyniri\n")
file.write("14: Et\n")
file.write("15: Soğan\n")
file.write("16: Mısır\n")
file.write("\n\n\nTeşekkür Ederiz\n")
file.close()


class Pizza():

    def __init__(self, tür, fiyat, malzeme):
        self.tür = tür
        self.fiyat = fiyat
        self.malzeme = malzeme

    def bilgilerigöster(self):
        print("""
        Pizza Özellikleri

        Tür : {}
        Fiyat (tl) : {}
        Malzeme : {}

        """.format(self.tür, self.fiyat, self.malzeme))


pizza = Pizza("klasik pizza", 100, ["peynir", "zeytin", "et", "mantar"])
pizza.bilgilerigöster()

pizza1 = Pizza("türk pizza", 95, ["peynir", "zeytin", "et"])
pizza1.bilgilerigöster()

pizza2 = Pizza("dominos pizza", 120, ["peynir", "zeytin", "et", "mantar", "mısır", "soğan"])
pizza2.bilgilerigöster()

pizza3 = Pizza(" margarita pizza", 80, ["keçi peynir", "zeytin", "biber"])
pizza3.bilgilerigöster()

print("------------------------------------------------------------------------------------------")



class Sos():

    def __init__(self, malzeme, fiyat):
        self.malzeme = malzeme
        self.fiyat = fiyat

    def bilgilerigöster(self):
        print("""
        Sos Özellikleri

        Malzeme : {}
        Fiyat (tl) : {}


        """.format(self.malzeme, self.fiyat))


sos = Sos("zeytin", 6)
sos.bilgilerigöster()

sos1 = Sos("mantarlar", 8)
sos1.bilgilerigöster()

sos2 = Sos("keçi peyniri", 7)
sos2.bilgilerigöster()

sos3 = Sos("et", 12)
sos3.bilgilerigöster()

sos4 = Sos("soğan", 5)
sos4.bilgilerigöster()

sos5 = Sos("mısır", 10)
sos5.bilgilerigöster()

sipariş = input("Pizza Seçiniz:")

if sipariş == "klasik pizza":
    time.sleep(1)
    print("Sos Seçiniz:")
    cevap = input("Cevabınız:")

    if cevap == "zeytin":
        print("Borcunuz toplam 106 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)
            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "mantarlar":
        print("Borcunuz toplam 108 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "keçi peyniri":
        print("Borcunuz toplam 107 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "et":
        print("Borcunuz toplam 112 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "soğan":
        print("Borcunuz toplam 105 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "mısır":
        print("Borcunuz toplam 110 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

elif sipariş == "türk pizza":
    time.sleep(1)
    print("Sos Seçiniz:")
    cevap = input("Cevabınız:")
    if cevap == "zeytin":
        print("Borcunuz toplam 101 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "mantarlar":
        print("Borcunuz toplam 103 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "keçi peyniri":
        print("Borcunuz toplam 102 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "et":
        print("Borcunuz toplam 107 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "soğan":
        print("Borcunuz toplam 100 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "mısır":
        print("Borcunuz toplam 105 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

elif sipariş == "margarita pizza":
    time.sleep(1)
    print("Sos Seçiniz:")
    cevap = input("Cevabınız:")
    if cevap == "zeytin":
        print("Borcunuz toplam 86 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "mantarlar":
        print("Borcunuz toplam 88 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "keçi peyniri":
        print("Borcunuz toplam 87 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "et":
        print("Borcunuz toplam 92 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "soğan":
        print("Borcunuz toplam 85 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "mısır":
        print("Borcunuz toplam 90 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

elif sipariş == "dominos pizza":
    time.sleep(1)
    print("Sos Seçiniz:")
    cevap = input("Cevabınız:")
    if cevap == "zeytin":
        print("Borcunuz toplam 126 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "mantarlar":
        print("Borcunuz toplam 128 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "keçi peyniri":
        print("Borcunuz toplam 127 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "et":
        print("Borcunuz toplam 132 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "soğan":
        print("Borcunuz toplam 125 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

    if cevap == "mısır":
        print("Borcunuz toplam 130 tl'dir. Ödeme İşlemine Devam Etmek İstiyor Musunuz?(evet/hayır)")
        cevap = input("Cevabınız:")
        if cevap == "evet":
            time.sleep(1)

            isim = input("İsminiz:")
            tc_kimlik = int(input("TC Kimlik Numaranız:"))
            kredi_kart_no = int(input("Kredi Kartı Numaranız:"))

            sys_parola = "123abc"

            giriş_hakkı = 3

            while True:
                parola = input("Parolanız:")
                if (sys_parola == parola):
                    print("Parola onaylandı. Ödeme Başarıyla Gerçekleşti...")
                    break
                elif (sys_parola != parola):
                    print("Parolanız Hatalı. Tekrar Deneyiniz...")
                    giriş_hakkı -= 1

                if (giriş_hakkı == 0):
                    print("Ödeme İptal Edildi...")
                    break
            time.sleep(1)
        if cevap == "hayır":
            print("Siparişiniz İptal Ediliyor...")

else:
    print("Geçersiz Sipariş... Programı Yeniden Çalıştırıp Pizza Menüsü'ne Bakarak Sipariş Veriniz...")


şu_an = datetime.now()
print(datetime.ctime(şu_an))

f = open("Orders_Database.csv","a", encoding="utf-8")
tup1 = ("isim:",isim)
tup2 = ("TC Kimlik Numarası:",tc_kimlik)
tup3 = ("Kredi Kartı Numarası:",kredi_kart_no)
tup4 = ("Kredi Kartı Şifresi:","123abc")
tup5 = ("Tarih:",şu_an)
writer = csv.writer(f)
writer.writerow(tup1)
writer.writerow(tup2)
writer.writerow(tup3)
writer.writerow(tup4)
writer.writerow(tup5)
f.close()


print("Yine Bekleriz...")
