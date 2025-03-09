from products import Product

class Store:
    """
    A class representing a store that manages a collection of products.

    Attributes:
        list_of_products (List[Product]): A list of Product instances available in the store.
    """

    def __init__(self, list_of_products):
        """
        Initialize the store with a list of products.

        Args:
            list_of_products (List[Product]): The initial list of products.

        Raises:
            TypeError: If list_of_products is not a list or if any item is not a Product instance.
        """
        # 1. Check the data type of list_of_products
        if not isinstance(list_of_products, list):
            raise TypeError("list_of_products must be of type 'list'.")

        # 2. Check the data type of each item in the list
        for item in list_of_products:
            if not isinstance(item, Product):
                raise TypeError("All items in list_of_products must be Product instances.")

        # If all checks pass, store the list
        self.list_of_products = list_of_products

    def add_product(self, product):
        """
        Add a new product to the store inventory.

        Args:
            product (Product): The product to add.

        Raises:
            TypeError: If product is not a Product instance.
            ValueError: If product is None (or falsy).
        """
        # Check the data type
        if not isinstance(product, Product):
            raise TypeError("The product must be a valid Product instance.")

        # Check value
        if not product:
            raise ValueError("Product should not be empty (None).")

        self.list_of_products.append(product)
        print(f"Added {product} to the list of Products.")

    def remove_product(self, product):
        """
        Remove a product from the store inventory.

        Args:
            product (Product): The product to remove.

        Raises:
            TypeError: If product is not a Product instance.
            ValueError: If product is None (or falsy) or if the product is not found in the inventory.
        """
        # Check the data type
        if not isinstance(product, Product):
            raise TypeError("The product must be a valid Product instance.")

        # Check value
        if not product:
            raise ValueError("Product should not be empty (None).")

        if product in self.list_of_products:
            self.list_of_products.remove(product)
        else:
            raise ValueError("Product not found in the store.")

    def get_total_quantity(self):
        """
        Calculate the total quantity of items available in the store.

        Returns:
            int: The sum of quantities for all products in the store.
        """
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        """
        Retrieve a list of all active products in the store.

        Returns:
            List[Product]: A list of Product instances that are active.
        """
        return [product for product in self.list_of_products if product.is_active()]

    def order(self, shopping_list):
        """
        Process an order based on a shopping list, ensuring the entire order is
        canceled if any item is invalid.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples where each
                tuple contains a Product and the quantity to purchase.

        Returns:
            float: The total price for the order.

        Raises:
            ValueError: If a product does not have sufficient quantity or if an
                        invalid quantity is provided.
        """
        # First, validate the structure of the shopping list.
        if not all(isinstance(item, tuple) and len(item) == 2 for item in shopping_list):
            raise ValueError("Shopping list must contain tuples of (Product, quantity).")

        total_price = 0

        for product, quantity in shopping_list:
            if quantity <= 0:
                raise ValueError("Quantity must be positive.")
            if quantity > product.quantity:
                raise ValueError(
                    f"Not enough quantity for product {product.name}. "
                    f"Requested: {quantity}, Available: {product.quantity}"
                )

            total_price += product.price * quantity

        for product, quantity in shopping_list:
            product.buy(quantity)

        return total_price
