import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from product import Product
from inheritance import Iphone


# polymorphism

# if parent class was instantiated,
# show method returns the full instance
mac_2017 = Product("MacBook Pro 2017", 2300, 4)
print(mac_2017.show())

# if child class `Iphone` was instantiated,
# show method returns the instance name
iphone_11 = Iphone("Iphone 11", 1000, 3)
print(iphone_11.show())


def show(instance):
    """
    we could even wrap it around another function
    as a form of polymorphism plus abstraction 
    """
    return instance.show()

# for Product instance
print('Product instance:', show(mac_2017))

# for Iphone instance
print("Iphone instance:", show(iphone_11))
