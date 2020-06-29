# TURKCE 
dogru1 = int(input("Turkce Dogru Sayinizi Giriniz: "))
yanlis1 = int(input("Turkce Yanlis Sayinizi Giriniz: "))
net1 = dogru1 - (yanlis1 / 4)
bos1 = 40 - (dogru1 + yanlis1)
# SOSYAL
dogru2 = int(input("Sosyal Dogru Sayinizi Giriniz: "))
yanlis2 = int(input("Sosyal Yanlis Sayinizi Giriniz: "))
net2 = dogru2 - (yanlis2 / 4)
bos2 = 20 - (dogru2 + yanlis2)
# MATEMATIK
dogru3 = int(input("Matematik Dogru Sayinizi Giriniz: "))
yanlis3 = int(input("Matematik Yanlis Sayinizi Giriniz: "))
net3 = dogru3 - (yanlis3 / 4)
bos3 = 40 - (dogru3 + yanlis3)
# FEN 
dogru4 = int(input("Fen Dogru Sayinizi Giriniz: "))
yanlis4 = int(input("Fen Yanlis Sayinizi Giriniz: "))
net4 = dogru4 - (yanlis4 / 4)
bos4 = 20 - (dogru4 + yanlis4)



toplamnet = net1 + net2 + net3 + net4
toplamdogru = dogru1 + dogru2 + dogru3 + dogru4
toplamyanlis = yanlis1 + yanlis2 + yanlis3 + yanlis4
toplambos = bos1 + bos2 + bos3 + bos4 
print(" ^^^ ")
print(f'Turkce Netiniz: {net1} ')
print(" ^^^ ")
print(f' Sosyal Netiniz: {net2} ')
print(" ^^^ ")
print(f'Matematik Netiniz: {net3} ')
print(" ^^^ ")
print(f'Fen Netiniz: {net4} ')
print(" ^^^ ")
print(f'Toplam Dogru Sayiniz: {toplamdogru}')
print(" ^^^ ")
print(f'Toplam Yanlis Sayiniz: {toplamyanlis}')
print(" ^^^ ")
print(f'Toplam Bos Sayiniz: {toplambos}')
print(" ^^^ ")
print(f'Toplam Netiniz: {toplamnet}')