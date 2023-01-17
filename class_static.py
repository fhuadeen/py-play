from main import Iphone

# using the class method
json_file = open('data.json')
iphones = Iphone.read_json(json_file)
print(iphones[0])

print(Iphone.all)

# using the static method
for model in iphones:
    print(Iphone.validate_integer(model['price']))

 
for model in iphones:
    """
    With a static method we could use the data
    from the json file to automatically instantiate objects

    This can be applied to say data from a database to a Python model,
    just like in Django.
    """
    Iphone.instantiate(model)

print(Iphone.all)
