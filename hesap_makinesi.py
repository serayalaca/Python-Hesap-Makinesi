class HesapMakinesi:
   
    def toplama(a, b):
        return a + b

    def cikarma(a, b):
        return a - b

    def carpma(a, b):
        return a * b

    def bolme(a, b):
        if b != 0:
            return a / b
        else:
            return "Hata: Sıfıra bölünemez!"

sayi1 = input("Birinci sayıyı girin: "))
sayi2 = input("İkinci sayıyı girin: "))
islem = input("İşlem seçin (+, -, *, /): ")


if islem == "+":
    sonuc = HesapMakinesi.toplama(sayi1, sayi2)
elif islem == "-":
    sonuc = HesapMakinesi.cikarma(sayi1, sayi2)
elif islem == "*":
    sonuc = HesapMakinesi.carpma(sayi1, sayi2)
elif islem == "/":
    sonuc = HesapMakinesi.bolme(sayi1, sayi2)
else:
    sonuc = "Geçersiz işlem!"

print("------------------")

print("İşlem Sonucu:", sonuc)
