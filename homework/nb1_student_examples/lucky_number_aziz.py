favourite_color = input("What is your favourite color?")
lucky_number = int(input("What is your lucky number?"))

if favourite_color == "green" and 4 <= lucky_number <= 7:
    print("In", lucky_number, "years, you'll buy a", favourite_color, "bike")
elif favourite_color == "green" and 1 < lucky_number < 4:
    print("I suppose you wanted a", favourite_color, "ball", lucky_number, "years ago")
else:
    print(lucky_number, "is not so lucky!")