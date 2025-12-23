import random
import sys
number = random.randint(1,101)

print ("you have 10 chances to guess the number between 1 and 100:")
for x in range(1,101):
    print ("what number do you guess?")
    value = int(input())
    if value < number: print ("your number is smaller than my number")
    if value > number: print ("your number is bigger than my number")
    if value == number: 
        print ("you guessed it correctly!")  
        sys.exit()