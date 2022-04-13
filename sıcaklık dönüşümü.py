from calendar import c


c=float(input("Havanın Kaç Santigrat Derece Olduğunu Yazınız: "))
fahrenheit=((9/5)*c)+32
kelvin=c+273.15

print("fahrenheit: {}".format(fahrenheit))
print("kelvin: {}".format(kelvin))
