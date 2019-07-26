'''
Write a Python program to implement the class chosen with its attributes and methods based on the requirements given below:
identify_distance_that_can_be_travelled(): Return the distance that can be travelled by the vehicle without using the reserve fuel. If the fuel left is less than or equal to reserve fuel, the method should return 0.


identify_distance_travelled(initial_fuel): Return the distance so far travelled by the vehicle based on the initial fuel,fuel left and mileage.
Assume that initial fuel is always greater than fuel left.


Represent a vehicle and test your program by initializing the instance variables and invoking the appropriate methods.
'''

class Vehicle:
    def __init__(self):
        self.reserve_fuel = 5
        self.mileage = None
        self.fuel_left = None
    
    def identify_distance_that_can_be_travelled(self,fuel_left,mileage):
        self.mileage = mileage
        self.fuel_left = fuel_left
        remaining_fuel = self.fuel_left - self.reserve_fuel
        distance = remaining_fuel * self.mileage
        return(distance)
    
    def identify_distance_travelled(self,initial_fuel,fuel_left,mileage):
        self.mileage = mileage
        self.fuel_left = fuel_left
        fuel_consumed = initial_fuel - self.fuel_left
        distance = fuel_consumed * self.mileage
        return(distance)
    

v1 = Vehicle()
Distance_can_be_travelled = v1.identify_distance_that_can_be_travelled(50,10)
Distance_travelled = v1.identify_distance_travelled(100,10,50) 
print("Distance that can be travelled is {}".format(Distance_can_be_travelled))
print("Distance travelled is {}".format(Distance_travelled))

        
                                                    
