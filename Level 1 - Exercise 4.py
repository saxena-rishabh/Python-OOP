'''
In the Athlete class given below, 
make all the attributes private and
add the necessary accessor and mutator methods
Represent Maria, the runner and make her run.
'''

class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
    
    def mutator(self, name, gender):
        self.__name=name
        self.__gender=gender
    
    def accessor(self):
        print("Name is {} and gender is {}".format(self.__name,
        self.__gender))

maria_obj = Athlete("Maria", "boy")
maria_obj.running()
maria_obj.accessor()
maria_obj.mutator("Maria", "girl")
maria_obj.running()
maria_obj.accessor()
