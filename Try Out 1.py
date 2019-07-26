'''
Problem Statement: 30 min

We have a list of customer objects. Complete the code so that we have a dictionary of customer objects based on location.
'''

class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

list_of_customers = [Customer(101, 'Mark', 'US'),
Customer(102, 'Jane', 'Japan'),
Customer(103, 'Kumar', 'India')]

dict_of_customer={"US":list_of_customers[0],
                "Japan":list_of_customers[1],
                "India": list_of_customers[2]}
for key,value in dict_of_customer.items():
        print(key, '-->' , value.cust_id,value.cust_name, value.location)
                                                
