import random


'''

snake=0
water=1
gun=-1

'''

computer =random.choice([0,-1,1])

# enter your chioce
youstr = input("Enter your choice :")
dict={"s":0,"w":1,"g":-1}
reversedict={1:"Water",0:"Snake",-1:"Gun"}
you = dict[youstr]

# to show what u and computer choose
print(f"Computer choose {reversedict[computer]} \nYou choose {reversedict[you]} ")


if(computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you ==1):
        print("You Win")
    elif(computer == -1 and you == 0):
        print("You lose")
    elif(computer == 1 and you == -1):
        print("You lose")
    elif(computer ==1 and you == 0):
        print("You Win")
    elif(computer == 0 and you == -1):
        print("You Win")
    elif(computer == 0 and you == 1):
        print("You lose")
    else:
        print("Something went wrong")