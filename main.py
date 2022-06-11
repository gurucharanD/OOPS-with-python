import csv


class Item:
    pay_rate: float = 0.8
    all = []

    # attribute shared across all the instances is called class attributes
    # pay_rate is an example of class attribute
    # all is an example of another class attribute

    # python first looks if an attribute is available in the instance level
    # if the attribute is not found then it goes to class level and tries to
    # find it in the class attributes

    # read only attributes can be created to avoid attributes
    # from being over-ridden after instantiation this
    # can be done using a property decorator

    def __init__(self, name: str, price: float, quantity=0):

        # to avoid price and quantity from receiving a negative value
        # we use assertions at the top to validate received arguments
        # allows us to catch errors or bugs as soon as possible

        assert price >= 0, f"price {price} is less than 0"
        assert quantity >= 0, f"Quantity {quantity} is less than 0"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        # create a list of all objects
        Item.all.append(self)

    # read only
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # __repr__ can be used to represent the object in
    # a readable format
    def __repr__(self):
        return f" {self.__class__.__name__}( '{self.name}' ,'{self.quantity}, '{self.price} ')"

    # class method is a method which can be invoked without creating an object
    # it could be accessed with the class name
    # decorators allow us to add additional behaviour to the method
    # class object is passed as the first argument for class methods
    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
        # pass

    # static method is used when
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @property
    def read_only_name(self):
        return "read only"


# inheritance
class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name=name,
            price=price,
            quantity=quantity
        )

        assert broken_phones >= 0, f"broken_phones {broken_phones} is less than 0"
        self.broken_phones = broken_phones
