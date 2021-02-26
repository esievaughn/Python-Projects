
#Format() Method

fName= "Skylar"
lName= "Woods"

print("Hello {} {}, welcome to Python!".format(fName,lName)) #declare variables within format method

txt1= "My name is {fName}, I'm {age}".format(fName="Skylar", age="30")
print(txt1)

x= format(8, 'b') #8 is formated into binary=1000
print(x)

print("binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}".format(4))

y= format(0.5, '%') #format 0.5 into a percentage
print(y)

z= format(255, 'x') #format 255 into hexadecimal; x for hexadecimal
print(z)

#getSum() function

def getSum(n1,n2,n3):
    answer= n1 + n2 * n3
    print("The answer is {}.".format(answer))

getSum(2,4,6)

myAdd=getSum
myAdd(2,4,3)


