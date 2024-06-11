# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for a in "banana": #looping through a String
  print(a)

# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for b in fruits:
  print(b)
  if b == "banana":
    break
  
# With the continue statement we can stop the current iteration of the loop, and continue with the next:


fruits = ["apple", "banana", "cherry"]
for c in fruits:
  if c == "banana":
    continue
  print(c)

# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.  

for d in range(6):
  print(d)

for e in range(2, 6):
  print(e)  

for f in range(3, 30, 3): #Increment the sequence with 3 (default is 1):
  print(f)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:  

for g in range(6):
  print(g)
else:
  print("Finally finished!")