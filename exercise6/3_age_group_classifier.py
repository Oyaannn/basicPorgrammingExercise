def age_group(age):
    if age >= 0 and age <=12 :
        return "Child"
    elif age >= 13 and age <=19 :
        return "Teenager"
    else :
        return "Adult"

age = int(input("Enter your age :"))
gruop = age_group(age)
print("your age is:", gruop )