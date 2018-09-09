import os
import random as ra
import sys
from conf import c, w

def title():

    # The Title ASCII Menu because ASCII shit is cool... 
    print(c.title + """
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    + $$$$$$$             $$$$$$                                          $$               +
    + $$    $$           $$     $$                                                         +
    + $$    $$ $$     $$ $$          $$$$$$  $$$$$$$   $$$$$$    $$$$$$$  $$  $$$$$$$      +
    + $$$$$$$  $$     $$ $$   $$$$  $$    $$ $$    $$ $$    $$  $$        $$ $$            +
    + $$       $$     $$ $$      $$ $$$$$$$$ $$    $$ $$$$$$$$   $$$$$$   $$   $$$$$$      +
    + $$       $$     $$  $$     $$ $$       $$    $$ $$              $$  $$        $$     +
    + $$         $$$$$$$   $$$$$$    $$$$$$$ $$    $$  $$$$$$$  $$$$$$$   $$  $$$$$$$      +
    +                 $$                                                                   +
    +          $$     $$            for WarLite20 (c) Sean Mitchell 2018                   +     
    +            $$$$$$                                                                    +
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """ + c.clear)

def menu():    

    # The Actual Menu Options
    print(c.fair + """
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    + [1]: Generate Kingdom/Region                                    [5]: Generate Potion +
    + [2]: Generate City/Town/Village                                 [6]: Generate Tome   +
    + [3]: Generate NPC/Character                                     [7]: Generate Weapon +
    + [4]: Generate Random Item                                       [8]: Generate Armor  +
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """ + c.clear)

    # Defining some other objects as to pull more random shit from the list on conf
    r  = ra.choice
    # Random Variables for Name Generation with multi-suffix and for sirnames, multi-prefix
    p1 = ra.choice(w.pre)
    s1 = ra.choice(w.suf)
    p2 = ra.choice(w.pre)
    s2 = ra.choice(w.suf)
    s3 = ra.choice(w.suf)
    gnd = ['Male', 'Female']
    # Stats based off WarLite20 Rulebook(4d6 and the bonus is the total/2 rounded up)
    p_stats = ra.randint(1, 24)
    # The bonus stat is right now set to round down until I find a better way to handle this
    stats_b = p_stats // 2
    # Handles random names for Cities 
    cname = [p1+s1, p1+s1+s2, p1+s1+s2+s3]
    nname = [p1+s1, p1+s1+s2 + ' ' + p2+s3]
    population = [c.poor + 'Poor' + ' ' + str(ra.randint(50, 200)) + c.clear, c.fair + 'Fair'  + ' ' + str(ra.randint(200, 700)) + c.clear, c.good + 'Good' + ' ' + str(ra.randint(700, 1500)) + c.clear, c.great + 'Great' + ' ' + str(ra.randint(1500, 20000)) + c.clear]
    regions = [c.desc + 'Villages: ' + c.clear + str(ra.randint(1, 20)), c.desc +'Cities: ' + c.clear + str(ra.randint(1, 20)), c.desc + 'Towns: ' + c.clear + str(ra.randint(1, 20))]
    options = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Prompted Input
    gen = input('Please select an option: ')
    
    # Generating a Kingdom with the following options (Name w/ Title, Description, Population, Market, Inns(total), Government)
    if gen == "1":
        clear()
        print(c.title + 'Kingdom or Region:' + c.clear + ' ' + r(cname) + ' ' +  r(w.tit) + '\n' + c.desc + 'Description:' + c.clear + ' ' + r(w.des) + '\n' + r(regions))
    elif gen == "2":
        clear()
        print(c.title + 'City, Village or Town:' + c.clear + ' ' + r(cname) + '\n' + c.desc + 'Description:' + c.clear + ' ' + r(w.des) + '\n' + c.desc + 'Population: ' + c.clear + r(population))
    elif gen == "3":
        clear()
        print(c.title + 'NPC Name: ' + c.clear + r(nname) + '    ' + c.title + 'Race: ' + c.clear + r(gnd) + ' ' + r(w.rac) + '    ' + c.title + 'Class: ' + c.clear + r(w.cla) + '\n' + 'STR: ' + str(p_stats) + ' +' + str(stats_b))
    elif gen not in options:
        clear()
        print(c.poor + "Please choose a valid option from the list below!" + c.clear)

    # Clear the screen when an option is selected
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

title()

while True:
    try:
        menu()
    except KeyboardInterrupt:
        sys.exit(0)
    else:
        menu()
