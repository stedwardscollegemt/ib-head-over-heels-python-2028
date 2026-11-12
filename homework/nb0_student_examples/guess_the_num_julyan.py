import random
 
# random number between 1 and 100
secret_number = random.randint(1, 100)
 
attempts = 0
running = True
 
print("guess a number between 1 and 100")
 
# while guess is wrong it keeps running
while running:
 
    guess = int(input("Enter your guess: "))
 
    attempts += 1
 
    # guess is correct
    if guess == secret_number:
        print("well done! You got it")
        print("good job, the number was", secret_number)
        print("you got it in", attempts, "attempts")
        running = False
 
    # guess too high
    elif guess > secret_number:
        print("guess is too high")
 
    # guess too low
    elif guess < secret_number:
        print("guess is too low")
 
print("thanks for playing")