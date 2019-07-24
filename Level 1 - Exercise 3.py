'''
Exercise 3:
Write a Python program to implement the class chosen with its attributes. Also,
represent Jack and Jill as objects of the class chosen
initialize their attributes and
display their details
Create a parameterless constructor in which create the attributes with None
Note: Verification is done only for class structure
'''

class Employee:
    def __init__(self):
        self.ismarried = None

jack = Employee()
jack.name = 'jack'
jack.ismarried = 'Yes'
print("name: {} and married: {}".format(jack.ismarried, jack.name))
jill = Employee()
jill.name = 'jill'
print("name: {} and married: {}".format(jill.ismarried, jill.name))
