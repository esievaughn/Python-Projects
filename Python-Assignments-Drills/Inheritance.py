
class Employee:                 #Create new class--Employee
    firstName = ''
    lastName =  ''
    age =   0
    email = ''
    def __init__(self, firstName, lastName, age, email):  #initialization--attach arguments
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email

CB = Employee('Charlie', 'Brown', 46, 'cbrown@gmail.com')
print("What is your first name? {}".format(CB.firstName))

print("\nEMPLOYEE PROFILE: \nFirst Name: {}\nLastName: {}\nAge: {}\nEmail: {}".format(CB.firstName, CB.lastName, CB.age, CB.email))



class Salary(Employee):         #Create child class 'Salary' from parent class 'Employee'
    firstName = "Charlie"
    lastName =  "Brown"
    age =   46
    income = 50000
    hourly = False
    salary1 = True
    def __init__(self, firstName, lastName, age, email, income, hourly, salary): #initialization--attach arguments
        super().__init__(firstName, lastName, age, email)
        self.income = income
        self.hourly = hourly
        self.salary = salary

    def salarymsg():
        if (Salary.income > 35000):
            print("\nYou're a good man, Charlie Brown!")
        else:
            print("\nSorry, Charlie.")
 

class Department(Employee):     #Create another child class 'Department' from parent class 'Employee'
    firstName = 'Charlie'
    lastName =  'Brown'
    age =   46
    deptName = 'Peanuts'
    manager = 'Charles Shulz'
    def __init__(self, deptName, manager): #initialization--attach arguments
        super().__init__(self, firstName, lastName, age, email)
        self.deptName = deptName
        self.manager = manager



print("\nINCOME & DEPARTMENT: \nIncome: {} \nDepartment: {}\nManager: {}".format(
        Salary.income, Department.deptName, Department.manager))


if __name__ == "__main__":
	print(Salary.salarymsg())
