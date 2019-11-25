import time
import random
#import tkinter
from PIL import Image
import math
from tkinter import *
from tkinter import ttk
import winsound

#root = Tk()
#win = Canvas(root, width = 500, height = 500)
#win.grid()

age_up = ["Age_up", "age_up"] #different valid options for inputs
want_sad = ["I_want_to_be_sad", "i_want_to_be_sad", "sa  bd"] 
spook_me = ["spook_moi", "Spook_moi"]
vino = ["do_it_for_the_vine", "Do_it_for_the_vine", "Do_it_for_the_Vine", "vine"]
no_job = ["quit_job", "Quit_job", "Quit_Job", "No_job", "no_job"]
neckrope = ["suicide", "Suicide", "commit_suicide", "die", "commit_neckrope"]
police_job = ["apply_police", "police_apply", "Apply_police", "apply_Police", "Apply_Police"]
doctor_job = ["apply_doctor", "apply_Doctor", "Apply_Doctor", "Apply_doctor"]
mafia_job = ["apply_mafia", "Apply_mafia", "Apply_Mafia", "apply_Mafia", "join_mafia", "Join_mafia", "Join_Mafia"]
no_school = ["drop_out", "dropout", "Dropout", "Drop_Out", "Drop_out"]
study = ["study", "Study", "STUDY"]
military_boi = ["join_military", "Join_military", "apply_military", "Appy_military", "military"]
know_logic = ["check_logic", "Check_logic", "Check_Logic", "logic", "Logic"]
weeb = ["weeb", "Weeb", "WEEB"]

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
'Uganda', 'Yemen', 'Zimbabwe', 'Venezuela', 'Uruguay', 'the United Arab Emrites'] #a pool of countries your character can be born in

thirdworld = ['Argentina', 'Puerto Rico', 'Guam', 'Mexico', 'Ukraine', 'Chad', 'Guatamala', 'Brazil', 'Chile',
              'Columbia', 'Egypt', 'Vietnam', 'India', 'the Phillipines', 'Cambodia', 'Indonesia', 'Central America',
              'Ecuador', 'Lithuania', 'Serbia', 'Nepal', 'Sri Lanka', 'Afghanistan', 'Algeria', 'Albania', 'Botswana',
              'the Ivory Coast', 'Cabo Verde', 'Cameroon', 'Coasta Rica' ,'Eswatini', 'Ethiopia', 'Ghana', 'Haiti',
              'Madagascar', 'Malaysia', 'Mongolia', 'Guyana', 'Honduras', 'Jordan', 'Kenya', 'Laos', 'Lybia',
              'Somalia', 'Uganda', 'Yemen', 'Zimbabwe', 'Venezuela', 'Uruguay', 'Fiji', 'Thailand', 'Hungary', 
              'Jamaica', 'Niger', 'Nigeria', 'Morocco', 'Turkey', 'Bangladesh', 'Bolivia', 'Belize', 'Lebanon',
              'Slovakia'] #conuntries classified as more difficult for character to live in

biologicalSex = ['female', 'male'] #allows code to choose between to sexes at the beginning of the game

gender_idenity = ['cisgender', 'nonbinary', 'genderfluid', 'binary', 'cisgender', 'cisgender', 'cisgender',
'cisgender', 'cisgender', 'bigender', 'transgender', 'transgender', 'cisgender', 'cisgender', 'cisgender']
#different gender identies your character can randomly be assigned. Cisgender appears more because it makes it
#more likely to be choosen, because it is more common IRL

sexual_orientations = ['straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight',
'straight', 'straight', 'straight', 'gay', 'bisexual', 'bisexual', 'asexual', 'demisexual', 'pansexual', 
'straight', 'straight', 'straight']
#list of sexual orientations that a character can be randomly assigned
#straight appears more often because so it is more likely to be choosen

sad = ['Your bones are always wet', 'Like if you cri evrytim', 'The average sugar baby makes about the same amount as someone with a two-year degree.',
      'The flat earth society has members all around the globe.', 'Chick-fil-a cures homosexuality', 'big mood',
       'Double rainbow all da way across da sky (its so bootyful)', 'Technically, you live in a dystopia because its not a utopia.', 'hi.', 
       'Alex Jones makes more money than u fam.'] #easter egg thing

