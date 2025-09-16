"""Q.1) You have a list of employee records, and you need to create a new list
that contains the names of employees who work in the 'Sales' department, all in uppercase.
Hint:Create Dictionary with name ,department and salary field"""

emp_info=[{"name":"Vaibhav","Department":"Sales","Salary":122200},
          {"name":"shrey","Department":"Production","Salary":846546},
          {"name":"hemraj","Department":"Sales","Salary":554554},
          {"name":"tejas","Department":"engineering","Salary":122200},
          {"name":"sahil","Department":"Sales","Salary":96465}
          ]
        

for emp in emp_info:
    if emp["Department"]=="Sales":
        emp["name"]=emp["name"].upper()
        
for emp in emp_info:
    print(emp)