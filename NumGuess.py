import random
Random_Num = random.randint(1,100)
Your_guess = int(input("Enter your guess :"))
print("Your guess is ",Your_guess)
print("Random number is ",Random_Num)
if(Your_guess > Random_Num):
    print("Too high")
elif(Your_guess < Random_Num):
    print("Too low")
elif(Your_guess == Random_Num):
    print("Correct guess")
