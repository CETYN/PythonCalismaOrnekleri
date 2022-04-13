harf=(input("harfinizi giriniz:"))
liste=[("a"),("e"),("ı"),("i"),("o"),("ö"),("u"),("ü")]

for x in liste:
    
    if(x == harf ):
     print("sesli harf:{}".format(x))
     break
    
else:
        print("sessiz harf:{}".format(harf))
        
    
    
