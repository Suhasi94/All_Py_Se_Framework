import time

########### func decorator
"""
def param_(n):
    def outer(func):
        def wrapper(*args,**kwargs):
            print(f"name of the main function is {func.__name__}")
            time.sleep(n)

            
            res = func(*args,**kwargs)
            return abs(res)
        return wrapper
    return outer

#@outer # add = outer(add)
@param_(2)
def add(a,b):
    return a+b
print(add(2,3))

#@outer
@param_(1)
def sub(a,b):
    return a-b
print(sub(4,6))
"""

##########

class Demo:

    def __init__(self,n):
        self.n = n

    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print(f"name of the main function is {func.__name__}")
            time.sleep(self.n)
            func(*args,**kwargs)
        return wrapper
#d = Demo(2)
@Demo(2)  #@d
def add(a,b):
    print(a+b)
add(2,3)

