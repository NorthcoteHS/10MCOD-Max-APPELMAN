"""
prog: study.py
name: Max A
date: 2018/05/08
desc: asks user a series of questions, gives correct/incorrect feedback, and tallies score to display at the end
"""

#displays welcome message
"HELLO THIS IS A QUIZ 4 SKILLED PEOPLE PLZ ANSWER A B C OR D THNKS"

#list of questions and multiple choice answers
questions=['Which of these is not a breed of dog? A) Pugador B) Prince Charles Spaniel C) Beaglier D) Griffon Bruxellois. answer= ', 'What is the melting point of ice (not the drug)? A) 100 celsius B) 100 Fahrenheit C) 212 Fahrenheit D) 32 Fahrenheit. answer= ', 'Best way to disarm a knife in close range(<2m)? A) Run away B) get stabbed then play dead C) get stabbed then be dead D) grab the knife, punch assailant and run away. answer= ', 'Which of these is a berry? A) celery B) strawberry C) banana D) celeriac. answer= ', 'How do you make bronze? A) tin and copper B) gold minus silver C) gold plus silver D) iron and gold. answer= ', 'If price increases... A) demand expands and supply expands B) demand contracts and supply contracts C) demand expands and supply contracts D) demand contracts and supply expands. answer= ', 'What is 12x12? A) 144 B) 48 C) 24 D) 121. answer= ']

#list of correct answers
correctAnswers=['B','D','D','C','A','D','A']

#defines the function 'q'
def q():
    #sets starting score
    score = 0
    #goes through the questions in the list and sets a counter for each question
    for i,n in enumerate(questions):
        #gets rid of whitespace and case issues
        answer=input(n).upper()
        answer = answer.strip()
        #gives feedback to user and adjusts user score
        if answer == correctAnswers[i]:
            print('Correct!')
            score +=1
        else:
            print('Wrong! You suck!')
    #gives user their total score and comments on the score
    print("You scored "+ str(score)+" out of 7!")
    if score ==7:
        print('(PERFECT OMG)')
    elif score==4 or score==5 or score==6:
        print('(hmm...reasonable)')
    else:
        print('(Wow you really suck nah its all g)')
#calls the function
q()



