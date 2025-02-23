faiz = 1.59
vade = "36"
krediAdi = " ihtiyaç kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade)+12)
#print(int(krediAdi)) metinsel ifadeyi int bir ifadeye çeviremezsin.
faiz = str(faiz)
print(type(faiz))

vade = int(input (" Lütfen istenilen vade sayısını giriniz : "))
print(type(vade))
vade = vade + 12

#string interpolation 
# seçtiğiniz vade sonucu ortaya çıkan vade :
print (" seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade))
print(" seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi} " .format(vadeSayisi= vade))
print ( f"Seçtiğiniz vade sonucu ortaya çıkan vade : {vade}")

isim = "İsminizi giriniz : "
metin = "merhaba {name}".format(name = 123)
print(metin)

# f - string 
metin = f"Hoşgeldiniz {120 + 3}"
print(metin)

# Listeler 
# döngüler
# fonksiyonlar

dizi = ["ihtiyaç kredisi" , 10 , 5.2 ,True] 
 # dizilerde ve listelerde liste içinde string int dizilenmesi önemsenmez hepsi yazılabilir
print(dizi)

krediler = ["ihtiyaç kredisi" , "taşıt kredisi" , "konut kredisi"]
print(type(krediler))

print(krediler[0])
# programcılar saymaya 0 dan başlar , index listeden o dan başlatır

print(len(krediler))   #lenght (uzunluk , listedeki eleman sayısı index gibi sıfırdan başlamaz)
# print(krediler[3]) => hata verir .

krediler.append("özel kredi") #append listenin sonuna ekler
print(krediler)

krediler.append(" x kredisi")
print(krediler)

krediler.pop(0) #listenin elemanlarını siler (index sayısı ile)eger bir sayı yazmazsa son elemanı siler.

krediler.remove("taşıt kredisi") # listenin elemanlarını siler (listedeki degeri ile , deger "taşıt kredisi")
print(krediler)

  # for
  # i=0 i<10

for i in range (10) :
    print("xx")
    print(i)
print("*************")
for i in range(5,11) :
    print(i)
print("***********")
for i in range(0,51,10) : #başlangıç , varış noktası ama 51 dahil değil 50 son elemandır , artış noktası
    print(i) 
print("***************")  
# for i in range (0.1,0.5) : range fonksiyonu float değerler almaz integer değerler alır.
# print(i)
krediler = ["ihtiyaç kredisi" , "taşıt kredisi" , "konut kredisi"]
for kredi in krediler : 
  print(kredi)
print("**************")
for i in range(len(krediler)) :
      print(krediler[i])

# sonsuz döngü

#while True  :   
   # print("x")
#print("y")

i=0
while i<10 :
    print("x")
    i += 1
print("y")

print("***********")

while True : 
    print("x")
    break

print("*************")

i = 0
while i < len(krediler) :
    print(krediler[i])
    i+=1
    if krediler[i] == "konut kredisi" :
        break

print("*****Son Döngü*****")

krediler = ["ihtiyaç kredisi", "taşit kredisi" ,"konut kredisi"]
i = 0
while i < len(krediler) :
     i+=1
     print(i)
     print (krediler[i])
     if krediler[i] == "konut kredisi" :
      break 

# fonksiyonlar 

fiyat = 100
indirim = 20
# definition define 
def calculate() :
    print(100-20)

def calculateWithParams(fiyat , indirim ) :
     print(fiyat-indirim)

def sayHello(name) :
    print(f"merahba {name}")

calculate()
calculateWithParams(50,10)  
calculateWithParams(100,30)
sayHello("elif")
sayHello("fatma nur")
sayHello("esma")

def calculateAndReturn(fiyat, indirim ) :
     return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat+10)

# void fonksiyonu
def calculatePrice(price,discount) :
   print(price-discount)

def calculatePriceAndReturn(price,discount) :
        return price-discount

print("************")
#fonk1 = calculatePrice(100,50)
#fonk2 = calculatePriceAndReturn(300,100)
#print(f"160.satır {fonk2+100} ")
print("***************") 

# sınıflar => classlar
# modules
#paket yönetimi
# self => this

class Human :
    def talk(self): 
     print("Human is talking")
    def walk(self) :
        print("Human is walking")

# instance => örnek 
human1 = Human()
human1.talk()
human1.walk()