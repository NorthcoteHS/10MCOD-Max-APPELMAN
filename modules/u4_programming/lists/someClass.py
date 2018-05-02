import random
roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah']
print (roll[2])
enrolment=len(roll)
roll.append('James')
del roll[2]
roll[5]= 'Mike'
roll.sort()
roll.reverse()
print(random.choice(roll))
first=roll[:6]
last=roll[-6:]
