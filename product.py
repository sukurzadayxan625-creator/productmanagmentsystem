def add_product(products, name, price, quantity):
    products.append({"name": name, "price": price, "quantity": quantity})


def show_products(products):
    for product in products:
        print(product)


def remove_product(products, name):
    products.remove(next(product for product in products if product["name"] == name))


def filter_by_price(products, max_price):
    return [product for product in products if float(product["price"]) < max_price]