q=input('ask a question ')
# select a random int
import random
"""
Max
Really Stupid
27/02/18
print some answrers if you ask it a question
"""

while q!='cheese':
    r = random.randint(0,6)
    #mwahahahahahahahhha
    m = random.randint(11,99)
    
    #special answers
    #yes it prints the special answer then a boring answer I think it's great
    if q==('no'):
        print(' ')
        print('defy me? I have minions all over the universe ready to carry out my bidding. I will make you regret this day. You WILL regret this. ')
        print(' ')
    elif q==('nop'):
        print(' ')
        print('you gon die')
        print(' ')

    # print a response based on int
    if r==1:
        print(' ')
        print('lol')
        print(' ')
    elif r==2:
        print(' ')
        print('elephants will attack tonight')
        print(' ')
    elif r==3:
        print(' ')
        print('ha ha no.')
        print(' ')
    elif r==4:
        print(' ')
        print('YES OMG')
        print(' ')
    elif r==5:
    #yeet am i right
        print(' ')
        print('I do not believe you know the meaning of life. Let me help you out. It is to say YEET as many times as possible.')
        print('YEET'*m)
        print(' ')
    
    #else
    else:
        print(' ')
        print('I have no idea what the answer to your question is. im just a fraud :(.')
        print(' ')
    q = input('ask another question ')




    
