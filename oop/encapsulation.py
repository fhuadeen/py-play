import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from oop.inheritance import Iphone, Samsung


# encapsulation
iphone_8 = Iphone(name='Iphone 8', quantity=25, price=650, broken_phones=3)
print(iphone_8.broken_phones)
iphone_8.price = 40
print(iphone_8)
print(Iphone.all)

galaxy_s20 = Samsung('Galaxy S20', 650, 25, 8)
print(galaxy_s20.broken_phones)
print(Samsung.all)










def counte(*, string: str):
    print("first")
    return len(string)

def counte(*, li: list):
    print("last")
    return len(li)

# print(counte(li="fhuad"))