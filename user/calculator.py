number1=input('Pick a number')
number2=input('Pick another number')
operation=input('Pick an operation')
float(number1)
float(number2)
#the floats do not work and I don't know why
number3=int(number1)
number4=int(number2)
if operation==('plus')or operation==('+'):
    print("The answer is: ",number3+number4)
if operation==('minus')or operation==('-'):
    print("The answer is: ",number3-number4)
if operation==('times')or operation==('*'):
    print("The answer is: ",number3*number4)
if operation==('divide')or operation==('/'):
    print("The answer is: ",number3/number4)

