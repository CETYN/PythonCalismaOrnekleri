
print("""
      MENÜ
      ÇORBA = 10tl
      PİLAV = 15tl
      DÖNER = 20tl
      ET = 100tl
      """)
corba = 10
pilav = 15
doner = 20
et = 100

sipariş = input("Siparişinizi Veriniz:")
if(sipariş=="çorba"): 
   corbabahsis= corba-(corba*0.08)
   #print(corbabahsis)
   corbabahsis= corbabahsis*0.15
   print("Bahşiş:{}".format(corbabahsis))
   
elif(sipariş=="pilav"):
   pilavbahsis= pilav-(pilav*0.08)
   #print(pilavbahsis)
   pilavbahsis= pilavbahsis*0.15
   print("Bahşiş:{}".format(pilavbahsis))
   
elif(sipariş=="döner"):
   dönerbahsis= doner-(doner*0.08)
   #print(dönerbahsis)
   dönerbahsis= dönerbahsis*0.15
   print("Bahşiş:{}".format(dönerbahsis))
   
elif(sipariş=="et"):
   etbahsis= et-(et*0.08)
   #print(etbahsis)
   etbahsis= etbahsis*0.15
   print("Bahşiş:{}".format(etbahsis))

else:
    print("Menü Dışı Sipariş Verdiniz...")




   
