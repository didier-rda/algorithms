from tools import *

@time_it
def find_nemo(array):
    for element in array:
        if element == 'nemo':
            print('Found!')

concat = lambda x, y: x + y 

# set variables
array = ['nemo']
bigger_array = [concat(array[0],str(i)) for i in range(1000)]

# big O
'''
big O is the language to massure how
long a algoritm takes to run
'''
find_nemo(array) #5*10e-5
find_nemo(bigger_array) # 12.8*10e-5

'''
only the time doesent mean much, so 
let calculus tasks by fucntion with big O
big O:
#Operations(elemets) u.time

O(1) : Constant time
O(log) : log(n)
O(n) : linear time
O(n.logn) : log(n)
O(N^2)
O(2^n)
O(N!)
'''

# example
def func2(input): 
    a = 10 # O(1)
    a = 50 + 3 # O(1) 
    for i in len(input):
        func_inner() # O(n)
        b = True # O(n)
        a += 1 # O(n)
    return n # O(1)
# func2 Big O: O(3 + 4n)

'''
for rules to calculus big O:
    1 worst case
    2 remove constants
    3 different terms for inputs
    4 drop non dominants

worst case:
    big O calculus based on the worts case scenario

remove constants:
'''


