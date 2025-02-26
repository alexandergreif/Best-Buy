from products import Product
from store import Store



def main():
    # bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    # mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    #
    # print(bose.buy(50))
    # print(mac.buy(100))
    # print(mac.is_active())
    #
    # print(bose.show())
    # print(mac.show())
    #
    # bose.set_quantity(1000)
    # print(bose.show())

    product_list = [
        Product("MacBook Air M2", 1450, 100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    shopping_list = [(products[0], 1), (products[1], 2)]
    print(type(shopping_list[0]))
    print(best_buy.order(shopping_list))


if __name__ == "__main__":
    main()