i = 1
while i < 6:
#   print(i)
  i += 1

# With the break statement we can stop the loop even if the while condition is true:
a = 1
while a < 6:
#   print(a)
  if a == 3:
    break
  a += 1

# With the continue statement we can stop the current iteration, and continue with the next:

b = 0
while b < 6:
  b += 1
  if b == 3:
    continue
#   print(b)

#  With the else statement we can run a block of code once when the condition no longer is true: 

c = 1
while c < 6:
  print(c)
  c += 1
else:
  print("c is no longer less than 6")