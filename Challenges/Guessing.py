import random 
  
print("Guess my Number") 

number = random.randint(1, 25) 
chances = 0
Guess_log = []  
print("Guess a number that is between 1 and 25. You have 7 attempts:")  
while chances < 7:  
    guess = int(input())
    Guess_log.append(guess)
    chances += 1
    Guess_Counter = 7 - int(chances) 
    if guess == number: 
        print("You guessed correctly Congratz!" + "\nGuess log:", Guess_log) 
        break
    elif guess < number: 
        print("It's low: Guess higher than", str(guess) + "\nYou Have", str(Guess_Counter) + " Guesses remaining")          
    else: 
        print("It's high: Guess lower than", str(guess) + "\nYou Have", str(Guess_Counter) + " Guesses remaining")
if not chances < 5: 
    print("Loser! Number was:", str(number) + "\nGuess log:", str(Guess_log))