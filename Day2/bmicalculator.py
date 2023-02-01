# program to calculate BMI of a person using user data.

weight = int(input("Enter your weight in Kgs:"))
height = float(input("Enter your Height in metre:"))

BMI = int(weight/height)
print("Your BMI index is " + str(BMI))

""" In above step converting to str cuz diff datatypes cant concatenate.
    So we can use f" to solve this problem. It can accomodate all datatypes.
"""
score = 168
time = 5.0
player = "Adam"
print(f"{player}'s score is {score} in {time}")