string = "Number Guessing Game"
string2 = "Guess a number (1-9)"
print(string)
print(string2)
number = 9
guess = input("Enter Your guess:-")
if(guess < 9):
    print("You Lose")
elif(guess == number):
     print("YOU WIN")
