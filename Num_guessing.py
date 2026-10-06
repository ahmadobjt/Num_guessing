import random

print("click 1: Kids")
print("click 2: Easy")
print("click 3: Medium")
print("click 4: Hard")
# generting random num

mode=int(input("Enter your mode: "))

if(mode==1):
    max_nums=50
    max_attempts=20
elif(mode==2):
    max_nums=100
    max_attempts=15
elif(mode==3):
    max_nums=150
    max_attempts=10
elif(mode==4):
    max_nums=200
    max_attempts=8
else:
    max_nums=100
    max_attempts=15
    print("Invalid number,range(1 to 4)")
    print("Default mode is easy")
    
secret_no=random.randint(1,max_nums)
attempts=0
Won=False
total_attempts=max_attempts
while attempts<max_attempts:
    try:
        guess=int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid num")
        continue
        
    attempts+=1
    if(guess == secret_no):
        print("Correct!")
        print("You guessed the right num at attempts",attempts)
        Won=True
        break
    elif(guess<secret_no):
        print("Your guess is low")
        total_attempts-=1
        print("attempts left",total_attempts)
    elif(guess>secret_no):
        print("Your guess is high")
        total_attempts-=1
        print("attempts left",total_attempts)
        
if(not Won):    
    print("Your attempts has ended & you lost the game")        
    print("The secret number was ",secret_no,"\nPlz try again")        






