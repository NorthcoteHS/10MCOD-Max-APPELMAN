q=input('ask a question ')
# select a random int
import random
"""
YOU NEED TO MAKE IT SAY YEET A RANDOM NUMBER TIMES
"""

while q!='cheese':
    r = random.randint(0,6)
    
    #special answers
    #yes it prints the special answer then a boring answer I think it's great
    if q==('no'):
        print(' ')
        print('defy me? I have minions all over the universe ready to carry out my bidding. I will make you regret this day. You WILL  regret this. ')
    elif q==('nop'):
        print(' ')
        print('you gon die')

    # print a response based on int
    if r==1:
        print(' ')
        print('lol')
    elif r==2:
        print(' ')
        print('elephants will attack tonight')
    elif r==3:
        print(' ')
        print('ha ha no.')
    elif r==4:
        print(' ')
        print('YES OMG')
    elif r==5:
        print(' ')
        print('I do not believe you know the meaning of life. Let me help you out. It is to say YEET as many times as possible. YEETYEETYEETYEETYEETYEETYEETYEET...')
    
    #else
    else:
        print(' ')
        print('I have no idea what the answer to your question is. im just a fraud :(.')
    q = input('ask another question ')




    
