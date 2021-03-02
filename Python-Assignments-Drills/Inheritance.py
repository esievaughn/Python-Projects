
class Employee:                 #Create new class--Employee
    firstName = ''
    lastName =  ''
    age =   0
    email = ''
    employID = 0
    def __init__(self, firstName, lastName, age, email, employID):  #initialization--attach arguments
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email
        self.employID = employID

        def employeeLogin(self):                         #polymorphism assignment -- will add to department child class
            firstName= input("Please enter your first name: ")
            lastName= input("Please enter your last name: ")
            email= input("Please enter your email: ")
            employID = input("Please provde your employee ID: ")
        if(self.firstName and self.lastName and self.email and self.employID):
            print("\nThank You, {}!".format(self.firstName))
        else:
            print("\nInformation is incorrect, please try again.")
        
CB = Employee('Charlie', 'Brown', 46, 'cbrown@gmail.com', 5512)     
print("\nWhat is your first name? {}".format(CB.firstName))
print("\nEMPLOYEE PROFILE: \nFirst Name: {}\nLastName: {}\nAge: {}\nEmail: {}\nID: {}".format(CB.firstName, CB.lastName, CB.age, CB.email, CB.employID))

class Salary(Employee):         #Create child class 'Salary' from parent class 'Employee'
    firstName = "Charlie"
    lastName =  "Brown"
    age =   46
    income = 50000
    hourly = False
    salary1 = True
    def __init__(self, firstName, lastName, age, email, income, hourly, salary): #initialization--attach arguments
        super().__init__(firstName, lastName, age, email, employID)
        self.income = income
        self.hourly = hourly
        self.salary = salary

    def salarymsg():
        if (Salary.income > 35000):
            print("\nYou're a good man, Charlie Brown!")
        else:
            print("\nSorry, Charlie.")

#polymorphism assignment -- adding income amount and type to parent employee information
print("\nINCOME PROFILE: \nFirst Name: {}\nLastName: {}\nEmail: {}\nIncome: {}\nSalary: {}".format(CB.firstName, CB.lastName, CB.email, Salary.income, Salary.salary1))
 

class Department(Employee):     #Create another child class 'Department' from parent class 'Employee'
    deptName = 'Peanuts'
    manager = 'Charles Shulz'
    deptID = 6743
    def __init__(self, deptName, manager, deptID): #initialization--attach arguments
        super().__init__(firstName, lastName, age, email, employID)
        self.deptName = deptName
        self.manager = manager
        self.deptID = deptID

        def employeeLogin(self):                         #polymorphism assignment -- will add to department child class, changed from employeeID to Maanager ID
            firstName= input("Please enter your first name: ")
            lastName= input("Please enter your last name: ")
            email= input("Please enter your email: ")
            deptID = input("Please provde your employee ID: ")
        if(self.firstName and self.lastName and self.email and self.deptID):
            print("\nThank You, {}!".format(self.firstName))
        else:
            print("\nInformation is incorrect, please try again.")

CB = Employee('Charlie', 'Brown', 46, 'cbrown@gmail.com', 5512)


print("\nINCOME & DEPARTMENT: \nIncome: {} \nDepartment: {}\nManager: {}\nDeptID: {}".format(
        Salary.income, Department.deptName, Department.manager, Department.deptID))



if __name__ == "__main__":
	print(Salary.salarymsg())


