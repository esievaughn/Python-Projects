import time
A=12
B=18
C=22.1
print(A)
time.sleep(.5)
print(B)
time.sleep(.5)
print(A > B)
time.sleep(.5)
print(A < B)
time.sleep(.5)
biker= ['Joe', 'Chelsea']
if A < B:
        print(biker[1] + " bikes faster than " + biker[0])
elif A > B:
        print(biker[1] + " bikes slower than " + biker[0])
else:
        print(biker[1] + biker[0] + 'bike the same speed')

dictionary = {"Joe" : "12 mph", "Chelsea" : "18 mph"}
print("Now we add 'Nick' to the dictionary")
dictionary['Nick'] = '22.1 mph'
print(dictionary)        
for x in dictionary:
        print(x)

tuple= ("12", "18", "22.1")
for x in tuple:
        print(x)

print("Total mph adding together is")
def addition(C,D,E):
    add = C + D + E
    return add
print(addition(12,18,22.1))


        
