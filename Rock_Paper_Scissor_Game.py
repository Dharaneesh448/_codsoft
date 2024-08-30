import random
a=0
b=0
while True:
    x=input("Enter your choice (rock, paper, or scissors): ")
    y= random.choice(["rock", "paper", "scissors"])
    print("The user's choice is:",x)
    print("The computer's choice is:",y)
    if x==y:
        print("tie")
    elif (x=="rock" and y=="scissors"):
        print("Congratulation! You are the winner")
        a+=1
    elif (x=="scissors" and y=="paper"):
        print("Congratulation! You are the winner")
        a+=1
    elif (x=="paper" and y=="rock"):
        print("Congratulation! You are the winner")
        a+=1
    elif (x=="scissors" and y=="rock"):
        print("You lost!")
        b+=1
    elif (x=="paper" and y=="scissors"):
        print("You lost!")
        b+=1
    elif (x=="rock" and y=="paper"):
        print("Congratulation! You are the winner")
        b+=1
    else:
        print("Please Enter a valid input:")

    print("your score:",a, "computer score:",b)

    play_again = input("Do you want to play another round? (yes/no): ")
    if play_again != "yes":
        print("Thanks for playing the game!")
        break
if a>b:
        print("The overall winner in the user")
elif a<b:
    print("The overall winner is the computer")
else:
    print("The game is a Tie")
