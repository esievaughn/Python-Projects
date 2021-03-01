
class Employee:                 #Create new class--Employee
    firstName = 'Charlie'
    lastName =  'Brown'
    age =   46
    email = 'c.brown@gmail.com'
    def __init__(self, firstName, lastName, age, email)  #initialization--attach arguments
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email

class Salary(Employee):         #Create child class 'Salary' from parent class 'Employee'
    income = 50,000.00
    hourly = False
    salary = True
    def __init__(self, income, hourly, salary) #initialization--attach arguments
        self.income = income
        self.hourly = hourly
        self.salary = salary

class Department(Employee):     #Create another child class 'Department' from parent class 'Employee'
    deptName = 'Peanuts'
    manager = 'Peppermint Patty'
    def __init__(self, deptName, manager) #initialization--attach arguments
        self.deptName = deptName
        self.manager = Manager
    
            
            