spoops = ['Boo', 'BOO', '*ghost noises*', 'UWU', 'Now you OWO', 'cannibals exist', 'Vine is DEAD', 'They are putting chemicals in the water, that are turning the freaking frogs gay',
         'Rawr means I luv u in dinosaur' ] #list of random stuff

vines = ['Ooooo, he needs some milk.', 'Hi, welcome to chilis.', 'I smell like beef.', 'It is Wednesday, my dudes.'
        'F*ck ya chicken strips.', 'Barbecue sauce on my tiddies.', 'Gimme ya f*ckin money.', 'Ms. Keisha, MS. KEISHA! Oh my f*ckin gawd she f*ckin dead.',
        'Fre-sha-vocado', 'That is my OPINION', 'This bitch empty, YEET!', 'Road work ahead, uh, yeah I sure hope it does.', 
        'Oh my gawd, they were roommates!', 'Watch your profanity.', 'You better stop.', 'Why you always lyin?',
        'I like turtles.', 'iridocyclitis', 'I DONT CARE THAT YOU BROKE YOUR ELBOW.', 'Try me, bitch', 'I said whoever threw that paper, your mom is a hoe.',
        'So no head?', 'I am shooketh.', 'Can I PLEASE get a waffle?', 'There is only one thing worse than a rapist. A CHILD. NO.',
        'Add two shots of vodka *proceeds to pour a WAY more than 2 shots of vodka*'] #list of random stuff

otaku = ["OWO", "UoU", "owo", "uwu", 'UwU', 'You are a weeb.', 'Stop it. Get some help.']


life_status = int(0) #makes you alive
job = int(0) #you dont have a job
medical = int(0) #you dont have a medical degree
dental = int(0) #you dont have a dental degree
vet_school = int(0) #you didn't go to vet school
cs_degree = int(0) #no CS degree
english_degree = int(0) #no english degree
fl_degree = int(0) #no foreign language degree
business_degree = int(0) #no business degree
math_degree = int(0) #no math degree
science_degree = int(0) #no science degree
teaching_degree = int(0) #no education degree
art_degree = int(0) #no fine arts degree
music_degree = int(0) #no music degree
history_degree = int(0) #no history degree
secondary_diploma = int(0) #babies can't have high school diplomas, m8
school = int(0) #not currently enrolled in school
money = float(0) #sets money = 0 because babies are poor
mafia_career = int(0)
doctor_career = int(0)
vet_career = int(0)
military_career = int(0)
police_career = int(0)


intellegence = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'] 

athletic_ability = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

creativity = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

communications = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

logic = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
#allows code to randomly assign character with different characteristic points

print("Hello, welcome to The Game of Life ")
print("You are...")
print(random.choice(biologicalSex)) #randomly chooses character's sex
time.sleep(1.5) #pauses game for 1.5 seconds

print("What is your character's name?")
name = input(">>> ") #allows you to input a name, and the program "saves" it
time.sleep(1.5)

print(name + " is  0 years old")
age = 0 #age is 0 years old
time.sleep(2)
print(name + " was born in...")
char_origin = random.choice(country) #randomly chooses country character is born in
print(char_origin) #saves origin country for later reference
time.sleep(2)


print(name + " identifies as...")
chargender = random.choice(gender_idenity) #randomly chooses character's gender identity
print(chargender) #prints what it randomly chooses
time.sleep(2)

print(name + " 's sexual orientation is...")
chargay = random.choice(sexual_orientations) #randomly chooses a sexual orientation
print(chargay) #shows the results
time.sleep(2)

print(name + "now gets different points assigned their characteristics.")
print("Characteristic strength is based out of 15.")
print("i.e. 14/15 INTELLEGENCE")
time.sleep(3) #instructions

print(name + "'s INTELLEGENCE, ATHLETIC ABILITY, CREATIVITY, COMMUNICATIONS, and LOGIC.")
time.sleep(3)

