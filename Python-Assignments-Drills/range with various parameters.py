import time
my_list = ['one', 'two', 'three', 'four', 'five']
my_list_len = len(my_list)
for i in range (0, my_list_len):
    print(my_list[i])
    time.sleep(.5)

my_list = ['1', '2', '3', '4', '5']
my_list_len = len(my_list)
for i in range (4):
    print(i, end=' , ')
time.sleep(.5)

my_list = ['1', '2', '3', '4', '5']
my_list_len = len(my_list)
for i in reversed (range(0, 4, 1)):
    print(i, end=' , ')
time.sleep(.5)

my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '10']
my_list_len = len(my_list)
for i in reversed (range(2, 10, 2)):
    print(i, end=' , ')
time.sleep(.5)
