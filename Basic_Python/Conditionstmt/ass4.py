# WAP to accept basic salary from user and Give 10% of DA on basic salary ,12% HRA on basic salary  to employee if the salary is more than 50000 .calculate total salary.
salary = float(input("Enter salary: "))

da = 0
hra = 0

if salary > 50000:
    da = 0.10 *salary
    hra = 0.12 *salary

total_salary =salary + da + hra

print("Basic Salary:",salary)
print("DA (10%):", da)
print("HRA (12%):", hra)
print("Total Salary:", total_salary)
