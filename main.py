
class Item:

    # class attributes
    pay_rate = 0.8
    
    def __init__(self, name: str, price: float, quantity: int=0):
        # assert the types of your instance attributes
        assert type(name) == str, "Name must be a string"
        if type(price) != float and type(price) != int:
            raise ValueError("Price must be a float or integer")
        assert type(quantity) == int, "Quantity must be an integer"

        # assert the values of your instance attributes
        assert price >= 0, "Price must be greater than or equal to 0"
        assert quantity >= 0, "Quantity must be greater than or equal to 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calc_total_price(self):
        return self.price * self.quantity

    def calc_discount(self):
        return self.calc_total_price() * self.pay_rate

# magic method to get all attributes and methods of the class
# can also be used to get all instance attributes when called on an object of the class
print(Item.__dict__)

iphone_11 = Item("Iphone 11", 1000, 3)
print(iphone_11.name)

print(iphone_11.calc_discount())


# exception class