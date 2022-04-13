para=float(input("paranızı giriniz:"))
if(para/1):
    deger=int(para/1)
    para=para%1
    print("1 tl adeti:{}".format(deger))
    if(para/0.5):
        deger=int(para/0.5)
        print("50 kr adeti:{}".format(deger))
        para=para%0.5
        if(para/0.25):
            deger=int(para/0.25)
            print("25 kr adeti:{}".format(deger))
            para=para%0.25
            if(para/0.10):
                deger=int(para/0.10)
                print("10 kr adeti:{}".format(deger))
                para=para%0.10
                if(para/0.05):
                    deger=int(para/0.05)
                    print("5 kr adeti:{}".format(deger))
                    para=para%0.05
                    if(para/0.01):
                        deger=int(para/0.01)
                        print("1 kr adeti:{}".format(deger))
                        para=para%0.01
                        
                        
    
print("toplam bozuk para sayısı".format(deger))
