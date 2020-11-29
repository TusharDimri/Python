#number is 69
#total gusses=9,print number of guesses taken,print game over
i=1
while i <= 10:
    n = int(input("Enter your Guess"))
    if n == 69:
       print("Congratulations You Won")
       print(f"You used {i} chances")
    elif n>69:
        print("This number is greater than the number to guess")
        num = 9-i
        print("Number of guesses left=", num)
    else:
        num = 9 - i
        print("This number is smaller than the number to guess")
        print("Number of guesses left=", num)
    i = i+1
    if i == 10:
        print("You Lose")
        ch = input("Pres s Y to Play Again")
        if ch=='Y':
            i=0
            continue
        elif ch!='Y':
            print("Better Luck Next Time")
            break







