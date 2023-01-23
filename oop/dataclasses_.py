"""Adding dataclass decorator to your class helps to reduce the code
to write.
1. It removes the need to manually create a __init__ constructor.
2. It removes the need to manually create a __str__ magic method. With it.
3. You don't need to update __init__ and __str__ methods every time you add a new attribute.
4. With this, you can easily create instance attributes for your classes. Make sure to decorate the class with @dataclass to avoid creating class attributes instead of instance attributes.
5. Using the field function, you can add default values to attributes. with init=False, you encapsulate the attributes from being set on instantiating
6. To encapsulate all attributes so they can't be changed once instantiated, you add frozen=True to the decorator.
"""


from dataclasses import dataclass, field
from uuid import uuid4


def generate_id()-> str:
    return uuid4().hex

@dataclass(frozen=True)
class Person():
    name: str
    gender: str
    id: str = field(init=False, default_factory=generate_id)

def main() -> None:
    person = Person("Fhuad", "male")
    # person.name = "Faridah"
    print(person)

if __name__ == "__main__":
    main()
