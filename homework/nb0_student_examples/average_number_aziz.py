# Programming exercises from the book (p. 304)
def average_number(no1, no2, no3):
    return (no1 + no2 + no3) / 3

no1 = int(input("Enter first number"))
no2 =  int(input("Enter second number"))
no3 = int(input("Enter third number"))

average = (average_number(no1, no2, no3))

print("Your average is:", average)