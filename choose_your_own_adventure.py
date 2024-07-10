name = input("Type your name: ")
print("Welcome,",name,"to this adventure")

answer = input(
    "You are on a dirt road, it has come to an end and you can g left or right. Which way you go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk and swim to swim accross ").lower()
    if answer == "swim":
        print("You swam accross and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game")
    else:
        print('not a valid option. You lose')    
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back)").lower()
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger, Do you talk to him or not (yes/no)").lower()
        if answer == "yes":
            print("You talk to the strange and they give you gold. you WIN!")
        elif answer == "no":
            print("You lost the gold. You lost.")
        else:
            print("No a valid answer. You lose.")
    elif answer == "back":
        print("you go back and lose.")
else:
    print('not a valid option. You lose.')

print("Thank you for trying: ",name)