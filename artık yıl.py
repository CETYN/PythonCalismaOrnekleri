yıl=int(input("Yılınızı Giriniz:"))

if(yıl%400==0):
   
    print("Artık Yıl")
else:
    if((yıl%4==0)and(yıl%100!=0)):  
        print("Artık Yıl")
    
    else:
        print("Artık Yıl Değil")
     
     
    
