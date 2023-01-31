# This is a program to create the wedding hashtag by taking names from users.

print("Welcome to the program which suggest you couple hashtags.")
bride = input("Enter bride name :")
groom = input("Enter groom name :")

a = int(len(bride)/2)
b = int(len(groom)/2)

for i in range(0,a):
   print(bride[i],end = "")
for i in range(0,b):
   print(groom[i],end = "")

