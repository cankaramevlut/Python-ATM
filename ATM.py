class Atm:
    def __init__(self,pin,bakiye) :
        self.pin=pin
        self.bakiye=bakiye

    def bakiyeyi_sorgula(self):
        return self.bakiye

    def para_cek(self, miktar):
        if miktar > 0 and miktar <= self.bakiye:
            self.bakiye -= miktar
            return f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL"
        elif miktar <= 0:
            return "Geçersiz miktar. Lütfen geçerli bir miktar girin."
        else:
            return "Yetersiz bakiye."   

    def para_yatir(self, miktar):   
        if miktar>0:
            self.bakiye += miktar 
            return f"{miktar} TL Yatırıldı. Yeni bakiye: {self.bakiye} TL"
        
        else:
            return "Geçersiz miktar. Lütfen geçerli bir miktar girin."
        



hesapA=Atm(321,100)  # Şifre 321 bakiye 100 TL


while True: 
    girilenPin=int(input("PIN Giriniz: "))

    if girilenPin == (hesapA.pin):
        print("Hoş Geldiniz ")

        while True:
            print("\n1. Bakiye Sorgula\n2. Para Çek\n3. Para Yatır\n4. PIN Değiştir\n5. Çıkış")
            secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")   

            if secim == "1":
                print(f"Bakiyeniz: {hesapA.bakiyeyi_sorgula()} TL")

            elif secim == "2":
                miktar = float(input("Çekmek istediğiniz miktarı girin: "))
                sonuc = hesapA.para_cek(miktar)
                print(sonuc)
            
            elif secim == "3":
                miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
                sonuc=hesapA.para_yatir(miktar)
                print(sonuc)

            elif secim == "4":
                yeni_pin = input("Yeni PIN girin: ")
                hesapA.pin = yeni_pin
                print("PIN başarıyla değiştirildi.")

            elif secim == "5":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçenek. Lütfen tekrar deneyin.")
    else:
        print("Yanlış PIN. Lütfen tekrar deneyin.")            

