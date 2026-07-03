import random
import time 

kullanicilar = list()

def kullanici_ekle(x):
    print("-"*30)
    print("Kullanıcı ekleme ekranına hoş geldiniz!")
    ekle = input("Lütfen eklemek istediğiniz kullanıcıyı yazınız : ")
    kullanicilar.append(ekle)
    input("Devam etmek için ENTER tuşuna basınız...")

def kullanici_gör(x):
    say = 1 
    print("-"*30)
    for i in x:
        print(str(say)+".Kullanıcı adı: " , i)
        say+=1
    print("-"*30)
    input("Devam etmek için ENTER tuşuna basınız...")


def sec(x):
    say = 1
    kisi_sec = int(input("Kaç kişi seçilsin ? : "))
    rastgele_sec = random.sample(x , kisi_sec)

    for i in rastgele_sec:
        print(str(say)+".Kullanıcı adı : " , i)
        say+=1
        print("Diğer kişiler sistemden seçiliyor...")
        time.sleep(3)
    print("-"*30)
    input("Devam etmek için ENTER tuşuna basınız...")


def karistir(x):
    print("-"*30)
    say = 1
    random.shuffle(x) 
    #listelerin içindeki sıralamayı shuffle ile karıştırırız.

    for i in x: 
        print(str(say)+".Kullanıcı adı : " , i)
        say+=1
    print("-"*30)
    input("Devam etmek için ENTER tuşuna basınız...")


while True :

    print("***ÇEKİLİŞ UYGULAMASINA HOŞGELDİNİZ!***")
    secim = int(input("1-kullanıcı ekle\n2-kullanıcı gör\n3-kullanıcıları karıştır\n4-rastgele seçin\n"))

    if secim == 1:
        kullanici_ekle(kullanicilar)
    
    elif secim == 2:
        kullanici_gör(kullanicilar)

    elif secim == 3:
        karistir(kullanicilar)

    elif secim == 4: 
        print("Kişi seçme alanı hesaplanıyor...")
        time.sleep(5)
        sec(kullanicilar)


    else: 
        print("Lütfen uygun bir seçim yapınız...")


    

