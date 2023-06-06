import random   # random kütüphanesini ekliyoruz
import time        # time kütüphanesini ekliyoruz
bk = 0  # bilgisyar kazanımını 0 a eşitliyoruz
kk = 0  # kullanıcı kazanımını 0 a eşitliyoruz
x = 0    # tur sayısını x değişkeni ile ifade ediyoruz ve 0 a eşitliyoruz
s = ["taş", "kağıt", "makas"]   # seçeneklerin kısaltması olan s ile liste oluşturuyoruz
while True:
    bs = s[random.randint(0, 2)]    # bilgisayara rastgele bir sayı seçtiriyoruz ve bu sayı ile s listesinden eleman çağırıyoruz
    ks = input("Taş Kağıt Makas'tan birini seçiniz, çıkmak için q'ya basınız:").lower()    # kullanıcıdan seçim yapmasını istiyoruz
    if ks == "q":      # çıkış durumunu kontrol ediyoruz
        print(x, "tur oynandı,", kk, "tur kazanıldı,", bk, "tur kaybedildi", x-(bk+kk), "tur berabere")
        time.sleep(2.5)
        # time kütüphanesi sayesinde uygulamayı kapatmadan öne 3 saniye bekletiyoruz eğer bekletmezseniz sonucu göremeden uygulama kapanır
        break
    elif ks not in s:   # kullanıcın girdisini kontrol ediyoruz hatalı giriş varsa tekrar girdiriyoruz
        print("Hatalı giriş yaptınız!")
        continue
    x += 1  # tur sayısını arttırıyoruz
    if ks == bs:                 # kullanıcın seçimi ve bilgisayarın seçimi karşılaştırılıyor ve buna göre bir sonuç veriliyor
        print("BERABERE")
    elif ks == "taş":
        if bs == "kağıt":
            print("KAYBETTİN")
            bk += 1
        else:
            print("KAZANDIN")
            kk += 1
    elif ks == "kağıt":
        if bs == "makas":
            print("KAYBETTİN")
            bk += 1
        else:
            print("KAZANDIN")
            kk += 1
    elif ks == "makas":
        if bs == "taş":
            print("KAYBETTİN")
            bk += 1
        else:
            print("KAZANDIN")
            kk += 1
    print("Kullanıcının seçimi:", ks.upper())
    print("Bilgisayarın seçimi:", bs.upper())
