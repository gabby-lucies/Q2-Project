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

#BASIC GAME FUNCTIONS
age_up = ["Age_up", "age_up"] #different valid options for inputs
stop = ["cancel", "Cancel", "back", "Back", "CANCEL"]
neckrope = ["suicide", "Suicide", "commit_suicide", "die", "commit_neckrope"]
study = ["study", "Study", "STUDY"]
no_school = ["drop_out", "dropout", "Dropout", "Drop_Out", "Drop_out"]
know_logic = ["check_logic", "Check_logic", "Check_Logic", "logic", "Logic"]
no_job = ["quit_job", "Quit_job", "Quit_Job", "No_job", "no_job"]

#STUPID "EASTER EGGS"
want_sad = ["I_want_to_be_sad", "i_want_to_be_sad", "sad"] 
spook_me = ["spook_moi", "Spook_moi"]
vino = ["do_it_for_the_vine", "Do_it_for_the_vine", "Do_it_for_the_Vine", "vine"]
weeb = ["weeb", "Weeb", "WEEB"]

#JOBS TO APPLY TO
police_job = ["apply_police", "police_apply", "Apply_police", "apply_Police", "Apply_Police"]
doctor_job = ["apply_doctor", "apply_Doctor", "Apply_Doctor", "Apply_doctor"]
mafia_job = ["apply_mafia", "Apply_mafia", "Apply_Mafia", "apply_Mafia", "join_mafia", "Join_mafia", "Join_Mafia"]
military_boi = ["join_military", "Join_military", "apply_military", "Appy_military", "military"]
retail_job = ["apply_retail", "retail", "Apply_Retail", "Apply_retail"]
writer_job = ["apply_writer", 'Apply_writer', "Apply_Writer", "join_writer", "Join_writer", "Join_Writer", "writer"]
programmer_job = ["apply_programmer", "Apply_Programmer", "Apply_programmer", "apply_Programmer", "join_programmer", "Join_programmer", "programmer"]
fastfood_job = ["Fast_food", "fast_food", "Fast_food", "Food", "food", "apply_fastfood"]
dancer_job = ["apply_dancer", "Apply_dancer", "dancer", "Dancer", "join_dancer"]
historian_job = ["Historian", "historian", "apply_historian", "Apply_Historian"]

#UNIVERSITY-RELATED STUFF
college = ["apply_college", "college", "Apply_college", "apply_postsecondary", "Apply_postsecondary", "postsecondary"]
history_major = ["history", "HISTORY", "History"]
english_major = ["english", "English", "ENGLISH"]
fl_major = ["FL", "Fl", "fl", "foreign_language", "Foreign_Language", "language"]
math_major = ["math", "Math", "Maths", "maths"]
business = ["business", "Business"]
compsci = ["CS", "cs", "Cs", "computer_science", "Computer_science", "Computer_Science"]
biology_major = ["biology", "Biology", "Bio", "bio"]
physics_major = ["Physics", "physics", "Phys", "phys"]
chemistry_major = ["chem", "Chem", "chemistry", "Chemistry"]
engineering_major = ["Engineering", "engineering", "engin", "Engin"]
art_major = ["art", "Art", "Fine_Arts", "fine_arts", "Fine_arts"]
music_major = ["music", "Music"]
education_major = ["teaching", "Teaching", "education", "Education", "ed", "Ed"]

#CONSUMERISM
house = ["buy_house", "Buy_house", "Purchase_house", "house"]
apartment = ["rent_apartment", "Apartment", "Appartment", "apartment", "Appartment"]



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

raise_chance = ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1']

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
        'F--- ya chicken strips.', 'Barbecue sauce on my tiddies.', 'Gimme ya f*ckin money.', 'Ms. Keisha, MS. KEISHA! Oh my f---in gawd she f----n dead.',
        'Fre-sha-vocado', 'That is my OPINION', 'This b---- empty, YEET!', 'Road work ahead, uh, yeah I sure hope it does.', 
        'Oh my gawd, they were roommates!', 'Watch your profanity.', 'You better stop.', 'Why you always lyin?',
        'I like turtles.', 'iridocyclitis', 'I DONT CARE THAT YOU BROKE YOUR ELBOW.', 'Try me, b----', 'I said whoever threw that paper, your mom is a hoe.',
        'So no head?', 'I am shooketh.', 'Can I PLEASE get a waffle?', 'There is only one thing worse than a rapist. A CHILD. NO.',
        'Add two shots of vodka *proceeds to pour a more than 2 shots of vodka*'] #list of random stuff

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
biology_degree = int(0) #no biology degree
chemistry_degree = int(0)
physics_degree = int(0)
engineering_degree = int(0)
teaching_degree = int(0) #no education degree
art_degree = int(0) #no fine arts degree
music_degree = int(0) #no music degree
history_degree = int(0) #no history degree

