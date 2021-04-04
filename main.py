import random

name = input("enter a name: ")
print('Hello '+ name.capitalize())

game = ['rock', 'paper', 'scissors']

x = random.choice(game)
g = (x)


print("""
the rules of the game are:
rock beats scissors
scissors beats paper
paper beats rock
""")

def main():

    print("enter either 'rock', 'paper' or 'scissors' ")
    play = input("")

    if play == "scissors":
        print(g)
        if g == "scissors":
            print('you got a draw')
        elif g == "paper":
            print("you won")
        elif g == "rock":
            print("you lost")



    elif play == "rock":
        print(g)
        if g == "rock":
            print('you got a draw')
        elif g == "paper":
            print("you lost")
        elif g == "scissors":
            print("you won")



    elif play == "paper":
        print(g)
        if g == "paper":
            print('you got a draw')
        elif g == "scissors":
            print("you lost")
        elif g == "rock":
            print("you won")
       
            

main()


v = input("do you want to play again, (y/n): ")
if v == "y":
    main()
else:
    print("understandable")