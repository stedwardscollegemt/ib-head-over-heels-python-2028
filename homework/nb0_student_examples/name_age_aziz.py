# Programming exercises from the book (p. 304)
def new_age(age):
    return (age + 10)

name = input("Enter your name below")
age = int(input("Enter your current age below"))

new_age = new_age(age)

print(name, "in 10 years you'll be", new_age)