import products

class Store:

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        if not product:
            raise ValueError("Product should not be empty.")
        self.list_of_products.append(product)
        print(f"Added {product} to the list of Products.")

    def remove_product(self, product):
        if not product:
            raise ValueError("Product should not be empty.")
        if product in self.list_of_products:
            self.list_of_products.remove(product)
        else:
            raise ValueError("Product not found in the store.")


    def get_total_quantity(self):
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.quantity
        return total_quantity


    def get_all_products(self):
        return [product for product in self.list_of_products if product.is_active()]

    def order(self, shopping_list):
        if not isinstance(shopping_list[0], tuple):
            raise ValueError("Shopping list need to contain Item name and quantity as tuple.")
        total_price = 0
        for product, quantity in shopping_list:
            if quantity <= 0:
                raise ValueError("Quantity must be positive.")
            if quantity > product.quantity:
                raise ValueError(
                f"Not enough quantity for product {product.name}. "
                f"Requested: {quantity}, Available: {product.quantity}"
            )
            total_price += product.buy(quantity)

        return total_price


