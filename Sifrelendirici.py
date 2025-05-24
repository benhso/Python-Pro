import random

liste="14523AbaCDK*_)^/!'IRSJF"

uzunluk=int(input("bize bir uzunluk ver: "))

sifre=""

for i in range(uzunluk):
    
    sifre+=random.choice(liste)

print("şifreniz:"+sifre)
