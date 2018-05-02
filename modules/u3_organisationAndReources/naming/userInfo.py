"""
Prog:   userInfo.py
Name:   Max Appelman
Date:   12/03/18
Desc:   Asks the user for their name, address, etc.
"""

# Display welcome message.
print('Welcome to the User Information Booth! Please enter your info.')

# Get user's name.
firstName = input('First Name: ')
lastName = input('Last Name: ')

# Get user's birth date.
birthYear= input('Birth Year: ')
birthMonth = input('Birth Month: ')
birthDay = input('Birth Day: ')

# Get user's favourites.
favColour = input('Favourite colour: ')
favSong = input('Favourite song: ')
favSport = input('Favourite sport: ')

# Display exit message.
print('Thank you, your information has been saved.')
