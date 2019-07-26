'''
Write a Python program to implement the class chosen with its attributes and methods based on the requirements given below:
identify_distance_that_can_be_travelled(): Return the distance that can be travelled by the vehicle without using the reserve fuel. If the fuel left is less than or equal to reserve fuel, the method should return 0.


identify_distance_travelled(initial_fuel): Return the distance so far travelled by the vehicle based on the initial fuel,fuel left and mileage.
Assume that initial fuel is always greater than fuel left.


Represent a vehicle and test your program by initializing the instance variables and invoking the appropriate methods.
'''

class Vehicle:
    def __init__(self, mileage, fuel):
        self.reserve_fuel = 5
        self.mileage = mileage
        self.fuel = fuel
    
    def identify_distance_that_can_be_travelled(self):
        remaining_fuel = self.fuel - self.reserve_fuel
        distance = remaining_fuel * self.mileage
        return(distance)
    
    def identify_distance_travelled(self, initial_fuel):
        fuel_consumed = initial_fuel - self.fuel
        distance = fuel_consumed * self.mileage
        return(distance)
    

v1 = Vehicle(50,10)
print("Distance that can be travelled is {}".format(v1.identify_distance_that_can_be_travelled() ))
print("Distance travelled is {}".format(v1.identify_distance_travelled(100)))

        
                                                    
