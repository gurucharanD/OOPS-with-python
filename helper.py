#  when to use class method and when to use static method

# static method:
#     when we want to do something that is not unique per instance.
#     some method that can also be used as a standalone function
#
# class method:
#     these are created to manipulate or instantiate objects
#
# static methods do not pass the self parameter as the first argument

# both could be called both from the instance level and class level
# should always be called form class level

from main import Item
from main import Phone

item1 = Phone('laptop', 100, 2, 1)
print(item1.calculate_total_price())

item2 = Phone('laptop1', 100, 2)
item3 = Phone('laptop2', 100, 2)

print(item1.pay_rate)
print(Item.pay_rate)
# item2 = Item('laptop', 100, -1)

# __dict__ gives the attributes that are present on the object
# when applied on an object gives all attributes of the object
print(item1.__dict__)
print(Item.__dict__)
# when applied on class gives all the class attributes

# if you want to have a different value for the class attribute
# on a particular object, you can assign it directly on the instance
item1.pay_rate = 0.75

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(100.76))
print(Item.is_integer(100.00))

print(item1.read_only_name)
item1.name = "guru"
print(item1.name)
print(item1.price)

# encapsulation : mechanism of restricting the direct access to objects
# any modifications are done only through class attributes
# example : name attribute in item class, you need to use getters and setters

# abstraction: hides unnecessary information from instances
# that is done by making the methods or attributes private
# and using appropriate access modifiers

# inheritance: using child and parent classes

# polymorphism: many forms, the idea is ability to have different scenarios when
# we call the exact same entity, i.e. the function we define
# example: len built-in function, that takes different types of parameters





