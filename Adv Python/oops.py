class Phone:
    def __init__(self, name, price, quantity=0):
        print(f"New phone created with name: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        # self in argument in this method shows that object itself is passed as argument while calling this method.
        # If self is not written in args and method is called then:
        # TypeError: calculate_total_price() takes 0 positional arguments but 1 was given
        return self.price*self.quantity


p1 = Phone("MI", 1000, 10)
p2 = Phone("Apple", 3000, 20)

print(p1.name)
# MI
print(p1.calculate_total_price)
# if not called: <bound method Phone.calculate_total_price of <__main__.Phone object at 0x7fcac7333df0>>
# A bound method is the one which is dependent on the instance of the class as the first argument.
# all functions in a class are by default bound functions.
# The instance obj is automatically passed as the first argument  to the function called
# and hence the first parameter of the function will be used to access the variables/functions of the object.
