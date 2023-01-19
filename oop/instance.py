from .product import Product


# magic method to get all attributes and methods of the class
# can also be used to get all instance attributes when called on an object of the class
# print(Product.__dict__)

iphone_11 = Product("Iphone 11", 1000, 3)
print(iphone_11.name)

print(iphone_11.calc_discount())


# you can also save data of instances in your class for quick access and reuse
# a popular framework that uses it is Django in query results
iphone_x = Product('Iphone X', 850, 10)
iphone_12 = Product('Iphone 12', 1200, 12)
iphone_13 = Product('Iphone 13', 1350, 14)

# example of results without using __repr__
# [<__main__.Iphone object at 0x7f6cb3667fd0>, <__main__.Iphone object at 0x7f6cb3667e80>, <__main__.Iphone object at 0x7f6cb3667e20>, <__main__.Iphone object at 0x7f6cb3667dc0>]
print(Product.all)

for i in Product.all:
    if i.name.endswith('X'):
        i.price = i.calc_discount()
print('finished 1')

for i in Product.all:
    print(i.price)

# with __repr__
print(Product.all)
