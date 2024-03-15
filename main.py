import hesap
import islem

def ana_ekran():
    counter = 3

    while counter> 0:
        username = input("Kullanızı adınıcı giriniz :")
        password = input("Şifrenizi giriniz :")

        hesap_adi = islem.giris_yap(username, password)

        #User interface (UI)

        if hesap_adi:
            while True:
                # Kullanıcıdan işlem türü tercihi yapıyor
                prompt = "İşlem Türü Seçiniz:\n1 Para Çekme\n2 Para Yatırma\n3 Bakiye Sorgulama\n4 Hesap Bilgileri\n5 Çıkış\n>> "
                tercih = input(prompt)

                if tercih == "1":
                    miktar = int(input("Para çekme miktarı: "))
                    islem.para_cek(hesap_adi, miktar)
                elif tercih == "2":
                    yatirim = int(input("Para yatırma miktarı: "))
                    islem.para_yatir(hesap_adi, yatirim)
                elif tercih == "3":
                    islem.bakiye_sorgu(hesap_adi)
                elif tercih == "4":
                    islem.hesap_bilgi(hesap_adi)
                elif tercih == "5":
                    print("Güle güle...")
                    break
            break
        else:
            counter -= 1
            print(f"Giriş başarısız. Kalan deneme hakkınız: {counter}")

    if counter == 0:
        print("Giriş hakkınız tükenmiş ve hesabınız bloke olmuştur.")

if __name__ == '__main__':
    print("Bankamıza hoşgeldiniz.")
    ana_ekran()