"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1700
Respository: https://github.com/RoddenBona/PROG1700
Project: Dinosaur Chicken Eating
Programming language: Python 3
Version 2.75
Last Edited Dec.13.2023
"""

#Values set for amount of chicken left, number of days past, and how much chicken the dinosaur
#Will start eating on the first day and
chkn = 20
days = 0
chkn_eat = 0

#While the amount the chicken left is not 0. the program will continue to calculate how much
#Will be eaten, and increment the passing days in a loop until there is no chicken left
while chkn > 0:
    #At the start of the loop increment the amount the days as it makes no sense to begin on day 0
    days = days + 1
    if days == 1: # On day 1 the dino starts with eating 1 pound of chicken
        chkn_eat = 1.00
    #Little message displaying what number day it is and how much chicken is left
    print(f"On day {days} There were {chkn:.2f} pounds of chicken")
    #On day 7. The Dino gets sick and doesn't eat anything
    if days == 7:
        print(f"The dinosaur was sick on day {days}. So he did not eat any chicken")

#If the Dino is not sick on day 7. This program will determine how much will be eaten each day
    else:
        #The chicken value will have it's value subtracted by the chicken eat value. Rounded to
        #The nearest hundreth decimal. Starting with 1 pound on day 1
        chkn = chkn - chkn_eat
        #Another little message howing how much the Dino ate each day
        print(f"The Dinosaur ate {chkn_eat:.2f} pounds of the chicken on that day")
        #Increase the amount of chicken that will be eaten on the next day by 0.05 times # of days
        # rounded to the nearest hundreth
        chkn_eat = (chkn_eat + (chkn_eat * 0.05))
        

#If there is no more chicken left. Display below message, and end the program as the loop is no
#longer active
if chkn <= 0:
    chkn = 0
    print(f"And now the chicken is all gone within {days} days")