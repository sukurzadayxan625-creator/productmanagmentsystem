import csv

FILE_NAME = "products.csv"
FIELDNAMES = ["name", "price", "quantity"]


def load_csv():
    products = []
    with open(FILE_NAME, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products


def save_csv(products):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(products)

def show_csv(products):
    for product in products:
        print(product)