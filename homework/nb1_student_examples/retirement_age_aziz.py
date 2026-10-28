name = input("Enter your name below.")
age = int(input("Enter your age below."))
gender = input("Male or Female (M/F)")

if gender == "M":
    gender = True
elif gender == "F":
    gender = False

if age >= 65 and gender == True:
    print(name, "you are eligible for retirement and pension")
elif age < 65 and gender == True:
    print(name, "you have:", 65 - age, "years left till eligible for pension")

if age >= 62 and gender == False:
    print(name, "you are eligible for retirement and pension")
elif age < 62 and gender == False:
    print(name, "you have:", 62 - age, "years left till eligible for pension")