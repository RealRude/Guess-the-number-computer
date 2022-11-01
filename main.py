# Guess the number (computer) 12 Beginner Python Projects - Coding Course https://www.youtube.com/watch?v=8ext9G7xspg

print("")
import random

randy_number = random.randrange(1, 11)
#print("The random number is: ", randy_number)

guessed_number = 0
while guessed_number != randy_number:
    guessed_number = int(input("Please pick a number between 1 and 10: "))
    if guessed_number > randy_number:
        print("Your guess is too high.")
    elif guessed_number < randy_number:
        print("Your guess is too low")

#github-test-change

#print("Your choice is: ", guessed_number, " but randy_number was", randy_number)

print("\nYou are correct! You have correctly guessed the number: ", randy_number)

endprint = "\n\n>>>|END OF PROGRAM|<<<"
print(endprint)