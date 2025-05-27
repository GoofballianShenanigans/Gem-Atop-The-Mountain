# imports
import random
# Variables
game_over = False
started = False

max_hp = 100
location = ""
current_hp = max_hp
attack = 1
defense = 1
gold = 0
exp = 0
level = 1
kills = 0

inshop = False
shop = "none"

enemy = "none"
enemyclass = "none"
thief1alive = True
thief2alive = True
slime1alive = True
slime2alive = True
slime3alive = True
elitethiefalive = True

m3oremined = False
m5oremined = False
m7oremined = False

# Level up func.
def levelup():
    global level
    global exp
    for i in range(1, 5):
        if exp >= 20*level:
            level += 1

# To be attack function
def attack(object):
    global enemy
    global enemyclass
    global current_hp
    global attack
    global defense
    global gold
    global exp
    global kills

# Interact function
def interact(object):
    global location

# Interaction functions
def goldshop():
    global gold
    global shop
    shop = "goldenfalls"
    inshop = True
    print("'Hey there, venturer! Interested in my wares?'")
    print("The shopkeeper shows you everything in stock.")
    print("Tempitem1: 15 gold.")
    print("Tempitem2: 10 gold, 2 ore.")


# Area functions
def death():
    global current_hp
    global game_over

    if current_hp <=0:
        print("You have died.")
        game_over = True

def goldenfalls():
    global location
    global started
    location = "goldenfalls"
    if started == False:
        print("Welcome to the town of Goldenfalls.")
        print("You've overheard talk about a powerful gem atop the nearby treacherous mountain.")
        print("Your goal is to obtain this gem, and achieve glory.")
        started = True
    else:
        print("Welcome back to goldenfalls.")
    print("As you look around, you spot a shopkeeper, training dummies, the surrounding cliffs, and the vast meadow to the north.")

def m1():
    global location
    global enemy
    global enemyclass
    global thief1alive
    location = "m1"
    print("You have wandered into the meadow.")
    if thief1alive == True:
        print("A thief stands here, seemingly wanting to fight.")
        enemy = "thief1"
        enemyclass = "thief"

def m2():
    global location
    location = "m2"
    print("You have wandered into the meadow.")

def m3():
    global location
    global enemy
    global enemyclass
    global slime1alive
    global m3oremined
    location = "m3"
    print("You have wandered into the meadow.")
    if slime1alive == True:
        print("A bouncy slime stands in front of you, as if it wants to violently play.")
        enemy = "slime1"
        enemyclass = "slime"
    if m3oremined == False:
        print("A rock with ores piques your interest, maybe you could use your pickaxe.")

def m4():
    global location
    global slime2alive
    location = "m4"
    print("You have wandered into the meadow.")
    if slime2alive == True:
        print("A bouncy slime stands in front of you, as if it wants to violently play")
        enemy = "slime2"
        enemyclass = "slime"

def m5():
    global location
    global elitethiefalive
    global m5oremined
    location = "m5"
    print("You have wandered deep into the meadow, the hills infront of you.")
    if m5oremined == False:
        print("A rock with ores piques your interest, maybe you could use your pickaxe.")
    if elitethiefalive == True:
        print("You see a thief, more shadowy and sinister than the rest, blocking the way ahead.")
    else:
        print("The path to the hills lays unprotected to progress.")

def m6():
    global location
    location = "m6"
    print("You have wandered into the meadow.")

def m7():
    global location
    location = "m7"
    print("You have climbed the clifftops of the meadow, Goldenfalls looming below you to the east.")
    if thief2alive == True:
        print("A thief stands here, seemingly wanting to fight.")
        enemy = "thief1"
        enemyclass = "thief"
    if m7oremined == False:
        print("A rock with ores piques your interest, maybe you could use your pickaxe.")


def m8():
    global location
    location = "m8"
    print("You have climbed the clifftops of the meadow, Goldenfalls looming below you to the west.")
    if slime3alive == True:
        print("A bouncy slime stands in front of you, as if it wants to violently play")

def h1():
    global location
    location = "h1"

# THE MOVE FUNCTION ALONE.
def move(direction):
    global location
    global enemy

    if enemy == "gem":
        print("AS YOU TRY TO ESCAPE, THE POWER OF THE GEM PULLS YOU BACK. THERE IS NO RUNNING.")
    elif enemy == "grim":
        print("The door out of Grim's lair is locked behind you. You cannot back out now.")
    if inshop == True:
        print("You are currently shopping. Type 'exit' to stop.")
    elif location == "goldenfalls":
        if direction == "north":
            m2()
        else:
            print("You cannot move that way.")
    elif location == "m1":
        if direction == "north":
            m4()
        elif direction == "east":
            m2()
        elif direction == "south":
            m7()
        else:
            print("You cannot move that way.")
    elif location == "m2":
        if direction == "north":
            m5()
        elif direction == "south":
            goldenfalls()
        elif direction == "west":
            m1()
        elif direction == "east":
            m3()
        print("You cannot move that way.")
    elif location == "m3":
        if direction == "north":
            m6()
        elif direction == "west":
            m2()
        elif direction == "south":
            m8()
        else:
            print("You cannot move that way.")
    elif location == "m4":
        if direction == "east":
            m5()
        elif direction == "south":
            m1()
        else:
            print("You cannot move that way.")
    elif location == "m5":
        if direction == "north":
            if elitethiefalive == False:
                h1()
            else:
                print("As you try to walk towards the hills, the figure stops you in your path. You must fight it.")
        elif direction == "west":
            m4()
        elif direction == "east":
            m6()
        elif direction == "south":
            m2()
        else:
            print("You cannot move that way.")
    elif location == "m6":
        if direction == "west":
            m5()
        elif direction == "south":
            m3()
        else:
            print("You cannot move that way.")
    elif location == "m7":
        if direction == "north":
            m1()
        elif direction == "east":
            print("It's not a clever idea to walk down a cliff.")
        else:
            print("You cannot move that way.")
    elif location == "m8":
        if direction == "north":
            m3()
        elif direction == "west":
            print("It's not a clever idea to walk down a cliff.")
        else:
            print("You cannot move that way.")


# main game loop
goldenfalls()
while game_over == False:
    while True:
        commands = input("What would you like to do? ").lower().strip().split()

        if len(commands) > 0:
            break

    if commands[0] == "quit":
        print("Farewell, traveller!")
        game_over = True

    if commands[0] == "help":
        print("move (direction) - move in (direction) direction, uses compass directions.")
        print("interact (person/object) - allows you to potentially talk to someone, or check out something.")
        print("attack (enemy) - allows you to attack a potential threat that's around.")

    if commands[0] == "move":
        move(commands[1])

    if commands[0] == "checklocation":
        print(location)