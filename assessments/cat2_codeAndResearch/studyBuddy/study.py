"""
prog: study.py
name: Max A
date: 2018/05/08
desc: asks user a series of questions, gives correct/incorrect feedback, and tallies score to display at the end
"""

#displays welcome message
print("HELLO THIS IS A QUIZ 4 SKILLED PEOPLE PLZ ANSWER A B C OR D THNKS")

#list of questions and multiple choice answers
questions=['1. Which of these is not a breed of dog? A) Pugador B) Prince Charles Spaniel C) Beaglier D) Griffon Bruxellois. answer= ', '2. What is the melting point of ice (not the drug)? A) 100 celsius B) 100 Fahrenheit C) 212 Fahrenheit D) 32 Fahrenheit. answer= ', '3. What is the best/safest way to disarm a knife in close range(<2m)? A) Run away B) get stabbed then play dead C) get stabbed then be dead D) grab the knife, punch assailant and run away. answer= ', '4. Which of these is a berry? A) celery B) strawberry C) banana D) celeriac. answer= ', '5. How do you make bronze? A) tin and copper B) gold minus silver C) gold plus silver D) iron and gold. answer= ', '6. If price increases... A) demand expands and supply expands B) demand contracts and supply contracts C) demand expands and supply contracts D) demand contracts and supply expands. answer= ', '7. What is 12x12? A) 144 B) 48 C) 24 D) 121. answer= ', '8. What is the capital of Turkey? A) Bangladesh B)Ankara C)Istanbul D) Rabat', '9. Who is the founder of Amazon? A) Steve Jobs B) Bill Gates C) Jeff Bezos D) Hilary Clinton', '10. Which of these cells have cell walls? A) plant cells B) plant and animal cells C) animal cells D) bacteria and protozoa cells. answer= ']

#list of correct answers
correctAnswers=['B','D','D','C','A','D','A','B','C','A']

#sets starting score
score = 0

#defines the function 'q'
def q(i,n):
    global score
    #gets rid of whitespace and case issues
    answer=input(n).upper()
    answer = answer.strip()
    #gives feedback to user and adjusts user score
    if answer == correctAnswers[i]:
        print('Correct!')
        score=score+1
    else:
        print('Wrong! You suck!')


#goes through the questions in the list and sets a counter for each question
for i,n in enumerate(questions):
    #calls the function
    q(i,n)
#gives user their total score and comments on the score
print(' ')
print("You scored "+ str(score)+" out of 7!")
if score ==7:
    print('(PERFECT OMG)')
elif score==4 or score==5 or score==6:
    print('(hmm...reasonable)')
else:
    print('(Wow you really suck nah its all g)')

#asks user for very basic feedback on the quiz
x=input('Please rate how much you like this quiz out of 5! ')
#repsonds to the user feedback
if x==5:
    print("YEE THANKS!")
elif x==3 or x==4:
    print("Well that's a bit rude")
else:
    print("YOU'RE SO MEANNN")



