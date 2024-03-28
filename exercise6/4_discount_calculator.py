purchase_amount = float(input("Input Number : $"))

if purchase_amount > 100:
    discount = 0.1  # 10% discount
elif purchase_amount > 50:
    discount = 0.05  # 5% discount
else:
    discount = 0  # no discount   
    
total = purchase_amount - (purchase_amount * discount)    

print("Price is = ${:.2f}".format(purchase_amount))
print("price after discount = ${:.2f}".format(total))