import json

FILE_NAME = "products.json"


def load_products():
    with open(FILE_NAME, mode='r') as file:
        products = json.load(file)
    return products


def save_products(products):
    with open(FILE_NAME, mode='w') as file:
        json.dump(products, file, indent=4)
        