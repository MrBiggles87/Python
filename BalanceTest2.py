cost=input("Enter the Purchase cost of all items: ")
tendered= input("Enter the Tendered amount: ")
change=tendered-cost*100

a=(change/200)
print(a, " - £2 Coins")
b=(change - (a*200)) / 100
print(b, " - £1 Coins")
c=(change - (a*200) - (b*100)) / 50
print(c, " - 50p Coins")
d=(change - (a*200) - (b*100) - (c*50)) / 20
print(d, " - 20p Coins")
e=(change - (a*200) - (b*100) - (c*50) - (d*20)) / 10
print(e, " - 10p Coins")
f=(change - (a*200) - (b*100) - (c*50) - (d*20) - (e*10)) / 5
print(f, " - 5p Coins")
