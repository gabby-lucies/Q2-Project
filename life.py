import time
import tkinter
import random



country = ['Argentina', 'Russia', 'Japan', 'America', 'Puerto Rico', 'Guam', 'France', 'Canada', 'Mexico',
'Finland', 'Sweden', 'Norway', 'China', 'Germany', 'Ukraine', 'Chad', 'Guatamala', 'Brazil', 'Chile', 'Columbia',
'Iraq', 'Iran', 'Saudi Arabia', 'Egypt', 'Vietnam', 'India', 'the Phillipines', 'Cambodia', 'Indonesia', 'S. Korea',
'Portugal', 'Spain', 'Central America', 'Ecuador', 'Greenland', 'Australia', 'New Zealand', 'Austria', 'Belgium',
'Azerbaijan', 'Lithuania', 'Serbia', 'Czech Republic', 'Greece', 'Belarus', 'Denmark', 'Bangladesh', 'Angola',
'Nepal', 'Sri Lanka', 'Bulgaria', 'Bolivia', 'Italy', 'Ireland', 'England', 'Scotland', 'Wales', 'Afghanistan',
'Algeria', 'Albania', 'Andorra', 'Armenia', 'the Bahamas', 'Barbados', 'Belize', 'Botswana', 'the Ivory Coast', 'Cabo Verde',
'Cameroon', 'Costa Rica', 'Croatia', 'Eswatini', 'Ethiopia', 'Fiji', 'Georgia', 'Ghana', 'New Guinea', 'Haiti',
'Guyana', 'Iceland', 'Honduras', 'Hungary', 'Jamaica', 'Jordan', 'Kenya', 'Kuwait', 'Laos', 'Lebanon', 'Lybia',
'Luxemborg', 'Madagascar', 'Malaysia', 'Mongolia', 'Morocco', 'Netherlands', 'Niger', 'Nigeria', 'Panama',
'Peru', 'Poland', 'Singapore', 'Slovakia', 'Somalia', 'South Africa', 'Switzerland', 'Thailand', 'Turkey',
'Uganda', 'Yemen', 'Zimbabwe', 'Venezuela', 'Uruguay', 'the United Arab Emrites']

biologicalSex = ['female', 'male']

Chargender = ['cisgender', 'nonbinary', 'genderfluid', 'binary', 'cisgender', 'cisgender', 'cisgender',
'cisgender', 'cisgender', 'bigender', 'transgender', 'transgender', 'cisgender', 'cisgender', 'cisgender']

Chargay = ['straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight',
'straight', 'straight', 'straight', 'gay', 'bisexual', 'bisexual', 'asexual', 'demisexual', 'pansexual', 
'straight', 'straight', 'straight']

intellegence = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

athletic_ability = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

creativity = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

communications = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

logic = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

print("Hello, welcome to The Game of Life ")
print("You are...")
print(random.choice(biologicalSex))
time.sleep(1.5)

print("What is your character's name?")
name = input(">>> ")
time.sleep(1.5)

print(name + " is  0 years old")
age = 0
time.sleep(2)
print(name + " was born in...")
print(random.choice(country))
time.sleep(2)

print(name + " identifies as...")
print(random.choice(Chargender))
time.sleep(2)

print(name + " 's sexual orientation is...")
print(random.choice(Chargay))
time.sleep(2)

print(name + "now gets different points assigned their characteristics.")
print("Characteristic strength is based out of 15.")
print("i.e. 14/15 INTELLEGENCE")
time.sleep(3)

print(name + "'s INTELLEGENCE, ATHLETIC ABILITY, CREATIVITY, COMMUNICATIONS, and LOGIC.")
time.sleep(3)

print("Intellegence")
print(random.choice(intellegence))
time.sleep(2)
print("Athletic Ability")
print(random.choice(athletic_ability))
time.sleep(2)
print("Creativity")
print(random.choice(creativity))
time.sleep(2)
print("Communications")
print(random.choice(communications))
time.sleep(2)
print("Logic")
print(random.choice(logic))
time.sleep(2)

