import json


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

        # instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        Iphone.all.append(self)

    def calc_total_price(self):
        return self.price * self.quantity

    def calc_discount(self):
        return self.calc_total_price() * self.pay_rate

    @classmethod
    def read_json(cls, file):
        """
        1. The class is passed as the first argument in a class method
        2. The class doesn't need to be instantiated to use this method,
        but you can also use it with an instance.
        3. It is mainly used when you want to instantiate objects about
        a data that you created on your own but is related to the class.
        """

        return json.load(file)

    @staticmethod
    def validate_integer(num):
        """
        1. Static methods don't send the instance or class as a first argument
        2. It works like a regular function but inside a class
        3. The class also doesn't need to be instantiated to use this method,
        but you can also use it with an instance
        4. Mainly used when you want a method that does something related to the class
        but not to the instances of the class.
        """
        if isinstance(num, float):
            return num.is_integer() # allows numbers with .0 as integers.
        elif isinstance(num, int):
            return True
        return False

    @staticmethod
    def instantiate(instance):
        validate_price = Iphone.validate_integer(instance.get('price'))
        if validate_price:
            phone = Iphone(
                instance.get("name"),
                instance.get("price"),
                instance.get("quantity"),
            )
            return phone
        else:
            return "Invalid price value, must be an integer"

    def __repr__(self):
        """
        To alow printing the content of all without
        just printing the location in memory,
        you use the __repr__ magic attribute
        """
        return f"Iphone({self.name}, {self.price}, {self.quantity})"
