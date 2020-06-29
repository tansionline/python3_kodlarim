
dogru = int(input("Dogru Sayinizi Giriniz: "))
yanlis = int(input("Yanlis Sayinizi Giriniz: "))
netdegeri = int(input("Kac Yanlis Dogrunu Goturuyor: "))
net = dogru - (yanlis / netdegeri)
sinirli_float_degeri = round(net, 2)
print(f'Netiniz: {sinirli_float_degeri} ')

