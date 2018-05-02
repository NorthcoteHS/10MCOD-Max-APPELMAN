"""
Prog:   yesNoProgram.py
Name:   Max Appelman
Date:   2018/03/12
Desc:   Answers yes or no to any question.
"""

#imports random module
import random
# Ask the user for a question.
question = input('Ask me anything! ')

# Check for special input.
if  question == 'Quit':
    print('Goodbye.)
elif question == 'Hi' or question=='Hello':
    print("What's up?")

# Answer yes or no randomly.
else:
    num = random.randint(0,4);
if num == "1":
    print("Yes!")
if num = 2:
    "No"
done
