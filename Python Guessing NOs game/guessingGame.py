import random 
number  =  random.randint (1,9)
chances  = 0

while chances < 5 :
    guess = int(input("enter your guess : "))

    if guess == number :
        print("You won") 
        break 
    elif guess < number :
        print ("your guess was too low")

    else : 
        print ("Your guess was too high")

    chances +=1 

if not chances <5 :
    print ("You lose. The number is  ",number)
    
        

