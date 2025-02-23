print ("AcunmedyaAkademi")
baslik = "Taşıt Kredisi"
print(baslik)
# string => metinsel ifade 
baslik = "ihtiyaç kredisi"
print(baslik)
#int , integer => tam sayı 
vade = 36
ekVade = 6
vade2 = "36"

# float , decimal ,double 
aylikOdeme = 200.50

# bool , boolean => True veya false
yükselistemi = False

# matematiksel operatörler 


# + 
print(5+5)
print(vade+12)
print(vade + ekVade )
print(36+6)

# - 
print(5-5)
print(vade - 12)
print (vade - ekVade)
print(36-6)

# *
print(5*5)
print(vade*2)
print(vade*ekVade)
print(10*10)

# / 
print(5/5)
print(vade/2)
print(vade/ekVade)
print(10/2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod alma işlemleri
print(10%2)
print(vade % 5)
print(vade % ekVade)
print(30%10)


# mantıksal operatörler

print(1==1)
print(1==2)

# CTRL K + CTRL C
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)


print(1 != 1)
print(1 != 2)

# or and 

print( 1 > 2 or 5 > 2 )
print( 1 > 2 and 5 > 2)
print( 1 > 2 or 5 > 2 and 3 > 2)

print ( 1 > 2 and 5 > 2 and 3 > 2)

print (2 > 1 or 1 > 2 and 3 > 2)


# karar yapıları 
# ıf else 
sayi1 = 15
sayi2 = 15
 # sayi1 sayi2 den büyükse ekrana sayı 1 daha büyük yazdır 
 # condition (sayi1 > sayi2) , (şart) bu demek 

#indent ( diğer dillerde , süslü parantezi ,{} , ıf bloğunun içindeki 
# şartaları yazmakta kullandığımız süslü parantez ; pythonda 1 tab tuşuna
#  basarak 1 indent boşluk koyarak oluşturulur.  )

if sayi1 > sayi2 :
    print ("sayı 1 sayı 2 ' den küçüktür ")
    # eğer if bloğuna girmezse 
elif sayi1 == sayi2:
    print("iki sayı eşittir")
    # eğer if ve else if bloklarına hiç birine girmez ise 
else :
    print("sayi 1 sayı 2 ' den büyüktür ")

print("***************")

if sayi1 < sayi2 :
    print("sayı 1 sayı 2' den küçüktür ")
if sayi1 == sayi2 :
    print("iki sayı eşittir")
else :
    print("sayı 1 sayı 2 ' den küçüktür")

print (" burası if bloğunun dışıdır ")
