from .main import Iphone


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
