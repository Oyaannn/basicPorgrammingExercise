product1 = ["Facewash"  , 50000, 25]
product2 = ["Toner"     , 75000, 18]
product3 = ["Sunscreen" , 60000, 20]

transaksi   = 0
keuntungan  = 0

def transaction(product):
    global transaksi
    global keuntungan
    if product[2] == 0:
        print("sorry the item is sold out:(")
    else:
        buy = int(input("How Much to Buy : "))
        
        if buy > product[2]:
            print("Out of stock!")
        else:
            product[2] -= buy
            total = int(buy * (product[1] + (product[1] * 10/100)))
            keuntungan += int(buy * (product[1] * 10/100))
            transaksi += 1
            
            print(" ")
            print(f"Items Sold   : {product[0]} | {buy} Pcs ")
            print(f"Total        : Rp {total:,}")
            print(f"Profit Items : Rp {product[1] * 10/100:,}")
            print("=========================================")
            print(f" Transaction  : {transaksi}")
            print(f" Total Profit : Rp {keuntungan:,}")
            print(" ")
            
def item():
    print(">>>>>>>>>>>>> LIST PRODUCT <<<<<<<<<<<<<")
    print("NO|\t NAME\t  |   PRICE\t | STOCK")
    print(f"1 |  {product1[0]}\t  | Rp {int(product1[1] + (product1[1] * 10/100)):,}\t |  {product1[2]}")
    print(f"2 |  {product2[0]}\t  | Rp {int(product2[1] + (product2[1] * 10/100)):,}\t |  {product2[2]}")
    print(f"3 |  {product3[0]}\t  | Rp {int(product3[1] + (product3[1] * 10/100)):,}\t |  {product3[2]}")
    print(" ")

while (True):
    print("WELCOME TO BEAUTY STORE:)")
    print("Menu :")
    print("1. Product List")
    print("2. Close")
    siti = input("Enter Here: ")
    if siti == '1':
        item()
    elif siti == '2':
        print("Thanks for Transaction!")
        break
    elif siti == "Facewash":
        transaction(product1)
        item()
    elif siti == "Toner":
        transaction(product2)
        item()
    elif siti == "Sunscreen":
        item()
        transaction(product3)
    else:
        print("----!!Not Found!!----")