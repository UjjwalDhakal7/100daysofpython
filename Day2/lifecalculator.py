# Program to calculate remaining life if total life is 100.

age = int(input("Enter your age :"))
age_in_weeks = int(age*52)
age_in_days = int(age*365)

rem_age_years = 100 - age
rem_age_weeks = (rem_age_years*52 - age_in_weeks)
rem_age_days = (rem_age_years*365 - age_in_days)

print(f"Your remaining age is {rem_age_years} years, {rem_age_weeks} weeks, {rem_age_days} days ")