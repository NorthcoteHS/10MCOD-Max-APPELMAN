favourites=[]
no=input("What is one of ur favourite movies? ")
while no!='quit':
    yes=input('rate out of 5 ')
    favourites.append([no])
    no=input("What is one of ur favourite movies? ")
print("Thanks boi,you stored", len(favourites),"movies")
