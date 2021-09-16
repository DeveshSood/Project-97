number = 9
chance = 5
while chance > 0:
    guess = int(input("Guess A Number Between 1 And 9 :- "))
    if guess == number:
        break
    elif guess > number:
        print("Sorry!! the number is less than you Guess")
        chance = chance - 1
    elif guess < number:
        print("Sorry!! the number is greater than you Guess")
        chance = chance - 1
if chance == 0:
    print("Sorry!! You lost, the number was - ", number)
if chance > 0:
    print("WOW!! You got it rigt, the number was - ", number)