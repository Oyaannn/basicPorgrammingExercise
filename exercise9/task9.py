products = []

while True:
    print("====== Chosee the Menu: ======")
    print("1. List products")
    print("2. Add product")
    print("3. Remove product by name")
    print("4. Remove product by number")
    print("5. Exit")

    choice = int(input("Please input menu: "))

    if choice == 1:
        print("Products:")
        for i, product in enumerate(products, 1):
            print(f"{i}. {product}")
    elif choice == 2:
        product = input("Add the product: ")
        products.append(product)
    elif choice == 3:
        product = input("Remove the product by name: ")
        if product in products:
            products.remove(product)
        else:
            print("Product not found")
    elif choice == 4:
        try:
            index = int(input("Remove the product by number: "))
            if 0 < index <= len(products):
                del products[index - 1]
            else:
                print("Index out of range")
        except ValueError:
            print("Invalid input")
    elif choice == 5:
        print("Close")
        break
    else:
        print("Invalid choice")