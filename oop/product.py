import json


class Product:

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
        self.__price = price
        self.quantity = quantity

        Product.all.append(self)

    @property
    def price(self):
        """Encapsulation: Make the price attribute read-only"""
        return self.__price

    @price.setter
    def price(self, value):
        """Update the price attribute
        We add the price-negative check again during updating
        """
        if value < 0:
            raise ValueError("price must be positive")
        self.__price = value

    def calc_total_price(self):
        return self.price * self.quantity

    def calc_discount(self):
        return self.calc_total_price() * self.pay_rate

    @classmethod
    def __connect_to_db(cls):
        """Fake connection to the database"""
        return "connected"

    @classmethod
    def __read_json(cls, file, query=None):
        """
        1. The class is passed as the first argument in a class method
        2. The class doesn't need to be instantiated to use this method,
        but you can also use it with an instance.
        3. It is mainly used when you want to instantiate objects about
        a data that you created on your own but is related to the class.
        """
        data = json.load(file)
        if not query:
            return data
        return tuple(filter(lambda x: x.get("name").startswith(query), data))

    # abstraction
    @classmethod
    def filter(self, file_obj, query=None):
        """We can abstract away the methods that
        connect to the database and retrieve data
        by adding __ to their names"""
        cursor = Product.__connect_to_db()
        if cursor == "connected":
            instance = Product.__read_json(file_obj, query)
            return instance

    @staticmethod
    def __validate_integer(num):
        """
        1. Static methods don't send the instance or class as a first argument
        2. It works like a regular function but inside a class
        3. The class also doesn't need to be instantiated to use this method,
        but you can also use it with an instance
        4. Mainly used when you want a method that does something related to the class
        but not to the instances of the class.
        """
        if isinstance(num, float):
            return True # allows numbers with .0 as integers.
        elif isinstance(num, int):
            return True
        return False

    @staticmethod
    def instantiate(instance):
        validate_price = Product.__validate_integer(instance.get('price'))
        if validate_price:
            phone = Product(
                instance.get("name"),
                instance.get("price"),
                instance.get("quantity"),
            )
            return phone
        else:
            return "Invalid price value, must be an integer"

    def show(self):
        return self

    def __repr__(self):
        """
        1. To alow printing the content of all without
        just printing the location in memory,
        you use the __repr__ magic attribute.
        2. self.__class__.__name__ helps to dynamically change
        the class name between Parent and Child classes
        """
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"
