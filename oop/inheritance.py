from main import Product


class Iphone(Product):
    # # class attributes
    # pay_rate = 0.8

    # # to save instances
    all = []
    
    def __init__(self, name: str, price: float, quantity: int=0, broken_phones: int=0):
        """
        Using inheritance barely. However, this could be an issue
        when creating inheritance with many child class.
        Also, the
        """
        # assert the types of your instance attributes
        assert type(name) == str, "Name must be a string"
        if type(price) != float and type(price) != int:
            raise ValueError("Price must be a float or integer")
        assert type(quantity) == int, "Quantity must be an integer"
        assert type(broken_phones) == int, "Number of broken Phones must be an integer"

        # assert the values of your instance attributes
        assert price >= 0, "Price must be greater than or equal to 0"
        assert quantity >= 0, "Quantity must be greater than or equal to 0"
        assert broken_phones >= 0, "Broken phones must be greater than or equal to 0"

        # instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        Iphone.all.append(self)

iphone_8 = Iphone('Iphone 8', 650, 25, 3)
print(iphone_8.broken_phones)
print(Iphone.all)


class Samsung(Product):
    # class attributes
    pay_rate = 0.8

    # to save instances
    all = []
    
    def __init__(self, name: str, price: float, quantity: int=0, broken_phones: int=0):
        """
        Using inheritance with super function.
        This way, you only create new attributes for this specific child class
        after adding the previous ones to super constructor.
        """
        super().__init__(name, price, quantity)
        # assert the types of your instance attributes
        assert type(broken_phones) == int, "Number of broken Phones must be an integer"

        # assert the values of your instance attributes
        assert broken_phones >= 0, "Broken phones must be greater than or equal to 0"

        # instance attributes
        self.broken_phones = broken_phones

        """
        You can also make use of the class attributes like `all` in the parent class
        by deleting the one in child class,
        or make it specific to the child class by having its own
        """
        Samsung.all.append(self)

galaxy_s20 = Samsung('Galaxy S20', 650, 25, 8)
print(galaxy_s20.broken_phones)
print(Samsung.all)
