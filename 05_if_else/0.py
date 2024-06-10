a = 33
b = 200
if b > a:
  print("b is greater than a")

#   Elif === elseif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#   Short Hand If
if a > b: print("a is greater than b")
# or
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")