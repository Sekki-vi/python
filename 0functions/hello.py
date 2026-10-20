# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello,", name)

# official documentation for the print function
# print(*objects, seq=' ', end='\n', file=sys.stdout, flush=False)
# *objects = can take any n umber of objects
# sep=' ' =  seperator, a blank space between objects
# end='\n' = ends with a new line everytime

# we can override the value of end and make it not print new line
print("hello, ", end="")
print(name)

# change it to something random
print("hello, ", end="???")
print(name)

# print takes in positional parameters. seq and end are named parameters

# Say hello to user
# to use quotes in a print statement, you can take advantage of both qoutes doing the same thing
print('hello, "friend"')

# can also use backslash
print("hello, \"friend\"")

# f string to use variables inline
print(f"hello, {name}")

# Lets say someone enters a bad name
badname = "     sekki  "
# a built in string function can be used to strip whitespace
badname = badname.strip()
# Capitalize the first character
badname = badname.capitalize()
# Capitalizes the first letter of each word
badname2 = "sekki vi".title()
print(badname)

print(badname2)