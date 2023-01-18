from main import Product
import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, BASE)

# using the class method
json_file = open(f'{BASE}/oop/data.json')
iphones = Product.read_json(json_file)
print(iphones[0])

# using the static method
for model in iphones:
    print(Product.validate_integer(model['price']))

 
for model in iphones:
    """
    With a static method we could use the data
    from the json file to automatically instantiate objects

    This can be applied to say data from a database to a Python model,
    just like in Django.
    """
    Product.instantiate(model)

print(Product.all)
