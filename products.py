class Product:

    def __init__(self, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError("Name muss ein String sein.")
        if not isinstance(price, (int, float)):
            raise TypeError("Preis muss eine Zahl sein.")
        if not isinstance(quantity, int):
            raise TypeError("Menge muss ein Integer sein.")
        if not name:
            raise ValueError("Name should not be empty.")
        if price < 0:
            raise ValueError("Price should not be negative.")
        if quantity < 0:
            raise ValueError("Quantity should not be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity should not be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("The quantity has to be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in the storage")

        total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price




