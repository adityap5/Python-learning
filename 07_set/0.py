thisset = {"apple", "banana", "cherry"}
print(thisset)

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# functions work on set  :
len()
type()
set() #constructor
add() #To add one item to a set
update() #To add items from another set into the current set
remove(), #or 
discard() #To remove an item in a set
pop() #To remove a random item 
clear() #To remove all items from a set
del set #delete the completely existing set

#JOIN SETS
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.