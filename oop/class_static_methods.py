import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from product import Product


# using the class method
json_file = open(f'{BASE}/oop/data.json')
query = "Sam"

# abstracted away the methods under filter class method
iphones = Product.filter(json_file, query)
print(len(iphones))

# using the static method
 
for model in iphones:
    """
    With a static method we could use the data
    from the json file to automatically instantiate objects

    This can be applied to say data from a database to a Python model,
    just like in Django.
    """
    Product.instantiate(model)

print(Product.all)
