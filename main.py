from product import (
    add_product,
    show_products,
    remove_product,
    filter_by_price
)

from database import load_products, save_products
from csv_operations import load_csv, show_csv

def menu():
    print("\n=== Product Management ===")
    print("1. Məhsul əlavə et")
    print("2. Məhsullari göstər")
    print("3. Məhsul sil")
    print("4. Qiymətə görə filter et")
    print("5. JSON-dan oxu")
    print("6. JSON-a yaz")
    print("7. CSV məlumatlarini göstər")
    print("8. Çixiş")

    return input("Seçiminiz: ")


def main():
    products = load_products()

    while True:
        choice = menu()

        if choice == "1":
            name = input("Məhsulun adi: ")
            price = input("Məhsulun qiyməti: ")
            quantity = input("Məhsulun sayi: ")
            add_product(products, name, price, quantity)

        elif choice == "2":
            show_products(products)

        elif choice == "3":
            name = input("Silinəcək məhsulun adi: ")
            remove_product(products, name)

        elif choice == "4":
            max_price = float(input("Maksimum qiymət: "))
            filtered_products = filter_by_price(products, max_price)
            show_products(filtered_products)

        elif choice == "5":
            products = load_products()

        elif choice == "6":
            save_products(products)

        elif choice == "7":
            csv_products = load_csv()
            show_csv(csv_products)

        elif choice == "8":
            break

        else:
            print("Yanliş seçim.")


if __name__ == "__main__":
    main()