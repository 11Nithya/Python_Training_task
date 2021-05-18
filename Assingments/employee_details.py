class Employee:
    Company = "Sony"
    def __init__(self, name, designation, Status, ID):
        self.name = name
        self.designation = designation
        self.Status  = Status
        self.ID=ID
    
class Management(Employee):
    def add_employee(self):
        data=int(input("enter the number of employee "))
        for 











ob= Employee("abc","consultant","L1", 700002610)
ob1= Employee("xyz","consultant","L2", 700002612)
ob2= Employee("cdf","consultant","L3", 700002613)




print(ob.name,ob.designation,ob.Status,ob.ID)
