"""
prog: study.py
name: Max A
date: 2018/05/08
desc: asks user a series of questions, gives correct/incorrect feedback, and tallies score to display at the end
"""


questions=['Which of these is not a breed of dog? A) Pugador B) Prince Charles Spaniel C) Beaglier D) Griffon Bruxellois', 'What is the melting point of water? A) 100 celsius B) 100 Fahrenheit C) 212 Fahrenheit D) 32 Fahrenheit', 'Best way to disarm a knife in close range(<2m)? A) Run away B) get stabbed then play dead C) get stabbed then be dead D) grab the knife, punch assailant and run away', 'Which of these is a berry? A) celery B) strawberry C) banana D) celeriac', 'How do you make bronze? A) tin and copper B) gold minus silver C) gold plus silver D) iron and gold', 'If price increases... A) demand expands and supply expands B) deamnd contracts and supply contracts C) demand expands and supply contracts D) demand contracts and supply expands', 'What is 12x12? A) 144 B) 48 C) 24 D) 121']

correctAnswers=['B','D','D','C','A','D','A']

score=0

def q:

    for i,n in enumerate(questions):
        print(n)
        answer=input(n)
        if answer == correctAnswers[i]:
            print('Correct!')
            score +=1
        else:
            print('Wrong! You suck!')




