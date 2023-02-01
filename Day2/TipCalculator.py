# program to generate how much tip to pay.

print("Welcome to the Tip_Calculator")
amt = float(input("Total bill : "))
print(f"Your total amount to pay is Rs {amt}")

print("how much tip would you like to give? 10%, 12%, 15%")
tip = int(input(""))
if tip == 10:
    amt_with_tip = amt + amt * 0.1
elif tip == 12:
    amt_with_tip = amt + amt * 0.12
else:
    amt_with_tip = amt + amt * 0.15

print(f"Your total amount to pay with tip is Rs {amt_with_tip}")
members = round(int(input("How many person to split the bill among?")))
Per_person_pay = amt_with_tip/members
print(f"each person should pay {Per_person_pay}")
