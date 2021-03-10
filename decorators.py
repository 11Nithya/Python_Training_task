#Explain what are all the use case of Decorators, How control flows in decorator invoke, Code Examples of use cases
Def: A decorator is function which add extra functionality to the existing code without changing the existing code

Eg:  Time decorator
def _time(func):
    def wrapper(*args ,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end= time.time()
        return result
    return wrapper
@_time
def add(a,b):
    print(a+b)
output console
add(1,2)
3

explanation: when the function is called the execution starts from the the outer function(i.e _time function) and
then it enters the inner function when the inner function(i.e wrapper function) is called it executes the existing function that is add function
it note downs the start time ie at what time the function start executing and end time i.e at what time the function ends the
inner function(wrapper function )will be having the address of add function and when it is called it displays the output and
outer function(_time function) will be having the reference of inner function. The wrapper function contains arguments(* args and **kwargs )which means
we can give variable number  of position arguments and variable number of keyword arugements
