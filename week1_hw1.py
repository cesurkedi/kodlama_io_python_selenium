#Ödev1
#Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.
a = 1           # tamsayı (integer)
b = 2.2         # kayan noktalı sayı (float)
c = 3 + 4j      # karmaşık sayı (complex)
d = 'Ayşe'      # metin (string)
e = True        # boolean

meyveler = ['elma', 'armut', 'çilek', 'muz']                                                    # liste(list)
renkler = ('kırmızı', 'yeşil', 'mavi')                                                          # tuple
telefonlar = {'Ahmet': '0555 555 55 55', 'Mehmet': '0533 333 33 33', 'Ayşe': '0544 444 44 44'}  # dictionary


#Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
# Kurslarim, Tum Kurslar, Kariyer ve SSS ====> String
# Profil duzenledeki ad, soyad, sifre ====> String
# bitirme oranı  ====> int

#Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
ChangePassword = True
NewPassword="12345"
ConfirmPassword="123456"
if(ChangePassword):
   if NewPassword == ConfirmPassword:
    print("İki string birbirine eşittir.")
   else:
    print("İki string birbirine eşit değildir.")