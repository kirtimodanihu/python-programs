class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDeatils(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

class Employee(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT",75000)

engg1=Employee("Elon Musk",40,)
engg1.showDeatils()
