anapara=float(input("Yatırmak İstediğiniz Tutarı Giriniz:"))
yıl1=(anapara*0.14)+anapara
yıl2=(yıl1*0.14)+yıl1
yıl3=(yıl2*0.14)+yıl2
print("""
      Birinci yıl Ana Paranız: {}
      ikinci yıl Ana Paranız: {}
      üçüncü yıl Ana Paranız: {}
      """.format(yıl1,yıl2,yıl3))
