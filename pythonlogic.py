import random

# Service 2

def buy():
    x = ['ak/m4', 'galil/famas', 'm249', 'AWP', 'p90', 'SSG/AUG', 'Autosniper']

    return random.choice(x) 

def eco():
    x = ['57/Tec9', 'P250', 'Dualies', 'Negev', 'Mag7','Scout', 'Sawed-off', 'Bizon', 'UMP-45', 'MP7', 'MP9/Mac10', 'MP5', 'Deagle']
    choice = random.choice(x)
    return choice

# Service 3

def ct():
    strat = ['Stack A', 'Stack B', 'Default', 'Rush Mid', '4 A', '4 B']

    return random.choice(strat)

def t():
    timea = random.randint(20,105)
    timeb = random.randint(20,105)
    strat = ['Rush A', 'Rush B',timea, timeb]
    choice = random.choice(strat)
    if choice == timea:
        return 'Push A at', timea, 'seconds'
    elif choice == timeb:
        return 'Push B at', timeb, 'seconds'
    else:
        return choice 

print(buy(), eco(), ct(), t())
