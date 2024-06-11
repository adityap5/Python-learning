# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")

my_function()

def myfunction(fname):  #with arguments and parameters
  print(fname + " rose")

myfunction("Emili")
myfunction("Tobi")
myfunction("Linusa")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def myfunc(*kids):
  print("The youngest child is " + kids[2])

myfunc("Emil", "Tobias", "Linus")


def my_function(country = "Norway"): #default parameter value
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")