print("Intellegence")
char_int = float(random.choice(intellegence)) #randomly chooses intellegence points
print(char_int)
time.sleep(2)
print("Athletic Ability")
char_athletic = float(random.choice(athletic_ability)) #randomly chooses atheltic points
print(char_athletic)
time.sleep(2)
print("Creativity")
char_creative = float(random.choice(creativity)) #randomly chooses creativity points
print(char_creative)
time.sleep(2)
print("Communications")
char_communications = float(random.choice(communications)) #randomly chooses communication points
print(char_communications)
time.sleep(2)
print("Logic")
char_logic = float(random.choice(logic)) #randomly chooses logic points
print(char_logic)
time.sleep(2)

while True: #allows to make player keep entering input
    imput = input(">>> ")            
    if imput in age_up and job == 0: #ages character up 1 year
        print(age + 1)
        age = age + 1
        time.sleep(1)
    elif imput in age_up and mafia_career == 1:
        age = age + 1
        print(age)
        time.sleep(1)
        money = money + 42600
        print(money)
        print("You earned money from working in the mafia.")
        time.sleep(1)  
    elif imput in want_sad: #prints dumb stuff
        print(random.choice(sad))
        time.sleep(1.5)
    elif imput in spook_me: #prints dumb stuff
        print(random.choice(spoops))
        time.sleep(1.5)
    elif imput in vino: #prints vine references
        print(random.choice(vines))
        time.sleep(1.5)
    elif imput in weeb:
        print(random.choice(otaku))
        time.sleep(1)
    elif imput in no_job: #quits character's job
        job = 0
        mafia_job = 0
        doctor_job = 0
        vet_job = 0
        police_job = 0
        military_job = 0
        print("You quit your job.")
        time.sleep(2)
    elif imput in neckrope: #end the game early via suicide
        life_status = 1
        print("YOU ARE DEAD")
        exit()
    elif imput in police_job and job == 0 and secondary_diploma == 1: #allows you to apply to job if you do not already have a job and you graduated from secondary school
        job = 1
        police_career = 1
        print("You are now a police officer.")
        time.sleep(1)
    elif imput in police_job and job == 1: #tells character they cannot get this job because they already have a job
        print("You already have a job, and you do not have time to work two jobs.")
        time.sleep(1)
    elif imput in doctor_job and job == 0 and age == 18 and medical == 1:
        job == 1
        doctor_career = 1
        print("You are now a doctor.")
        time.sleep(1)
    elif imput in doctor_job and job == 1:
        print("You already have a job, and you do not have time to work two jobs.")
    elif imput in mafia_job and job == 0 and age >= 14:
        job = 1 #makes it recognize that NOW you have a job
        mafia_career = 1
        print("Congrats. You joined the mafia.")
        time.sleep(1)
    elif imput in mafia_job and job == 0 and age < 14:
        print("Sorry, but you are too young to join the mafia.")
        time.sleep(1)
    elif imput in no_school and age >= 12:
        secondary_diploma = 0 #assumes you will not get a diploma
        school = 0 #says you are not in school
        print("You dropped out of school. Have fun with that!")
        time.sleep(1)
    elif imput in no_school and age < 12:
        print("You are not old enough to drop out of school.")
        time.sleep(1)
    elif imput in military_boi and age >= 17 and athletic_ability >= 8:
        job = 1
        military_career = 1
        print("You are now in the military.")
    elif imput in military_boi and age >= 17 and athletic_ability < 8:
        print("You are not fit for the military.")
        print("Try getting a different job, or going to the gym.")
        time.sleep(1)
    elif imput in military_boi and age < 17:
        print("You are not old enough to join the military.")
    elif imput in military_boi and job == 1:
        print("You already have a job. If you want to join the military, quit your job and try again.")
    elif imput in study:
        print("You studied.")
        char_logic = char_logic + .25
        time.sleep(0.5)
    elif imput in know_logic:
        print(char_logic)
    else:
        print("That is not a valid response. Please try again.")
        time.sleep(1)

