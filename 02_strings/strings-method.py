txt = "I love apples, apple are my favorite fruit"


# casefold()	Converts string into lower case
print(txt.casefold())

# capitalize() : Converts the first character to upper case
print(txt.capitalize())


#center() : Returns a centered string
k = "banana"
y = k.center(20)
print(y)


#count() : Returns the number of times a specified value occurs in a string
x = txt.count("apple")
print(x)

# find() : Searches the string for a specified value and returns the position of where it was found
e = txt.find("apple")
print(e)

# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case

# join() : Converts the elements of an iterable into a string
myTuple = ("John", "Peter", "Vicky")
r = "#".join(myTuple)
print(r)