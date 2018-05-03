"""
Prog:   userInfo.py
Name:   Max Appelman
Date:   2018/03/12
Desc:   Asks the user for personal information.
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
userColour = input('Favourite colour: ')
userSong = input('Favourite song: ')
userSport = input('Favourite sport: ')

# Display exit message.
print('Thank you, your information has been saved.')
