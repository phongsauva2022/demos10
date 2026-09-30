FILE_NAME = "products.csv"

# doc du lieu tu file va tra ve ds doc duoc
def read_products():
    # tao 1 bien kieu list chua tat ca san pham doc duoc tu file
    productList = []

    try:
        with open(FILE_NAME, "r") as file:
            # bo qua dong dau
            file.readline()
            # doc tiep tu dong so 2
            for line in file:
                line = line.strip() # bo ky tu \n o cuoi moi!~ dong

                # cat chuoi thanh mang
                data = line.split(",")
                # tao san pham theo dang dictionary
                product = {
                    "id": data[0],
                    "name": data[1],
                    "price": data[2]
                }

                # them san pham vao list
                productList.append(product)
    except FileNotFoundError:
        print("File ko tim thay")
    except Exception as e:
        print("Error: ", e)

    # print(productList) 
    return productList     
          

# ham hien thi san pham
def display_product(products):
    # kiem tra neu file rong(chua co du lieu)
    if len(products) == 0:
        print("No products")
        return

    # neu co du lieu thi in ra 
    print("\n ----------------Product List-----------------")
    for p in products:
        print(f"ProductID: {p['id']}   ---  ProductName: {p['name']}   ---   Price: {p['price']}")

# ham them san pham
def add_product(products):
    try:
        # cho nhap product id
        product_id = input("Enter Product ID:")
        # kiem tra xem id nay co ton tai hay chua?
        for p in products:
            if p['id'].lower() == product_id.lower():
                print("Id was duplicated")
                return

        # nhap ten
        product_name = input("Enter Product Name:")
        # nhap gia
        product_price = float(input("Enter price:"))
        # tao san pham theo dang dictionary
        product = {"id": product_id, "name": product_name, "price": product_price}
        # them san pham vao danh sach
        products.append(product)
        print("Product added succesfully")
    except ValueError:
        print("Price must be number!!!!")

# ham tim kiem san pham
def search_product(products):
    # nhap id de tim kiem
    product_id = input("Enter Product ID:")

    # tao 1 bien kieu list de chua cac san pham tim thay duoc
    found = []
    for p in products:
        if product_id.lower() in p['id'].lower():
            found.append(p)

    # kiem tra xem co tim kiem duoc hay ko
    if len(found) > 0:
        display_product(found)
    else:
        print("No product found")


# ham luu vao file
def save_products(products):
    try:
        with open(FILE_NAME, 'w') as file:
                # ghi lai dong`` dau` tien
                file.write("ProductID,ProductName,Price\n")
        
                # ghi cac dong tiep theo dua vao ds
                for p in products:
                    line = p['id'] + "," + p['name'] + "," + str(p['price']) + "\n"
                    file.write(line)
        
                print("Write successfully")
    except Exception as e:
        print("Error: ", e)


# Main Menu
def main():
    # doc du lieu khi chuong trinh chay, goi ham readproducts()
    products = read_products()

    while True:
        print("********************MENU*********************")
        print("1. Display all products")
        print("2. Add product")
        print("3. Search product by id")
        print("4. Save products to file")
        print("5. Exit program")
        print("********************MENU*********************")

        choice = input("Enter your choice:")
        if choice == "1":
            display_product(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            search_product(products)
        elif choice == "4":
            save_products(products)
        elif choice == "5":
            print("Exit program")
            break
        else:
            print("Wrong choice. Enter 1-5")

# goi ham main
main()

