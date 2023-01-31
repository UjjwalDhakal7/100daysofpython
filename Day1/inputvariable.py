# here we look at the input function and variables in python.

#input function :

#input("What is your name?")

#print("Hello, my name is ujjwal " + input("your surname"))

# program to calculate the number of letters in users name.

print("Enter your name.")
n = input("Name :")                          #assign value to variable
i = int(input("enter contact :"))            #asign a integer value
print(n)     #prints name entered
print(len(n))

"""naming variable rules :
- define readable names
- has to be one unit, separate with '_'
- if include numbers it shouldn't be at the start
- if var_name is different you'll get nameerror
"""
