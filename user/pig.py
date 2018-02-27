"""
doesnt work i dont know why
"""
letters=input('Write something and magic will happen ')
stuff=letters.split()
owelvay = ['A','E','I','O','U','a','e','i','o','u']
yeet=[]
loop=0
while loop<len(stuff):
    if stuff[loop][0]in owelvay:
        yeet.append(stuff[loop]+ "ayyyy ")
    if stuff[loop][1] in owelvay:
            yeet.append(stuff[loop][1:]+stuff[loop][0]+"ayyy ")
    else:
        yeet.append(stuff[loop][2:]+stuff[loop][2:]+"ayyy ")

loop+= 1
magic=str(yeet)
print(magic)


