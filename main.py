
class Iphone:

    # class attributes
    pay_rate = 0.8

    # to save instances
    all = []
    
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

        Iphone.all.append(self)

    def calc_total_price(self):
        return self.price * self.quantity

    def calc_discount(self):
        return self.calc_total_price() * self.pay_rate

    # to alow printing the content of all without just printing the location in memory
    # You use the __repr__ magic attribute
    def __repr__(self):
        return f"Iphone({self.name}, {self.price}, {self.quantity})"

# magic method to get all attributes and methods of the class
# can also be used to get all instance attributes when called on an object of the class
# print(Iphone.__dict__)

iphone_11 = Iphone("Iphone 11", 1000, 3)
print(iphone_11.name)

print(iphone_11.calc_discount())


# you can also save data of instances in your class for quick access and reuse
# a popular framework that uses it is Django in query results
iphone_x = Iphone('Iphone X', 850, 10)
iphone_12 = Iphone('Iphone 12', 1200, 12)
iphone_13 = Iphone('Iphone 13', 1350, 14)

# example of results without using __repr__
# [<__main__.Iphone object at 0x7f6cb3667fd0>, <__main__.Iphone object at 0x7f6cb3667e80>, <__main__.Iphone object at 0x7f6cb3667e20>, <__main__.Iphone object at 0x7f6cb3667dc0>]
print(Iphone.all)

for i in Iphone.all:
    if i.name.endswith('X'):
        i.price = i.calc_discount()
print('finished 1')

for i in Iphone.all:
    print(i.price)

# with __repr__
print(Iphone.all)
