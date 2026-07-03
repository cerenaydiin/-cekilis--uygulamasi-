tel_rehberi = dict()

def tel_no_ekle(x):
    print("***Numara ekleme ekranına hoşgeldiniz***")
    numara_isim_al = input("Lütfen kayıt edilecek kişinin adını yazınız. :")
    numara_no_al = input("Lütfen kayıt edilecek kişinin numarasını yazınız. :")
    
    x = tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f"{numara_isim_al}'adlı kişi telefon listesine eklendi...")

def tel_rehber_goster(x):
    print("Rehbere Hos geldiniz")
    kisi_sayisi = len(x)
    print(f"Rehberinizdeki kayıtlı kişi sayısı : {kisi_sayisi}")

    for i,j in x.items():
        print(i,":",j)
       
    input("Devam edilsin mi?")

def no_sil(x):
    print("kişi silme ekranına hoş geldiniz!")
    silinecek_kisi = input("silinecek kişiyi yazınız : ")
    tel_rehberi.pop(silinecek_kisi)
   
   
    input("Devam edilsin mi? ")

while True: 
        print("***HOŞGELDİNİZ***")
        print("***SEÇİM YAPINIZ***")
        secim_yap = int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n4-Çıkış\n"))

        if secim_yap == 1:
            tel_no_ekle(tel_rehberi)

        elif secim_yap == 2:
            no_sil(tel_rehberi)

        elif secim_yap == 3: 
            tel_rehber_goster(tel_rehberi)
        
        elif secim_yap == 4:
            print("Program Sonlandırıldı...")
            break

        else: 
            print("Lütfen uygun tuşlara basınız.")
