a=float(input("Üçgenin 1. Kenarını Giriniz:"))
b=float(input("Üçgenin 2. Kenarını Giriniz:"))
c=float(input("Üçgenin 3. Kenarını Giriniz:"))
if a==b==c :
    print("Eşkenar")
elif (a!=b==c) or (a==b!=c):
    print("İkiz Kenar")
else :
    print("Çok Kenar")
