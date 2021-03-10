#Different arguments types explanations with code example

1.Default arguments: In the functions the arguments which assumes default values if a value is not supplied as an argument while calling the function. An assignment operator “=” is used to give a default value to an argument
Eg: def sum(a=4,b=2):  # 2 is supplied as default argument “”“ this function will print sum of two numbers if the arguments are not supplied it will add the default value”””
	Print(a+b)
sum() # no arguments are provided so it will take default arguments 
sum(1,2)# arguments are provided it will take 1 and 2 and sum it


2.Keyword arguments:  In this argument we can use the name of the parameter irrespective of its position while calling the function to supply the value all the keyword arguments must match one of the arguments by the function
Eg:   def add(a,b=5,c=10):
		return(a+b+c)
        # calling the function add by giving keyword arguments
                   All parameters are given as keyword arguments so need to maintain the same order.
                      print( add(b=10,c=15,a=20))
                  #output:45

                      
3.Positional arguments: During function call values passed through arguments should be in the order of parameters in the function definition 
Keyword arguments should follow positional arguments only
Eg: def add(a,b,c):
	return (a+b+c)

       
# calling the function add
   print(add(10,20,30)
all arguments are positional arguments values passed to parameters by their position. 10 is assigned to a, 20 is assigned to b and 30 is assigned to c


4.Arbitrary positional arguments: asterisk(*) is placed before parameter in function definition which can hold variable number of arguments these arguments wiil be wrapped in a tuple.
Eg: def name(*a):
	  return a
   print(name(1,2,3,))

5.Arbitrary keyword arguments: double astrerisk(**) is placed before a parameter in a function which can hold keyword variable -length arguments.
         Eg: def greet(**a):
		for i in a.items():
			print(i)
            greet(number=5, colour =”blue”,fruits=”apple”)
     output:
(“number”, “5”)
(“colour”, ” blue”)
       (“fruits”,”apple”)
