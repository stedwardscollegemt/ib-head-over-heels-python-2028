# Programming exercises from the book (p. 304)
number = int(input("Enter any three-digit number"))

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

print(hundreds + tens + ones)