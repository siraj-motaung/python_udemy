class Product:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        """
        Getter: Runs when you call product.price
        """
        print("GETTER!!!!!")
        return self._price
    
    @price.setter
    def price(self, price):
        """
        Setter: Called when you do product.price = 100
        """
        print("SETTER!!!!!")
        if price > 0 and price < 100:
            self._price = price
        else:
            raise ValueError("Invalid price")


product = Product(20)
print(f"Calling getter: price = {product.price}")
product.price = 25



