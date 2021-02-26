
#IF/ELIF/ELSE STATEMENTS w/CONDITONALS AND KEY
num1 = 12
key = False 

if num1 == 12:
    if key: 
        print("Num1 is equal to 12 and they have the key")
    else:
        print("Num1 is equal to 12 and they do no have the key")
elif num1 < 12:
    print("Num1 is less than 12")
else:
    print("Num1 is not equal to 12")
    

a = 25
key= True
b = 33
if b > a:
    if key: 
        print("b is greater than a and they have a key")
    else:
        print("b is greater than a, but they do not have the key")  
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


#BOOLEAN EXAMPLE
print(bool(False))
print(bool(10))


#ISISTANCE--if specified object is specified type
x = isinstance(5, int)
print(x)        #is 5 an integer? = true


