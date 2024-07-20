import random

sandi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
user = input("masukkan panjang  sandi anda:")
password = ''

for i in range(int(user)):
    password += random.choice(sandi)

print(password)    