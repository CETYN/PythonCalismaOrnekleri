gün=(input("günü giriniz:"))
saat=int(input("saati giriniz:"))
dakika=int(input("dakikayı giriniz:"))
saniye=int(input("saniyeyi giriniz:"))
saat = saat*3600
dakika = dakika*60
toplam=saat+dakika+saniye
print( gün ,"günü" , "toplam saniye: {}".format(toplam))
    
