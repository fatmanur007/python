def asal_mi(sayi) :
    if sayi <= 1 : 
        print(f"{sayi} bir asal sayı değildir.")
        return
    for i in range (2,int(sayi** 0.5)+1) :
        if sayi % i == 0 :
         print(f"{sayi} bir asal sayı değildir .")
         return 
        print(f"{sayi} bir asal sayıdır")

        # kullanıcıdan giriş olarak çalıştırma 
        sayi = int(input(" bir sayı girin :"))
        asal_mi(sayi)
        



        # hesap makinesi 


        def hesap_makinesi(sayi1,sayi2,islem) :
           if islem ==  '+' :
              sonuc = sayi1+sayi2
              return f"{sayi1} + {sayi2} = {sonuc} "
           elif islem == '-':
              sonuc = sayi1 - sayi2
              return f"{sayi}-{sayi2} = {sonuc}"
           elif islem == '*' :
              sonuc = sayi1 * sayi2
              return f"{sayi1} * {sayi2} = {sonuc}"
           elif islem == "/" :
              if sayi2 == 0 :
                 return f"bölme işlemi için ikinci sayı 0 olamaz !"
              else :
                 sonuc = sayi1 / sayi2
                 return f"{sayi1} / {sayi2}  = {sonuc}"
           else :
              return " geçersiz işlem türü !"
           
           # kullanıcıdan giriş olarak çalıştırma 
           sayi1 = float(input("birinci sayıyı girin ."))
           sayi2 = float(input("ikinci sayıyı girin :"))
           islem = input("işlem türünü seçiniz(+,-,*,/) :")
#sonucu ekrana yazdırma 
print(hesap_makinesi(sayi1,sayi2,islem)) 
