"""this is a module which contain various function
like add(),div(),pro(),sub()"""#(doc string)


allmethodenames=["add","sub","pro","div"]
def add(num1:int,num2:int):
    """return a number which will be the sum of two number"""#(Block level comment)
    return num1+num2 #this statement return sum of number to calling envirment #(inline comment)


def sub(num1:int,num2:int):
    """return a number which will be the subtraction of two number"""
    return num1-num2

def pro(num1:int,num2:int):
    """return a number which will be the product of two number"""
    return num1*num2

def div(num1:int,num2:int):
    """return a number which will be the div of two number"""
    return num1/num2
