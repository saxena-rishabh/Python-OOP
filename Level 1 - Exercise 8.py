'''
The jugglers hired in the circus are “Jack Bremlov” and “Anthony Gatto”. Jack juggles with knives and Anthony juggles with balls.15 min
Extend the program given below to represent the jugglers, Jack and Anthony and the juggling items, balls and knives. Once done modify the juggles() method of Juggler class to accept the juggling item ( with parameter name jugglingitem ) and display the following message:
"(name of the juggler) is juggling with (name of the juggling item)".
Invoke the juggles() method for each juggler and make them juggle.
Note: Verification is done only for class structure.
'''

class Juggler:
    def __init__(self,name):
        self.__name=name

    def juggles(self,jugglingitem):
        #write the code to make the juggler juggle
        print(self.__name + ' is juggling with ' + jugglingitem.get_name())

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

JK = JugglingItem("knives")
AB = JugglingItem("balls")
Jack = Juggler("Jack Bremlov")
Anthony = Juggler("Anthony Gatto")
Jack.juggles(JK)
Anthony.juggles(AB)
