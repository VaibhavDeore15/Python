"""Q.2)Employee Salary Calculator

Create an Employee class with attributes: name, salary, department.

Add a method to give a bonus (e.g., 10% of salary)"""

class emp:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
        
    def bonus(self):
        profit=(salary//100)*10
        return salary+profit
            
name=input("enter name of employee ")
salary=int(input("enter salary "))
department=input("Enter department ")
e=emp(name,salary,department)
print("After 10% profit the salary is ",e.bonus())