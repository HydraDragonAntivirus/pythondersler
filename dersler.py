isim = "isiminizi giriniz"
ali = '\nALI\t BABAPRO'.lower().capitalize()

print(isim[::2].upper()+ ali[0::4], isim[0::4].lower().capitalize().startswith("is"))
print(isim[0::4].lower().capitalize())

sayi30 = 4.234

sayi32 = 5

sayi49 = 5**100

print(sayi30)
print(type(sayi30), type(sayi32))
print(sayi49)

sayi50 = 22.001 / 7

print(sayi50)

print(3 + 4)

print(4 - 5)

print(16 / 5.1)

print(51 // 4)

print(round(abs(3.2)** 3 , 4)) # .000000000001 sebep olan şey yuvarlanir

print(isim[::2].upper()+ ali[0::4], isim[0::4].lower().capitalize().startswith("is") + 3)
print(isim[0::4].lower().capitalize())

print(3 + 5 * 6)

print((3 + 2) * 4 - 3 == 17.0)

sayi1 = 10

sayi2 = 11

sayi3 = 10
print(sayi1 > sayi2 - sayi2)
print(type(sayi30), type(sayi32))
print(round(abs(3.2)** 3 , 4)) # .000000000001 sebep olan şey yuvarlanir

print(sayi1 != sayi2)

print(sayi2 <= sayi3 )

a = 1

b = a

a = 5

print(b)

sayi4 = "100asd"
sayi4 = "100"
sayi8 = 100
sayi37 = int(sayi4)
print(type(sayi4))
print(type(sayi8))
print(sayi37 == sayi8)
sayi100 = int(-10.9)
print(sayi100)
sayi101 = int(round(-10.9))
print(sayi101)
sayi201 = 123

sayi203 = str(sayi201)

print(sayi203)
print(type(sayi203))

i = 1

i = i + 2

i += 2

i *= 5

print(i)

i /= 7

print(i)

i //= 7

print(i)

renklerim = ["Siyah", "Beyaz", "Sari", "Mavi", "Yeşil"]

print(type(renklerim))

print(renklerim)

print(type(len(renklerim)))

print(renklerim[1]) #0'dan başlar
print(renklerim[2:])
print(renklerim[:4])
print(renklerim[::2])
# input("cevap?")
print(renklerim)
renklerim.append("Gri")
print(renklerim)
renklerim.insert(0, "Pembe")
print(renklerim)
renklerim.remove("Pembe")
print(renklerim)

renklerim2 = ["Turuncu", "Pembis"]

renklerim.append(renklerim2)
print(renklerim)

renklerim = ["Siyah", "Beyaz", "Sari", "Mavi", "Yeşil"]

renklerim.extend(renklerim2)
print(renklerim)
renklerim.pop()

silinen = renklerim.pop()
print(renklerim)
print(silinen)

renklerim.reverse()

print(renklerim)

renklerim.sort()

renklerim.reverse()
renklerim.sort()
renklerim.reverse()
renklerim.sort(reverse = True)
print(renklerim2)

renklerim3 = ["Siyah", "Beyaz", "Sari", "Mavi", "Yeşil"]

print(renklerim3)
liste2 = sorted(renklerim3)
print(liste2)
print(renklerim3)
print(min(renklerim3))
sayilar = [1, 2, 39, 4, 3, 7, 8]
print(max(renklerim3))
print(sum(sayilar))

for renk in renklerim3:
    print(renk)

print(list(enumerate(renklerim3)))
print(list(enumerate(renklerim3, start=2)))
print ("Siyah" in renklerim3)
print ("Gri" in renklerim3)

stringrenkler = "".join(renklerim3)
print(stringrenkler)
stringrenkler = " ".join(renklerim3)
print(stringrenkler) #Aralarına baştaki arkadaşı koy mesela boşluk
print(type(stringrenkler))
stringrenkler = "".join(renklerim3)
print(stringrenkler),
stringrenkler = "-".join(renklerim3)
renklerimpro = stringrenkler.split("-")
print(renklerimpro)
stringrenkler = " - ".join(renklerim3)
renklerimpro = stringrenkler.split("-") #aynı muamleyi yapacağız yoksa arada boşluk olur
print(renklerimpro)
renklerimpro = "".join(renklerim3)
print(renklerimpro)
renklerimpro = str(renklerim3)
renklerimpro = " - ".join(renklerim3)
yazdir = print
yazdir(renklerimpro)
# renklerimpro2 = "Ma".split(renklerimpro) #Bu Ma olmasına sebep olur
renklerimpro2 = renklerimpro.split("Ma")
yazdir(renklerimpro2)

demet = {"Sari", "Mavi", "Yeşil", "Kirmizi", "Siyah"}

print(type(demet))
demet2 = ("Sari", "Mavi", "Yeşil", "Kirmizi", "Siyah")
print(type(demet2))
print(len(demet))
print(len(demet2))
for kor in demet:
    print(demet)
    print(kor)

# demet[2] = "Pembe" # Hatalı kod
print(demet)
for renkler in demet:
    print(renkler)
    print(demet)
for renkler in demet2:
    print(renkler)
    print(demet2)    
#demet2.append("Pembe") # Hatalı kod add olmalı
#demet.append("Pembe") # Hatalı kod add olmalı demet ve kümede olmaz
demet.add("SARI")
print(demet),
demet.remove("Sari") # Eğer yanlış girersem keyerror verir mesela demet.remove("Sari0")
demet.discard("Sari0") # Bunda hata olmaz keyerror çünkü olmasa dahi hata vermez
demet.discard("Sari")
print(demet)
kume1 = {"Sari", "Mavi", "Yeşil", "Kirmizi", "Siyah"}
kume2 = {"Sari", "Mavi", "Yeşil", "Beyaz", "Gri"}
print(kume1.intersection(kume2)) # Yer değiştirsem aynı
print(kume1.union(kume2)) #Birliktelik ama aynıları göstermez
print(kume1.difference(kume2)) #Bunda farklılık olur sıra değiştirirsem
print(kume2.difference(kume1))
yazdir("Sari" in kume1)
yazdir("Gri" in kume1)
yazdir("Gri" in kume1.uniofn(kume2))
bosliste1 = []
bosliste2 = list()
bosdemet1 = ()
bosdemet2 = tuple()
boskume2 = set()
boskume1 = {} # BU!! bir sözlüktür
print(type(boskume1))

python = set("PYTHON")
print(python)
python2 = set((1, 2, 3, 4, 5))
print(python2)
kisi  = {"isim" : "ali" , "yas" : 20, "cinsiyet" : "m", "hobiler" : ["Sinema", "Konser", "Yazilim"]}
print(kisi["isim"])
print(kisi["cinsiyet"])
kisi["isim"] = "Ahmet"
print(kisi)
kisi.update({"isim" : "Ahmet", "yas" : 30})
print(kisi)
kisi["id"] = 12345
print(kisi)

del kisi["id"]
print(kisi)
for x in kisi:
    print(x)
    print(kisi[x])
print(kisi.keys())
print(kisi.values())
print(kisi.items)
for k, v in kisi.items():
    print(k, v)
#print(kisi["id"]) #hata verir
print(kisi.get("id"))
print(kisi.get("isim"))
print(kisi.get("isim0"))
print(kisi.get("isim", "Bulunamadi"))
print(kisi.get("id", "Bulunamadi"))
# input( "asdf")
print('asdfx')
kitapismi = "Moby Dick"
sayfasayisi = 195
kitapagirligi = 13.45
Yeni = True
#isimler = input("İsminiz Nedir? ")
#print("Merhaba " + isimler)
#yemek = input("En sevdiğiniz yemek? ")
#isminiznedir = input("İsminiz Nedir? ")
#print(isminiznedir + " " + yemek + " " + "Sever")
if False:
   print("Kosul yanlis")
   print("Halen if blogumuz icindeyiz")
if True:
   print("Kosul dogru")
   print("Halen if blogumuz icindeyiz")
if 3 + 5 == 8:
    print("3+5=8")
a = 10
b = 7
if a == b:
    print("a = b")
if a > b:
    print("a > b")
if a != b:
    print("a !=b b")
c = 5 
d = 5
if c != d:
    print("c != d")
else:
    print("c = d")
renk = "Siyah"
if renk == "Beyaz":
   print("Beyaz")
elif renk == "Sari":
    print("Sari")
elif renk == "Mavi":
    print("Mavi")
else: 
    print("Hic biri")

a = 5

b = 8 

c = 10

if a < b or c > a:
    print("koşul doğru")
else:
    print("koşul yanliş")

if a < b and c > a: # Her ikisi doğru olmak zorunda
    print("koşul doğru")
else:
    print("koşul yanliş")

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = 4
if a in liste:
    print("Listede var")
else:
    print("Listede yok") # Listede yoksa tetiklenir

isim = "Python"

a = "p"

if a in isim:
    print("Listede var")
else:
    print("Listede yok") # Küçük p diye yok

if not a in isim:
    print("Listede yok")
else: 
    print("Listede var")

a = 8 
b = 10
if not a == b: 
    print("koşul doğru")
else:
    print("koşul yanliş")

a = "python"
b = "pytho"
b + "n"
print(a)
print(b)

if a == b:
    print("a = b")
else:
    print("a != b")

if a is b:
    print("a = b")
else:
    print("a != b")
    print(id(a))
    print(id(b))
isim = "Muhammet"
yas = 31
yas = str(yas)
print(isim + " " + str(yas) + " " + "Yasinda")
int()
float()
str()
bool()

x = 9

y = 5

""" print(x + y)
print(x - y)
print(x * y)
print(x / y)

 """

print(x // y) #1.8'den 1
print(x % y) #Kalan bulma
print(x ** y)
#sayigirme = int(input("Sayi giriniz: "))
#sayigirme2 = int(input("Ikinci sayiyi giriniz: "))
#
#print(int(sayigirme) + int(sayigirme2))

print(round(9.8))
print(abs(-9))
import math
print(math.sqrt(9))

print(min(9, 10, 56))
print(max(9, 10, 56))
mektup = """merhaba beyfendi
napiyosunuz beyfendi""" #aynen kaydedildi
isim = 'Muhammet'.capitalize() # ilk harfini büyük yap
print(isim)
print(isim[0])
print(isim[0:4])
print(isim[-1])
print(isim[-4:-1])
print(len(isim))
print(isim.capitalize())
isim = "python"
print(isim.find("th"))  # Çıktı: 2
print(isim.replace("th", "yh"))
#isimnedir = input("İsminiz nedir: ")
#print(isimnedir.capitalize())
yagmurlu = False
gunesli = True
if yagmurlu:
    print("hava yagmurlu")
elif gunesli:
    print("hava gunesli")
else: 
    print("Bilinmeyen durum") #ilk kontrol edilen if
ehliyet = False
araba = True
if ehliyet and araba:
    print("araba kullanabilirsiniz")
elif araba and not ehliyet:
    print("Bizim sürücü kursunu tercih ederek araba kullanmay başlayabilirsiniz.")
elif ehliyet or araba:
    print("Araba kullanmana çok az kaldi")
else:
    print("Araba kullanman icin daha cok zaman var")

sicaklik = -5

if sicaklik > 30:
    print("hava cok sicak")
elif sicaklik < 0:
    print("hava cok soguk")
elif sicaklik >= 0:
    print("hava cok soguk degil")

yas = 18
okul = False

#yas = int(input("yasiniz kac?: "))

#okul = (input("okula gidiyon mu? evet/hayir: ").lower())

if yas >= 18 and okul == "hayir":
    print("askere gitme yasiniz geldi")
elif yas >= 18 and okul == "evet":
    print("okulunuz bitince askere gideceksiniz")
elif yas < 18 and okul == "evet":
    print("Askere gitmene daha cok var")
else:
    print("okula git")

liste = [1, 2, 3, 4, 5, 6]

for rakam in liste:
    print(rakam)

isim = "Ahmet"

for harf in isim:
    print(harf)

demet = {1, 2, 3, 4}

for i in demet:
    print(i)

for i in range(0,10,2): #3. argüman ikişer ikişer git
    print(i)

sonuc = 1
for i in range(0,10):
   sonuc *= 2
print(sonuc)
liste1 = ["a", "b", "c"]
liste2 = [1, 2, 3]

for harf in liste1:
    for rakam in liste2:
        print(harf, rakam)

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in liste:
    if i == 3:
        print("3'ü atladik.")
        continue # break kullansam durar
    print(i)

liste = range(100)

for i in liste:
    if i %3 != 0:
        continue
    if i == 81:
        break
    print(i) 
#import os
#os.system('cls')
#while True:
#    print("yok oldun")
x = 2
y = 3
while x < 10:
    print(x)
    x += 1
print("x = ", x)

x = 2 #tekrar 2 yapıyoruz yoksa 10
while x * y < 1000:
    print(x, y)
    x += 2
    y += 2

i = 1
#while True:
#    print(i)
#    i += 1
#    if i == 10000:
#        break # belirtmezsem sonsuza kadar devam
"""     if i %2 == 0:
        i+= 1 # bunu unutursam yani arttırmazsam sadece bir kez 1 gösterir ve devam eder program çünkü 2 çift
        continue
    print(i)
    i += 1 #bunu unutursam yani attırmazsam sadece 1 yazar sürekli devamlı
    if i == 1000:
        break #shift+alt+a """
print("1")
print("2")
print("3")
print("4")
print("5")
i = 1 
#while i <= 1000:
#    print(i)
#    i = i + 1
isciler = ["Mehmet", "Ahmet", "Abdullah", "Kerim" "Ali"]
print(isciler[0])
print(isciler[0:3])

sayi1 = int(input("sayi gir: "))

sayi2 = int(input("sayi gir yine: "))

sayi3 = input("hangi islemi yapacagini gir: (+, -, :, *, **)")

if sayi3 == "+":
    sonuc = sayi1 + sayi2
    print(sonuc)
elif sayi3 == "-":
    sonuc = sayi1 - sayi2
    print(sonuc)
elif sayi3 == "*":
    sonuc = sayi1 * sayi2
    print(sonuc)
elif sayi3 == ":":
    sonuc = sayi1 / sayi2
    print(sonuc)
elif sayi3 == "**":
    sonuc = sayi1 ** sayi2
    print(sonuc)    
else:
    print("Gecersiz islem")
#Belki while ekleyebilirim
#Daha onca şey var string yanına . ekleyip eklediğimiz şeyler fstrip gibi ama onları sadece okudum yazmadım
#sayi = input("Bir sayi giriniz:") #stringdir ondan int çevir
#print(type(int(sayi)))
#sayi = int(input("Bir sayi giriniz: "))

#faktoriyel = 1

#i = 2
#while i <= sayi: #while aynı i += 1 ekstra olarak ekledim for in rangede yoktu
#for i in range(1, sayi + 1): #1 yazmazsam faktoriyel 0 ile carpar sıfır 0 olur
#    faktoriyel  *= i
#    i += 1
#print(f"{sayi}! = {faktoriyel}")
# artıra artıra çarpar 5 x 4 x 3 x 2 x 1 = 120
#i = sayi
#liste = range(1000000)
#while i <= sayi:
#    i /= sayi 
#    if i in liste:

#     print(i)
#    elif i == 0:
#      break   
""" asalbulucu2 = sayi - 1
asalbulucu2 = range(asalbulucu)
print(asalbulucu2)
print(type(asalbulucu2))
asalbulucu2 = asalbulucu2[1:]
print(asalbulucu2)
bolunensayi = 1 # Kendisi de bölen olduğu için 1 olacak
for sayi in asalbulucu2:
    if sayi % asalbulucu != 0:
        bolunensayi += 1
        continue
print(bolunensayi) """ 
sayi = int(input("Lütfen geçerli bir sayi giriniz: "))

bolensayi = 0
for i in range(1, sayi + 1):
    if sayi % i == 0:
        bolensayi += 1
print(bolensayi)
print(f"{sayi} sayisinin {bolen_sayisi} tanesi vardir")
sayi = int(input("Lütfen geçerli bir sayi giriniz: "))

prime = True
for i in range(2, sayi): #bütün doğal sayılar 1'e bölünür
    if sayi %i == 0:
        prime = False
        break
if prime == True:
    print(f"{sayi} sayisi asaldir")
else:
    print(f"{sayi} sayisi asal degildir")
sayi = int(input("Bir sayi giriniz: "))

toplam = 0

gecici_sayi = sayi

while gecici_sayi != 0:

   basamak = gecici_sayi % 10
   toplam += basamak
   gecici_sayi //= 10

print(toplam)

#str_sayi = str(sayi)
#for rakam in str_sayi:
#    toplam += int(rakam)
# ikinci yöntem
#print(toplam)
#sayi1 = int(input("bir sayi giriniz 1/5: "))
#sayi2 = int(input("bir sayi giriniz 2/5: "))
#sayi3 = int(input("bir sayi giriniz 3/5: "))
#sayi4 = int(input("bir sayi giriniz 4/5: "))
#sayi5 = int(input("bir sayi giriniz 5/5: "))
#if sayi1 > sayi2 and sayi1 > sayi3 and sayi1 > sayi4 and sayi1 > sayi5:
#    print(f"En büyük sayi bulundu:{sayi1}")
#if sayi1 < sayi2 and sayi1 < sayi3 and sayi1 < sayi4 and sayi1 < sayi5:
#    print(f"En küçük sayi bulundu:{sayi1}")    
sayilar = input("beş tane sayi giriniz: ")
sayilar_listesi = sayilar.split()
sayilar_listesi = [int(sayi) for sayi in sayilar_listesi]
en_kucuk = min(sayilar_listesi)
en_buyuk = max(sayilar_listesi)
print(f"En küçük: {en_kucuk} En büyük: {en_buyuk}")
liste = []
for i in range(5):
    sayi = int(input("Bir sayi giriniz: "))
    liste.append(sayi)
print(f"en büyük sayi : {max(liste)}")
print(f"en küçük sayi : {min(liste)}")
sayi = int(input("Bir sayi giriniz: "))
karekok = sayi ** 0.5

if karekok == int(karekok):
    print("Tamkare")
else:
    print("Tamkare değil")
yazi = (input("Bir yazi giriniz: "))
yazilar_sayisi = 0
for harf in yazi:
    print(harf)
    

for i in yazilar:
    if i == i:
     yazilar_sayisi += 1
     yazi = i
print(f"{yazilar_sayisi}, {yazi}" )

metin = input("Bir metin giriniz: ")

sozluk = dict()

for harf in metin:
    if harf in sozluk:
       sozluk[harf] += 1
    else:
       sozluk[harf] = 1

for harf, adet in sozluk.items():
    print(harf, adet)
metin = input("Bir metin giriniz: ")

metin2 = ""

for harf in metin:
    if harf == "a":
     harf = "A"
     metin2 += harf
    else:
     metin2 += harf
print(metin2)
sozluk = []
asalsayisi = 0
asalsayisi2 = []
prime = True
sayi = 0
while asalsayisi <= 10000:
 for i in range(2, sayi): #bütün doğal sayılar 1'e bölünür
    if sayi %i == 0:
        prime = False
        break
    else:
        prime = True
 if prime == True:
        print(f"{sayi} sayisi asaldir")
        sozluk.append(sayi)
        asalsayisi +=1
        asalsayisi2.append(asalsayisi)
        sayi += 1
 else:
        print(f"{sayi} sayisi asal degildir")
        sayi += 1

temizsozluk = []
temizsozluksayisi = 0
for i in sozluk:
    if str(i).startswith("3") and str(i).endswith("7"):
     temizsozluk.append(i)
     temizsozluksayisi += 1

print(temizsozluk)
print(temizsozluksayisi)

#tamsozluk = list(zip(sozluk, asalsayisi2))

#print(tamsozluk)

""" sayi = int(input("Lütfen geçerli bir sayi giriniz: "))

prime = True
for i in range(2, sayi): #bütün doğal sayılar 1'e bölünür
    if sayi %i == 0:
        prime = False
        break
if prime == True:
    print(f"{sayi} sayisi asaldir")
else:
    print(f"{sayi} sayisi asal degildir")
sayi = int(input("Bir sayi giriniz: "))
 """



""" 
liste1 = ["a", "b", "c"]
liste2 = [1, 2, 3]

for harf in liste1:
    for rakam in liste2:
        print(harf, rakam)

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9] """

""" for harf in metin:
    if harf in sozluk:
       sozluk[harf] += 1
    else:
       sozluk[harf] = 1

for harf, adet in sozluk.items():
    print(harf, adet) """

prime_list = list()

prime_list.append(2)

sayi = 3

while True:
    prime = True
    for i in range(2, int(sayi ** 0.5) + 1): #0.5 kuvveti yani tam uyumlu 25/5 5 olur bu yüzden bundan büyükse yani +1 o zaman devam ediyoruz
        if sayi %i == 0:
            prime = False
            break
        if prime:
            prime_list.append(sayi)
            if len(prime_list) == 10000:
                break
    sayi += 1        

liste2 = [] # boş liste

for prime in prime_list:
    strprime = str(prime)
    if strprime.startswith("3") and strprime.endswith("7"):
      liste2.append(prime)

print(liste2)
print(len(liste2))
liste1 = list(range(100, 1000))
liste2 = []
liste3 = []
eleman_tmp = []
for eleman in liste1:
    eleman_str = str(eleman)
    for rakam in eleman_str:
        rakam = int(rakam)   
        harf_kup = rakam ** 3
        liste3.append(harf_kup)
        eleman_tmp.append(eleman)
print(liste3)
liste3_toplam = sum(liste3)          
if str(eleman_tmp) == str(liste3_toplam):
    liste2.append(eleman)
    liste3.clear()
    eleman_tmp.clear()
else:
    liste3.clear()
    eleman_tmp.clear()
print(liste2)
print(len(liste2))
# 3 basamaklı sayıların kaç tanaesi rakamların küplerine toplamına eşittir? **3 153 gibi = 1 küp 5 küp 3 küp farklı optimizasyonlar yapılabilir
liste = list(range(100, 1000))
liste2 = []
liste3 = []
liste4 = []
while True:
 for sayi in liste:
    sayi2 = str(sayi)
    for rakam in sayi2:
        rakam2 = int(rakam)
        kup = rakam2 ** 3
        liste2.append(kup)
        liste4.append(sayi)
    toplam = int(sum(liste2))
    toplam2 = int(sum(liste4))
    if str(toplam) == str(toplam2):
        liste3.append(toplam)
        liste2.clear()
        break
    else:
        liste2.clear()
print(liste3)
liste = []
for sayi in range(100, 1000):
     birler = sayi %10
     onlar = (sayi // 10) % 10
     yuzler = sayi // 100
     kup_toplami = ((birler ** 3) + (onlar ** 3) + (yuzler ** 3))
     if kup_toplami == sayi:
        liste.append(sayi)
print(len(liste))
print(liste)
liste = []

for sayi in range(100, 1000):
    toplam = 0
    gecici_sayi = sayi
    while gecici_sayi!= 0:
        basamak = gecici_sayi %10
        toplam += basamak ** 3
        gecici_sayi //= 10
    if toplam == sayi:
        liste.append(sayi)
print(liste)
fibonacci_list = [1, 1]
while len(fibonacci_list) != 100:
      sayi = fibonacci_list[-1]
      sayi2 = fibonacci_list[-2]
      sayi3 = sayi2 + sayi
      fibonacci_list.append(sayi3)
print(fibonacci_list)
fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)
index = 2
while True: 
    fibonacci_list.append(fibonacci_list [index -2] + fibonacci_list[index -1])
    index += 1
    if len(fibonacci_list) == 100:
        break
print(fibonacci_list)
fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)
for i in range(2, 100):
    fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
print(fibonacci_list)
fibonacci_list = [1, 1]
while True:
      sayi = fibonacci_list[-1]
      sayi2 = fibonacci_list[-2]
      sayi3 = sayi2 + sayi
      fibonacci_list.append(sayi3)
      if len(str(fibonacci_list[-1])) == 100:
        break
print(fibonacci_list[-1])
fibonacci_list = list()
fibonacci_list.append(1)
fibonacci_list.append(2)

index = 2
while True:
    fibonacci_list.append(fibonacci_list[index -2] + fibonacci_list[index -1])
    terim = fibonacci_list[index -2] + fibonacci_list[index -1]
    if len(str(terim)) == 1000:
        print(terim)
        print(index)
        break
    index += 1
def selamla(isim)
    print("Merhaba" + isim)

selamla("Ali")

def topla(x, y):
    print(f"x + y = {x + y}")

topla(3, 6)

def carp(x, y):
    print(f"x * y = {x * y}")

carp(3, 6)

def ortalama_hesapla(liste):
    toplam = sum(liste)
    adet = len(liste)
    ortalama = toplam / adet
    print(f"Girilen sayıların ortalaması: {ortalama}")

ortalama_hesapla([3, 2, 5])

def buyuk_harfe_cevir(metin):
    metin = metin.upper()
    print(metin)

buyuk_harfe_cevir("Stringim ben ulan")
def selamla(mesaj, isim= "Anonim"):
    print(f"{mesaj} {isim}.")

selamla("Merhaba", "Elif")
def indirim_yap(fiyat,yuzde = 20):
    indirim_miktarı = fiyat * (yuzde / 100)
    indirimli_fiyat = fiyat - indirim_miktarı
    print(f"İndirimli tutar: {indirimli_fiyat}")

indirim_yap(50)
def topla(x,y):
    print(x + y)
    return x + y # return olmazsa None gelir

sonuc = topla(3, 8)

print(sonuc)

def ortalama_hesapla(x ,y):
    return (x + y) / 2

print(type(ortalama_hesapla)) # function
print(type(ortalama_hesapla(2, 6))) # float

a = ortalama_hesapla(2,6)
b = ortalama_hesapla(6,10)
print(a + b)
def buyuk_harfe_cevir(metin):
    return metin.upper()

a = buyuk_harfe_cevir("AsDfG")
 print(a)
 def buyuk_harfe_cevir(metin):
    return metin.upper() #() koymayı unutma

fonk = buyuk_harfe_cevir

sonuc = fonk("Huk0nD")

print(sonuc)
import math
sonuc = math.factorial(6)
print(sonuc)
sonuc2 = math.sqrt(sonuc)
print(sonuc2)
sonuc3 = math.fabs(65) #flout abs
print(int(sonuc3))
from math import *
import os
sonuc = factorial(5)
print(sonuc)
sonuc2 = sqrt(5)
print(sonuc2)
from math import *
import os
sonuc = factorial(5)
print(sonuc)
sonuc2 = sqrt(5)
print(sonuc2)
import benim_matematik_modulum

sonuc = benim_matematik_modulum.cember_cevresi(4)

print(sonuc)
from benim_matematik_modulum import cember_cevresi
sonuc = cember_cevresi(4)
print(sonuc)
import benim_matematik_modulum as bmm

sonuc = bmm.daire_alani(5)
print(sonuc)
import os
import time
import datetime

import random

for i in range(10):
    print(random.random())
import random

for i in range(10):
    print(random.uniform(10, 30))
import random

for i in range(10):
    print(random.randint(1, 5)) #istisna üst sınır dahil

import random

for i in range(10):
    print(random.randrange(1, 10, 2))
import random

liste = ["Siyah", "Beyaz", "Mavi", "Yeşil", "Gri", "Turuncu"]

print(random.choice(liste))
import random

liste = ["Siyah", "Beyaz", "Mavi", "Yeşil", "Gri", "Turuncu"]

random.sample(liste, 3)

print(liste)
import random

liste = ["Siyah", "Beyaz", "Mavi", "Yeşil", "Gri", "Turuncu"]

print(random.sample(liste, 3))
import random

zarlar = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(1000000):
    zar = random.randint(1, 6)
    zarlar[zar] += 1

for zar in zarlar:
    print(f"{zar} gelme olasılığı: {zarlar[zar] / 1000000}")

import random

alti_alti = 0

deneme_sayisi = 0

while True:
    deneme_sayisi += 1
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    if zar1 == 6 and zar2 == 6:
        alti_alti += 1
        if alti_alti == 10:
           print(f"10 kere 6-6 gelmesi için zarlar {deneme_sayisi} kadar atıldı")
           break
import time

zaman = time.time()
print(zaman) # 1 Ocak 1970'den geçen zaman
import time

baslangic = time.time()

liste = []

for i in range(10000000):
    liste.append(i)
bitis = time.time()

print(bitis - baslangic)
import time

zaman = time.ctime(100000000) #ne kadar saniye geçerse o kadar zaman
print(type(zaman)) #str string
import time

zaman = time.localtime(10000000)
print(zaman)
import time

zaman2 = time.localtime()
zaman = time.asctime() #buna 10000 atamayamazsın ascitime(10000) gbi

print(zaman)

zaman = time.strftime("%d:%m:%Y: %H:%M:%S") #eğer hiç bir yazmazsan geçerli zamanı yazdırır çift tıklayıp modülün içine bakabilirsin pycharmda
print(zaman)
zaman = time.strftime("%d:%m:%Y: %I:%M:%S %p") #eğer hiç bir yazmazsan geçerli zamanı yazdırır çift tıklayıp modülün içine bakabilirsin pycharmda
import time

print("Program başlatıldı")
time.sleep(3)
print("Program sonlandı")
from datetime import date

bugun = date.today()

print(bugun)
print(type(bugun))
print(bugun.day)
print(bugun.month)
print(bugun.year)
print(bugun.weekday())
print(bugun.isoweekday())
from datetime import date
gecmis_tarih = date(2015, 8, 13)
print(gecmis_tarih)
from datetime import date
bugun = date.today()
gecmis_tarih = date(2015, 8, 13)
print(gecmis_tarih.weekday())
gecen_zaman = bugun - gecmis_tarih
print(gecen_zaman)
print(type(gecen_zaman))
from datetime import date
from datetime import datetime

suan = datetime.now()
print(suan)
print(type(suan))
print(suan.month)
print(suan.day)
print(suan.hour)
from datetime import date
from datetime import datetime
from datetime import ctime
suan = datetime.now()
print(suan)
print(suan.ctime())
print(suan.date())
print(suan.time())
print(suan.date().month) # tarih döndür ondan da ay
from datetime import datetime
suan = datetime.now()
gecmis_an = datetime(2014, 5, 26, 6, 45, 32, 123)

print(suan - gecmis_an)
from datetime import datetime
from datetime import date
bugun = date.today()
suan = datetime.now()
print(bugun.strftime("%d:%m:%Y %A"))
print(suan.strftime("%d-%m-%Y-%A"))
print(datetime.strftime(bugun, "%d:%m:%Y"))
print(suan.strftime("%d:%m.%Y"))
from datetime import datetime
from datetime import date
from datetime import timedelta

suan = datetime.now()
tdelta = timedelta(days=7, hours=5, seconds=69)
print(suan + tdelta)
print (suan - tdelta)
from datetime import datetime
from datetime import date
from datetime import timedelta

suan = datetime.now()
print(suan.month)
print(suan.date())
print(suan.day)
print(suan.year)
print(suan.second)
print(suan.year)
from datetime import datetime
from datetime import date
from datetime import timedelta

pazar_sayisi = 0 
for yil in range(1901, 2001): #2001 dahil etmeyecek her zaman başlangıç dahil olur
    for ay in range(1,13):
        if datetime(yil, ay, 1).weekday() == 6: #Ayın 1. günü
            pazar_sayisi += 1
print(pazar_sayisi)