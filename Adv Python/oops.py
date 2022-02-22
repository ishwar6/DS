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


class Salary:
    def __init__(self, basicPay, flexiPay, bonus, PPF):
        self.basicPay = basicPay
        self.flexiPay = flexiPay
        self.bonus = bonus
        self.PPF = PPF

    def get_ctc(self):
        return ((self.basicPay+self.flexiPay)*12+self.bonus+self.PPF)


class Employee:
    def __init__(self, name, empId, salaryObj):  # The salary object is passed
        self.name = name
        self.id = empId
        self.salObj = salaryObj  # The salary object is instantiated

    def annualCTC(self):
        # Calling the get_ctc function of salary class
        return "Total salary for " + str(self.name) + " with Employee ID " + str(self.id) + " is: " + str(self.salObj.get_ctc())


obj_sal1 = Salary(600, 1000, 10000, 3000)
obj_emp1 = Employee("Employee 1", "270991", obj_sal1)
print(obj_emp1.annualCTC())
obj_sal2 = Salary(600, 1000, 0, 3000)
obj_emp2 = Employee("Employee 2", "270919", obj_sal2)
print(obj_emp2.annualCTC())
