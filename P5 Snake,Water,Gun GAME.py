# Snake , Water & Gun
i=1
c=0
p=0
import random
while i<=10:
    comp=["Snake","Water","Gun"]
    comp_ch=random.choice(comp)
    pl_ch=input("Enter Snake, Water, Gun")
    if (pl_ch=="Snake" and comp_ch=="Water"):
        print("Computer Chose-",comp_ch)
        print("You Win")
        p+=1
    elif (pl_ch=="Snake" and comp_ch=="Gun"):
        print("Computer Chose-",comp_ch)
        print("You Lose")
        c+=1
    elif (pl_ch=="Water" and comp_ch=="Snake"):
        print("Computer Chose-",comp_ch)
        print("You Lose")
        c+=1
    elif (pl_ch=="Water" and comp_ch=="Gun"):
        print("Computer Chose-",comp_ch)
        print("You Win")
        p+=1
    elif (pl_ch=="Gun" and comp_ch=="Snake"):
        print("Computer Chose-",comp_ch)
        print("You Win")
        p+=1
    elif (pl_ch=="Gun" and comp_ch=="Water"):
        print("Computer Chose-",comp_ch)
        print("You Lose")
        p+=1
    elif pl_ch==comp_ch:
        print("Computer Chose-",comp_ch)
        print("Draw")
    else:
        print("Wrong Input")
        continue
    i=i+1
if p>c:
    print("Congratulations You Win")
elif p<c:
    print("Sorry,You Lose")
else:
    print("Its A Draw")


