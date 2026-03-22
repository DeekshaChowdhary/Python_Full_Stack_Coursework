
##E-commerce Website Example

products = [['laptop',560000],
            ['phone',760000],
            ['charger',2000],
            ['mouse',700],
            ['buds',3500]
            ]  # nested list


def view_products():
    print('ID'.ljust(5), 'Product Name'.ljust(15), 'Price')
    for i in range(len(products)):
        print(str(i).ljust(5), products[i][0].ljust(15), products[i][1])


def add_product():
    product_name = input("Enter the product name: ")
    price = int(input("Enter the product price: "))
    products.append([product_name, price])
    print(f"{product_name} is added")


def del_product():
    product_id = int(input("Enter the product Id: "))
    print(f"{products[product_id]} is deleted")
    products.pop(product_id)


while True:
    print("--------Welcome to the flipkart admin side---------")
    print("1.View Products")
    print("2.Add Product")
    print("3.Delete Product")
    print("4.Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        view_products()

    elif ch == 2:
        add_product()

    elif ch == 3:
        del_product()

    elif ch == 4:
        print("Thank you")
        break
