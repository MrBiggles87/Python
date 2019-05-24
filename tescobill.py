product=input("Insert Product Name: ")
price=input("Insert Price: ")
quantity=input("Insert Quantity: ")
amount=float(price)*int(quantity)
vat=amount*15/100
bill=amount+vat
print(" ")
print("Product:",product)
print("Amount:",amount)
print("VAT:","£",vat)
print("Final Bill:","£",bill)