secondary_diploma = int(0) #babies can't have high school diplomas, m8
school = int(0) #not currently enrolled in school

money = float(0) #sets money = 0 because babies are poor

house = int(0)
apartment = int(0)

mafia_career = int(0)
doctor_career = int(0)
vet_career = int(0)
military_career = int(0)
police_career = int(0)
writer_career = int(0)
programmer_career = int(0)
retail_career = int(0)
fastfood_career = int(0)
dancer_career = int(0)
historian_career = int(0)

history_years = int(0)
biology_years = int(0)
education_years = int(0)
music_years = int(0)
physics_years = int(0)
chemistry_years = int(0)
art_years = int(0)
fl_years = int(0)
engineering_years = int(0)
cs_years = int(0)
business_years = int(0)
english_years = int(0)
math_years = int(0)

mafia_wage = int(42600)
fastfood_wage = int(23269)
retail_wage = int(25000)
writer_wage = int(47000)
military_wage = int(43500)
police_wage = int(64500)
programmer_wage = int(82420)
dancer_wage = int(34000)
historian_wage = int(55000)


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
        if age == 6:
            school = 1
            print("You are now attending school.")
            time.sleep(0.5)
        if age == 16 and school == 1:
            secondary_diploma = 1
            print("Congratulations, you have graduated from secondary school!")
            school = 0
            print("You are no longer attending school.")
            time.sleep(0.6)
    elif imput in age_up and 1 <= music_years <= 4 and school == 1:
        age = age + 1
        print(age)
        music_years = music_years + 1
        time.sleep(0.4)
        if music_years >= 5:
            school = 0
            music_degree = 1
            music_years = 0
            print("Congrats. You graduated from college with a degree in music.")
            time.sleep(0.3)
    elif imput in college and secondary_diploma == 0:
        print("You need a secondary diploma to go to college. Sorry!")
        time.sleep(0.3)
    elif imput in college and job == 1:
        print("You cannot have a full-time job and pursue college at the same time. Quit your job and try again.")
        time.sleep(0.3)
    elif imput in college and secondary_diploma == 1 and job == 0:
        print("You must now pick a major.")
        time.sleep(0.3)
        print("List of Majors: ")
        time.sleep(0.3)
        print("Music")
        time.sleep(0.3)
        print("Art")
        time.sleep(0.3)
        print("Foreign Language")
        time.sleep(0.3)
        print("Education")
        time.sleep(0.3)
        print("Business")
        time.sleep(0.3)
        print("Computer Science")
        time.sleep(0.3)
        print("Physics")
        time.sleep(0.3)
        print("Biology")
        time.sleep(0.3)
        print("Chemistry")
        time.sleep(0.3)
        print("Math")
        time.sleep(0.3)
        print("History")
        time.sleep(0.3)
        print("Please type in one of the above majors to apply to a 4-year university program.")
        time.sleep(0.4)
        print("To go back, type cancel.")
        if imput in music_major and music_degree == 0:
            school = 1
            music_years = 1
            print("You are now currently enrolled in music school")
            time.sleep(.3)
        if imput in art_major and art_degree == 0:
            school = 1
            art_years = 1
            print("You are now currently enrolled in art school.")
            time.sleep(0.3)
        if imput in fl_major and fl_degree == 0:
            school = 1
            fl_years = 1
            print("You are now currently pursuing a foreign langauge degree at a university.")
            time.sleep(0.2)
        if imput in education_major and teaching_degree == 0:
            school = 1
            education_years = 1
            print("You are now currently pursuing a degree in education at a university.")
            time.sleep(0.3)
        if imput in business and business_degree == 0:
            school = 1
            business_years = 1
            print("You are now currently pursuing a business degree at a university.")
            time.sleep(0.3)
        if imput in compsci and cs_degree == 0:
            school = 1
            cs_years = 1
            print("You are now pursuing a computer science degree at a university.")
            time.sleep(0.3)
        if imput in physics_major and physics_degree == 0:
            school = 1
            physics_years = 1
            print("You are now pursuing a physics degree at a univeristy.")
            time.sleep(0.3)
        if imput in biology_major and biology_degree == 0:
            school = 1
            biology_years = 1
            print("You are now pursuing a biology degree at a university.")
            time.sleep(0.3)
        if imput in chemistry_major and chemistry_degree == 0:
            school = 1
            chemistry_years = 1
            print("You are now pursuing a chemistry degree at a university.")
            time.sleep(0.3)
        if imput in math_major and math_degree == 0:
            school = 1
            math_years = 1
            print("You are now pursuing a math degreee at a university.")
            time.sleep(0.3)
        if imput in history_major and history_degree == 0:
            school = 1
            history_years = 1
            print("you are now pursuing a history degree at a university.")
            time.sleep(0.4)
        else:
            print("A problem occured. Try pursuing another major, as you most likely have a 4-year degree in the major you applied for.")
            time.sleep(0.3)
    if imput in house and money > 97889 and age > 15:
        print("Congrts. You jsut bought a house.")
        house = 1
        time.sleep(0.4)
    if imput in house and money <= 97889:
        print("You do not have enough money to buy a house.")
        time.sleep(0.3)
    if imput in house and age <= 15:
        print("You are too young to buy a house.")
        time.sleep(0.3)
    elif imput in age_up and dancer_career == 1:
        age = age + 1
        print(age)
        time.sleep(0.5)
        money = money + dancer_wage
        print(money)
        print("You earned money by working as a dancer.")
        time.sleep(.5)
        if random.choice(raise_chance) == 1:
            print("You got a raise.")
            dancer_wage = dancer_wage + dancer_wage * (.03)
            time.sleep(0.5)
        else:
            print("You did not recieve a raise this year.")
            time.sleep(0.5)
    elif imput in age_up and historian_career == 1:
        age = age + 1
        print(age)
        time.sleep(.3)
        money = money + historian_wage
        print(money)
        print("You earned money by working as a historian.")
        time.sleep(.4)
        if random.choice(raise_chance) == 1:
            print("You got a raise.")
            historian_wage = historian_wage + historian_wage * .05
            time.sleep(0.3)
    elif imput in age_up and programmer_career == 1:
        age = age + 1
        print(age)
        time.sleep(0.5)
        money = money + programmer_wage
        print(money)
        print("You earned money by working as a computer programmer.")
        time.sleep(0.6)
        if random.choice(raise_chance) == 1:
            print("You got a raise.")
            programmer_wage = programmer_wage + programmer_wage * 0.05
        else:
            print("You did not get a raise this year.")
            time.sleep(0.5)
            #This block of code gives the player the yearly amount of money from working
            #It also randomly decides if the player earned a raise
            #The raise amount is = to the previous wage + 5% of the previous wage
            #Example: If you earned 100 a year previously, now you earn 105 a year after a programmer's raise amount
    elif imput in age_up and police_career == 1:
        age = age + 1
        print(age)
        time.sleep(0.5)
        money = money + police_wage
        print(money)
        print("You earned money working as a police officer.")
        time.sleep(0.6)
        if random.choice(raise_chance) == 1:
            print("You got a raise this year.")
            police_wage = police_wage + police_wage * 0.05
        else:
            print("You did not get a raise.")
            time.sleep(0.5)
    elif imput in age_up and military_career == 1:
        age = age + 1
        print(age)
        time.sleep(0.5)
        money = money + military_wage
        print(money)
        print("You earned moeny by working in the military")
        time.sleep(0.6)
        if random.choice(raise_chance) == 1:
            print("You got a raise this year.")
            military_wage = military_wage + military_wage * 0.05
        else:
            print("You did not ear a raise this year.")
            time.sleep(0.5)
    elif imput in age_up and retail_career == 1:
        age = age + 1
        print(age)
        time.sleep(0.5)
        money = money + retail_wage
        print(money)
        print("You earned money by working at a retail store.")
        time.sleep(0.5)
        if random.choice(raise_chance) == 1:
            print("You earned a raise this year.")
            retail_wage = retail_wage + retail_wage * 0.05
        else:
            print("You did not earn a raise this year.")
            time.sleep(0.5)
    elif imput in age_up and fastfood_career == 1:
        age = age + 1
        print(age)
        time.sleep(0.5)
        money = money + fastfood_wage
        print(money)
        print("You earned money by working in a fast food resturant.")
        time.sleep(0.5)
        if random.choice(raise_chance) == 1:
            print("You earned a raise this year.")
            fastfood_wage = fastfood_wage + fastfood_wage * 0.04
            time.sleep(0.5)
        else:
            print("You did not earn a raise this year.")
            time.sleep(0.5)
    elif imput in age_up and writer_career == 1:
        age = age + 1
        print(age)
        time.sleep(0.5)
        money = money + writer_wage
        print(money)
        print("You earned money by working as a writer")
        time.sleep(0.5)
        if random.choice(raise_chance) == 1:
            print("You earned a raise this year.")
            writer_wage = writer_wage + writer_wage * 0.06
            time.sleep(0.5)
        else:
            print("You did not earn a raise this year.")
            time.sleep(0.5)
    elif imput in age_up and mafia_career == 1:
        age = age + 1
        print(age)
        time.sleep(1)
        money = money + mafia_wage
        print(money)
        print("You earned money from working in the mafia.")
        time.sleep(1)
        if random.choice(raise_chance) == 1:
            print("You earned a raise this year.")
            mafia_wage = mafia_wage + mafia_wage * 0.03
            time.sleep(0.5)
        else:
            print("You did not earn a raise this year.")
            time.sleep(.5)
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
        mafia_career = 0
        doctor_career = 0
        vet_career = 0
        police_career = 0
        military_career = 0
        writer_career = 0
        programmer_career = 0
        retail_career = 0
        fastfood_career = 0
        dancer_career = 0
        historian_career = 0
        print("You quit your job.")
        time.sleep(2)
    elif imput in neckrope: #end the game early via suicide
        life_status = 1
        print("YOU ARE DEAD")
        exit()
    elif imput in historian_job and job == 0 and history_degree == 1:
        job = 1
        historian_career = 1
        print("You are now a historian.")
        time.sleep(.3)
    elif imput in historian_job and history_degree == 0:
        print("You need a 4-year degree in history to become a historian.")
        time.sleep(0.3)
    elif imput in historian_job and job == 1 or school == 1:
        print("You must quit your job or finish school before you can become a historian.")
    elif imput in dancer_job and job == 0 and athletic_ability >= 9 and age > 13:
        job = 1
        dancer_career  = 1
        print("You are now a dancer.")
        time.sleep(0.5)
    elif imput in dancer_job and job == 1:
        print("You cannot get a job because you already have a job. Quit your current job and try again.")
        time.sleep(0.5)
    elif imput in dancer_job and age < 14:
        print("You are too young to become a dancer. Try again next year.")
        time.sleep(.5)
    elif imput in dancer_job and athletic_ability < 9:
        print("You are not athletic enough to become a dancer. Please try again.")
        time.sleep(.5)
    elif imput in programmer_job and job == 0 and secondary_diploma == 1 and logic >= 8:
        job = 1
        programmer_career = 1
        print("You are now a computer programmer.")
        time.sleep(0.5)
    elif imput in programmer_job and job == 0 and secondary_diploma == 1 and logic < 8:
        print("Your logical reasoning skills are not high enough to become a computer programmer.")
        time.sleep(0.5)
    elif imput in programmer_job and age > 15:
        print("You are too young to become a computer programmer.")
        time.sleep(0.5)
    elif imput in programmer_job and secondary_diploma == 0:
        print("You do not have the education requried to become a comptuer programmer.")
        time.sleep(0.5)
    elif imput in fastfood_job and job == 0 and age > 14:
        job = 1
        fastfood_career = 1
        print("You are now working at a fast food resturant.")
        time.sleep(0.6)
    elif imput in fastfood_job and job == 0 and age <= 14:
        print("You are too young to work in a fast food resturant.")
        time.sleep(0.5)
    elif imput in fastfood_job and job == 1 and age > 14:
        print("You already have a job. Quit your current job if you want to work as a fast food worker.")
    elif imput in retail_job and job == 0 and age > 14:
        job = 1
        retail_career = 1
        print("You are now working at a retail store.")
        time.sleep(0.6)
    elif imput in retail_job and job == 1:
        print("You already have a job. Quit your current job to become a retail store worker.")
        time.sleep(0.5)
    elif imput in retail_job and age < 15:
        print("You are too young to work at a retail store.")
        time.sleep(0.5)
    elif imput in writer_job and job == 0 and char_communications > 7:
        job = 1
        writer_career = 1
        print("You are now a writer.")
        time.sleep(0.5)
    elif imput in writer_job and job == 0 and char_communications <= 7:
        print("You do not have the communication skills to become a writer.")
        time.sleep(0.5)
    elif imput in writer_job and age > 14:
        print("You are too young to become a writer. Maybe next year!")
    elif imput in writer_job and job == 1:
        print("You currently have a job. Quit your current job and try again to become a writer.")
        time.sleep(0.5)
    elif imput in police_job and job == 0 and secondary_diploma == 1 and char_athletic >= 5: #allows you to apply to job if you do not already have a job and you graduated from secondary school
        job = 1
        police_career = 1
        print("You are now a police officer.")
        time.sleep(1)
    elif imput in police_job and job == 0 and secondary_diploma == 1 and char_athletic < 5:
        print("You are not atheltic enough to become a police officer at the moment.")
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
    elif imput in study: #increases char_logic by .25 points
        print("You studied.")
        char_logic = char_logic + .25
        time.sleep(0.5)
    elif imput in know_logic:
        print(char_logic)
    else:
        print("That is not a valid response. Please try again.")
        time.sleep(1)

