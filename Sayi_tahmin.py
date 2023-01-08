import random
import time
print("\n1- Bebek Oyuncağı (1-10) hak:2\n2- Orta (1-100) hak:5\n3- Zor (1-1000) hak:20\n4- İmkansız (1-10000) hak:5")
sayi = 0
soru= input("\nSeviye seçiniz : \n")
if soru == "1":
    sayi=random.randint(1,10)
    hak = 2
elif soru == "2":
    sayi=random.randint(1,100)
    hak = 5
elif soru == "3":
    sayi=random.randint(1,1000)
    hak = 20
elif soru == "4":
    sayi=random.randint(1,10000)
    hak = 5

sayac = 0
sayac2 = hak
while hak > 0:
    hak-=1
    sayac+=1
    
    tahmin = int(input(f"\nTahmininiz nedir? {(sayac2)} hakkınız kaldı! :\n "))
    if sayi == tahmin :
        if soru == "1":
            print(f"\nTebrikler {sayac}. defada bildiniz. Toplam puanınız {100-(50)*(sayac-1)}\n")
            break
        elif soru == "2":
            print(f"\nTebrikler {sayac}. defada bildiniz. Toplam puanınız {100-(20)*(sayac-1)}\n")
            break
        elif soru == "3":
            print(f"\nTebrikler {sayac}. defada bildiniz. Toplam puanınız {100-(5)*(sayac-1)}\n")
            break
        elif soru == "4":
            print(f"\nTebrikler {sayac}. defada bildiniz. Toplam puanınız {100-(20)*(sayac-1)}\n")
            break
        
    elif sayi > tahmin:
        print("\nYukarı\n")
        sayac2-=1
    else:
        print("\nAşağı\n")
        sayac2-=1
    if hak==0:
        print(f"\nHakkınız Bitmiştir\n cevap:{sayi}\n")
        break