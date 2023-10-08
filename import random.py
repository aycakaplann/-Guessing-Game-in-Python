import random
number = random.randint(1, 100)
name = input("Enter your name : ")
print(f"Hello {name}. Let's start the game! You have 5 guesses.")
predicted_number = 0
while predicted_number<=4:
    predicted_number+=1
    guess= int(input(f" {name} Enter a number between 1 and 100 :" )) 
    if (guess<number):
        print(f"Your guess {guess} is not correct. Enter a higher number.") 
        continue
    elif(guess>number):
        print(f"Your guess {guess} is not correct. Enter a lower number.")
        continue
    else:
        print(f"Congratulations! You find the nunber correctly in your {predicted_number}. guess!")
        break
        
else:
    print(f"You're out of guesses. You didn't find the correct number. The number is : {number}")
            



