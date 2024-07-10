import random

top_of_range = input("Type a numbe: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type a number larger than zero next time')
        quit()
else:
    print('Please type a number larger than zero next time')


random_number = (random.randrange( top_of_range))
guesses = 0

while True:
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print('You got it')
        break
    else:
        print("You got it wrong")
        if user_guess > random_number:
            print('your guess is higher than the number')
        else:
            print('your guess is lower than the number')
        
print("It took you" ,guesses, "guesses to complete the game!")