# A function in Python is a block of code that can be reused. It is defined using the def keyword, followed by the function's name and a pair of parentheses. The function's body is then indented and contains the code that will be executed when the function is called.


# types of function:- There are two types of function in pyhton 
# 1) Predefined/Built-in library function
'''-> Python Built-in Functions:
The Python interpreter has a number of functions that are always available for use. These functions are called built-in functions. For example, print() function prints the given object to the standard output device (screen) or to the text stream file.'''

# In Python 3.6, there are 68 built-in functions. But for the sake of simplicity let us consider the majorly used functions and we can build on from there.


# 2) user defined function:-In this type of funtion we create a funtion according to the user
 
#  types of userdefined function

# 1> ----------------funtion without parameters without return value-------------------
'''def greeting(): #creating a function 
    print("Good morning")
greeting()#calling a function
'''


# 2> function with parameters without return value
'''def add(a,b):
    print("Sum of both Number is:",a+b)

a=int(input("Enter your first Number: "))
b=int(input("Enter your second Number: "))
add(a,b) '''



# 3> function without parameters with return value
'''
def sum():
    n=int(input("Enter your Number:"))
    p=int(input("Enter your Number:"))
    return n+p

addition=sum()   # storing the return value in addition
print(addition)
# print(sum())    # printing the return value directly
'''



# 4> function with parameters with return value
# def power(n):
#     return n*n

# n=2
# res=power(n)
# print(res)



