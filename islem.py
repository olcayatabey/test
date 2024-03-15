import hesap

def giris_yap(username, password):
    hesap_adi = None
    for user in hesap.users:
        if user["kullanıcıAdı"] == username and user["şifre"] == password:
            hesap_adi = user
            print(f"Hoşgeldiniz, {username}")
            break
    if not hesap_adi:
        print("Kullanıcı adı yada şifre hatalı")
    return hesap_adi

    return None


def para_cek(hesap, miktar):
    cekilebilir_miktar = hesap["bakiye"] + hesap['ekHesap']
    # Çekilebilir miktar, bakiye ve ek hesabın toplamı
    if cekilebilir_miktar >= miktar:
        # Öncelikle gerçek bakiyesinden çekip çekemeyeceğini kontrol ediyor
        if hesap["bakiye"] >= miktar:
            hesap["bakiye"] -= miktar
        # Eğer bakiye karşılamıyorsa ne kadar ek hesap limitinden kullanacak
        else:
            ek_cekilen = miktar - hesap["bakiye"]
            hesap["bakiye"] = 0
            hesap["ekHesap"] -= ek_cekilen
        print(f"{miktar} TL para çektiniz.\nKalan bakiyeniz: {hesap['bakiye']}\nEk Hesap bakiyeniz: {hesap['ekHesap']}")
    else:
        print("Yetersiz bakiye")


def para_yatir(hesap, yatirim):
    eksik = 3000 - hesap["ekHesap"]
    if yatirim <= eksik:
        hesap["ekHesap"] += yatirim
    else:
        hesap["ekHesap"] = 3000
        bakiye_eklenen = yatirim - eksik
        hesap["bakiye"] += bakiye_eklenen
    print(f"Yeni bakiyeniz: {hesap['bakiye']}\nEk hesap bakiyeniz: {hesap['ekHesap']}")


def bakiye_sorgu(hesap):
    print(f"Bakiyeniz: {hesap.get('bakiye')}\nEk Hesap: {hesap.get('ekHesap')}")


def hesap_bilgi(hesap):
    print("Hesap Bilgileriniz:")
    for key, value in hesap.items():
        print(f"{key}: {value}")