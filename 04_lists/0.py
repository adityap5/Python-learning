mylist = ["apple", "banana", "cherry"]
print(mylist)

# Lists allow duplicate values:

thislist =  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(thislist)) #Print the number of items in the list:

# List items can be of any data type
# A list can contain different data types

print(type(mylist))

# It is also possible to use the list() constructor when creating a new list.

thilist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thilist)

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.
print(thislist[2:5])

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
getlist = ["apple", "banana", "cherry"]
getlist.insert(2, "watermelon")
print(getlist)

# Append Items
# To add an item to the end of the list, use the append() method:
thislist.append("orange")
print(thislist)

# Extend List
# To append elements from another list to the current list, use the extend() method.
alist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
alist.extend(tropical)
print(alist)

# Remove Specified Item
# The remove() method removes the specified item.
blist = ["apple", "banana", "cherry"]
blist.remove("banana")
print(blist)

# The pop() method removes the specified index.
clist = ["apple", "banana", "cherry"]
clist.pop(1)
print(clist)

# The del keyword also removes the specified index:
del thislist[0]

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
thislist.clear()