# def greet(name):
#     print(f"Hello {name} sir Good Morning")

# greet("Rahul")


# required and optional argument

# def name(first_name,middle_name="",last_name="kumar"):
#     print(f"First Name :{first_name}Middle name: {middle_name} Last name :{last_name}")

# name("rahul",last_name="singh",middle_name="kr")



# def name(first_name,middle_name="",last_name="kumar"):
#     print(f"First Name :{first_name} and last name is {middle_name} and {last_name}")

# name("rahul",middle_name="singh",last_name="don")

# -------------------------------------------------------------------
'''If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.'''

# Arbitrary Arguments are often shortened to *args in Python documentations.

'''
def add(*nums):
    sum=0;
    for i in nums:
     sum+=i
    print(sum)
add(1)
add(1,2)
add(1,2,3,4)
add(1,23,4,5,6)
'''
# ------------------------------------------------->
# The phrase Keyword Arguments are often shortened to **kwargs in Python documentations.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# def add(**nums):   
#     # sum=0;
#     # for i in nums:
#     #  sum+=i
#     print(sum(nums.values()))

# #keyword argument is must in **
# add(a=2)
# add(a=1,b=2)
# add(a=1,b=2,c=3,d=4)
# add(a=1,b=23,c=4,d=5,e=6)


# def test(var1,var2,*var3,var4=1,var5=2,**var6):
#     print(f'''
# var1:{var1}
# var2:{var2}
# var3:{var3}
# var4:{var4}
# var5:{var5}
# var6:{var6}
# ''')
# test(1,2,3,4,4,6,7,var4=3,a=10,b=88)

# giving hint to the ----------------------------->   user
# def add(num1:int,num2:int,num3:int)->int:
#     return num1+num2+num3
# ans=add(1,2,3)
# print(ans)





# making a normal variable to fun
# def greet():
#     """greet message funti"""
#     return "welcome "
# res=greet
# print(res())



# def greetmsg():
#    print("Hello")

# def test(arg):
#    arg()
# greetmsg()
# print(greetmsg)
# test(greetmsg)

# def outerfunction():
#     print("outer")
#     def inner():
#         print("Inner")
# print(outerfunction())


# glb=1000
# def test():
#     glb=100
#     def child():
#         global glb
#         print(glb)
#     child()
# test()



# decoraters -> which accept the fun and return same function

# def test():
#     print("hello")
# def test2(arg):
#     arg()
#     return arg
# test()
# res=test2(test)
# res()


# def greet():
#     return "hello"
# def makebold(fun):
#     def boldlogic():
#         return "<b>"+fun()+"<b/>"
# makebold(greet)



# lambda funtion---------------------->
# pow=lambda a,b:a**b
# print(pow(2,5))


