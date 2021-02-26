
#Function Challenge
def myFunction(country= "Norway"):
    print("I am from " + country)

myFunction("Norway")
myFunction("India")
myFunction("Brazil")
myFunction() #returns Norway

#Array Challenge (cycle through array using loop; use count() & sort() methods

fruit = ['orange','kiwi','grapefruit','orange']
for i in fruit:
    print(i)
    
#count() returns the number of times a value appears in the array
a= fruit.count('orange')
print(a)

#sort() returns list ascending by default or can set criteria
fruit.sort()
print(fruit)


#Lambda function, small anonymous function that can take any number of arguments
x= lambda a: a + 10
print (x(10))

y= lambda a,b: a * b
print(y(5,6))

z= lambda a,b,c: a + b + c
print(z(6,5,2))

def myfunc(n):
    return lambda a: a * n
mydoubler= myfunc(2)        #doubles the number sent in 
print(mydoubler(11))

def myFunc(n):
    return lambda a: a * n
mydoubler=myFunc(2)
mytripler=myFunc(3)

print(mydoubler(11))
print(mytripler(11))


#Placeholder {} 
loc1= "Portland"
loc2= "Maui"
print("I flew from {} to {}".format(loc1,loc2))
