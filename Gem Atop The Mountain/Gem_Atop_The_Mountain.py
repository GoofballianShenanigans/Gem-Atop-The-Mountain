# imports
import random
from re import L
from tkinter import CURRENT
# Variables
game_over = False
started = False

max_hp = 100
location = ""
current_hp = max_hp
attack = 2
defense = 1
gold = 0
exp = 0
level = 1
kills = 0

inshop = False
shop = "none"

enemy = "none"
thief1alive = True
thief1hp = 8
thief2alive = True
thief2hp = 8
slime1alive = True
slime1hp = 12
slime2alive = True
slime2hp = 12
slime3alive = True
slime3hp = 12
elitethiefalive = True
elitethiefhp = 17

skeleton1alive = True
skeleton1hp = 14
skeleton2alive = True
skeleton2hp = 14
skeleton3alive = True
skeleton3hp = 14
jack1alive = True
jack1hp = 12
jack2alive = True
jack2hp = 12
amethystalive = True
amethysthp = 17
topazalive = True
topazhp = 25

orc1alive = True
orc1hp = 20
orc2alive = True
orc2hp = 20
stone1alive = True
stone1hp = 22
stone2alive = True
stone2hp = 22
stone3alive = True
stone3hp = 22
piercer1alive = True
piercer1hp = 19
piercer2alive = True
piercer2hp = 19
crystalalive = True
crystalhp = 25
ogrealive = True
ogrehp = 40

goat1alive = True
goat1hp = 25
goat2alive = True
goat2hp = 25
goat3alive = True
goat3hp = 25
guru1alive = True
guru1hp = 23
guru2alive = True
guru2hp = 23
guru3alive = True
guru3hp = 23
golem1alive = True
golem1hp = 28
golem2alive = True
golem2hp = 28
corruptalive = True
corrupthp = 35
guardianalive = True
guardianhp = 40
gemhp = 50

ethiefchoose = 0
amechoose = 0
topazchoose = 0
ame_cb = 0
orc_choose = 0
orc_cb = 0
piercer_choose = 0
crystal_cb = 0
crystal_choose = 0
summit_choose = 0
summit_cb = 0
# Level up func.
def levelup():
    global level
    global exp
    global attack
    global defense
    global max_hp
    for i in range(1, 5):
        if exp >= 20*level:
            print("You leveled up!")
            level += 1
            print("+1 ATK, +1 DEF, +50 MAXHP.")
            attack += 1
            defense += 1
            max_hp += 50

# DARN THAT'S ALOT FOR AN ATTACK FUNCTION...
def fight(object):
    global enemy
    global enemyclass
    global current_hp
    global attack
    global defense
    global gold
    global exp
    global kills

    global thief1hp
    global thief2hp
    global slime1hp
    global slime2hp
    global slime3hp
    global elitethiefhp
    global skeleton1hp
    global skeleton2hp
    global skeleton3hp
    global jack1hp
    global jack2hp
    global amethysthp
    global topazhp
    global orc1hp
    global orc2hp
    global stone1hp
    global stone2hp
    global stone3hp
    global piercer1hp
    global piercer2hp
    global crystalhp
    global ogrehp

    global thief1alive
    global thief2alive
    global slime1alive
    global slime2alive
    global slime3alive
    global elitethiefalive
    global skeleton1alive
    global skeleton2alive
    global skeleton3alive
    global jack1alive
    global jack2alive
    global amethystalive
    global topazalive
    global orc1alive
    global orc2alive
    global stone1alive
    global stone2alive
    global stone3alive
    global piercer1alive
    global piercer2alive
    global crystalalive
    global ogrealive

    global guru1alive
    global guru2alive
    global guru3alive
    global golem1alive
    global golem2alive
    global goat1alive
    global goat2alive
    global goat3alive
    global corruptalive
    global guardianalive
    global guru1hp
    global guru2hp
    global guru3hp
    global golem1hp
    global golem2hp
    global goat1hp
    global goat2hp
    global goat3hp
    global corrupthp
    global guardianhp
    global gemhp

    global ethiefchoose
    global ame_cb
    global amechoose
    global topazchoose
    global orc_choose
    global orc_cb
    global piercer_choose
    global summit_choose
    global summit_cb

    if object == "thief":
        if enemy == "thief1" and thief1alive == True:
            damage = random.randint(0, attack)
            if damage > 0:
                print("You succesfully attack the thief for" , damage , "damage.")
                thief1hp -= damage
            else:
                print("You attempt to attack, but the thief dodges.")
            damage = random.randint(-defense, 3)
            if damage > 0:
                print("The thief stabs you with its dagger, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The thief fails to stab you with its dagger.")
            if thief1hp <= 0:
                print("You have succesfully slain the thief.")
                print("+3 XP, +3 GOLD.")
                exp += 3
                gold += 3
                enemy = "none"
                thief1alive = False
                levelup()
        elif enemy == "thief2" and thief2alive == True:
            damage = random.randint(0, attack)
            if damage > 0:
                print("You succesfully attack the thief for" , damage , "damage.")
                thief2hp -= damage
            else:
                print("You attempt to attack, but the thief dodges.")
            damage = random.randint(-defense, 3)
            if damage > 0:
                print("The thief stabs you with its dagger, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The thief fails to stab you with its dagger.")
            if thief2hp <= 0:
                print("You have succesfully slain the thief.")
                print("+3 XP, +3 GOLD.")
                exp += 3
                gold += 3
                enemy = "none"
                thief2alive = False
                levelup()
        elif enemy == "elitethief" and elitethiefalive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You succesfully attack the elite thief for" , damage , "damage.")
                elitethiefhp -= damage
            else:
                print("You attempt to attack, but the elite thief dodges.")
            ethiefchoose = random.randint(1, 3)
            if ethiefchoose == 3:
                damage = random.randint(1, 3)
                print("The elite thief strikes you, quicker than you can react, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 4)
                if damage > 0:
                    print("The elite thief stabs you with its dagger, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The elite thief fails to stab you with its dagger.")
            if elitethiefhp <= 0:
                print("You have succesfully slain the elite thief, the northward path to the hills has opened.")
                print("+5 XP, +7 GOLD.")
                exp += 5
                gold += 7
                enemy = "none"
                elitethiefalive = False
                levelup()

    elif object == "slime":
        if enemy == "slime1" and slime1alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You succesfully attack the slime for" , damage , "damage.")
                slime1hp -= damage
            else:
                print("You attempt to attack, but the slime absorbs your blow.")
            damage = random.randint(-defense, 2)
            if damage > 0:
                print("The slime bounces on you, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The slime bounces on you, but not with enough force to harm.")
            if slime1hp <= 0:
                print("You have succesfully slain the slime.")
                print("+3 XP, +3 GOLD.")
                exp += 3
                gold += 3
                enemy = "none"
                slime1alive = False
        elif enemy == "slime2" and slime2alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You succesfully attack the slime for" , damage , "damage.")
                slime2hp -= damage
            else:
                print("You attempt to attack, but the slime absorbs your blow.")
            damage = random.randint(-defense, 2)
            if damage > 0:
                print("The slime bounces on you, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The slime bounces on you, but not with enough force to harm.")
            if slime2hp <= 0:
                print("You have succesfully slain the slime.")
                print("+3 XP, +3 GOLD.")
                exp += 3
                gold += 3
                enemy = "none"
                slime2alive = False
                levelup()
        elif enemy == "slime3" and slime3alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You succesfully attack the slime for" , damage , "damage.")
                slime3hp -= damage
            else:
                print("You attempt to attack, but the slime absorbs your blow.")
            damage = random.randint(-defense, 2)
            if damage > 0:
                print("The slime bounces on you, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The slime bounces on you, but not with enough force to harm.")
            if slime3hp <= 0:
                print("You have succesfully slain the slime.")
                print("+3 XP, +3 GOLD.")
                exp += 3
                gold += 3
                enemy = "none"
                slime3alive = False
                levelup()

    elif object == "skeleton":
        if enemy == "skeleton1" and skeleton1alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You succesfully attack the skeleton for" , damage , "damage.")
                skeleton1hp -= damage
            else:
                print("You attempt to attack the skeleton, but it swerves out of the way.")
            damage = random.randint(-defense, 2)
            if damage > 0:
                print("The skeleton swings its sword at you, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The skeleton attempts to swing its sword, but misses.")
            if skeleton1hp <= 0:
                print("The skeleton collapses to the ground, officially dead.")
                print("+4 XP, +4 GOLD.")
                exp += 4
                gold += 4
                enemy = "none"
                skeleton1alive = False
                levelup()
        elif enemy == "skeleton2" and skeleton2alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You succesfully attack the skeleton for" , damage , "damage.")
                skeleton2hp -= damage
            else:
                print("You attempt to attack the skeleton, but it swerves out of the way.")
            damage = random.randint(-defense, 2)
            if damage > 0:
                print("The skeleton swings its sword at you, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The skeleton attempts to swing its sword, but misses.")
            if skeleton2hp <= 0:
                print("The skeleton collapses to the ground, officially dead.")
                print("+4 XP, +4 GOLD.")
                exp += 4
                gold += 4
                enemy = "none"
                skeleton2alive = False
                levelup()
        elif enemy == "skeleton3" and skeleton3alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You succesfully attack the skeleton for" , damage , "damage.")
                skeleton3hp -= damage
            else:
                print("You attempt to attack the skeleton, but it swerves out of the way.")
            damage = random.randint(-defense, 2)
            if damage > 0:
                print("The skeleton swings its sword at you, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The skeleton attempts to swing its sword, but misses.")
            if skeleton3hp <= 0:
                print("The skeleton collapses to the ground, officially dead.")
                print("+4 XP, +4 GOLD.")
                exp += 4
                gold += 4
                enemy = "none"
                skeleton3alive = False
                levelup()
        elif enemy == "topaz" and topazalive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You land an attack on the Topaz Fighter for" , damage , "damage.")
            else:
                print("The topaz clashes with your weapon, nullifying your attack.")
            topazchoose = random.randint(1, 4)
            if topazchoose == 4:
                for i in range(0, 2):
                    damage = random.randint(-defense, 4)
                    if damage > 0:
                        print("The power of the topaz sets you aflame, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
                    else:
                        print("The power of the topaz fails to set you aflame.")
            elif topazchoose == 3:
                damage = random.randint(1, 3)
                print("The Topaz Fighter strikes you quicker than you can react, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 4)
                if damage > 0:
                    print("The Topaz Fighter slashes you with its topaz blade, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The Topaz Fighter tries to slash you with its topaz blade, just to miss.")
            if topazhp <= 0:
                print("The topaz fighter falls to the ground, fading into a pile of topaz powder.")
                print("+10 XP, +9 GOLD.")
                exp += 10
                gold += 9
                enemy = "none"
                topazalive = False
                levelup()

    elif object == "jackalope":
        if enemy == "jack1" and jack1alive == True:
            damage = random.randint(0, attack)
            if damage > 0:
                print("You manage land a hit on the jackalope for" , damage , "damage.")
                jack1hp -= damage
            else:
                print("You swing at the jackalope, but it is too nimble to be hit.")
            damage = random.randint(-defense, 3)
            if damage > 0:
                print("The jackalope rams into you, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The jackalope tries to charge into you, but just runs off to the side.")
            if jack1hp <= 0:
                print("The jackalope is no longer moving frantically, its body limp on the floor.")
                print("+5 XP, +3 GOLD.")
                exp += 5
                gold += 3
                enemy = "none"
                jack1alive = False
                levelup()
        elif enemy == "jack2" and jack2alive == True:
            damage = random.randint(0, attack)
            if damage > 0:
                print("You manage land a hit on the jackalope for" , damage , "damage.")
                jack2hp -= damage
            else:
                print("You swing at the jackalope, but it is too nimble to be hit.")
            damage = random.randint(-defense, 3)
            if damage > 0:
                print("The jackalope rams into you, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                print("The jackalope tries to charge into you, but just runs off to the side.")
            if jack2hp <= 0:
                print("The jackalope is no longer moving frantically, its body limp on the floor.")
                print("+5 XP, +3 GOLD.")
                exp += 5
                gold += 3
                enemy = "none"
                jack2alive = False
                levelup()

    elif object == "amethyst":
        if enemy == "amethyst" and amethystalive == True:
            damage = random.randint(-2, attack)
            if damage > 0:
                print("You manage to dent the amethyst with your weapon for" , damage , "damage.")
                amethysthp -= damage
            else:
                print("You cast your attack upon the amethyst, to no avail.")
            if ame_cb == 1:
                damage = random.randint(-defense, 6)
                if damage > 0:
                    print("A giant amethyst fist crushes you, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("You watch in horror as a giant amethyst fist falls directly beside you.")
                ame_cb = 0
            else:
                amechoose = random.randint(1,3)
                if amechoose == 3:
                    print("The amethyst starts charging energy, as if it wants to make a crushing blow.")
                    ame_cb = 1
                else:
                    damage = random.randint(-defense, 3)
                    if damage > 0:
                        print("An amethyst shard flies into you, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
                    else:
                        print("An amethyst shard flies beside you, failing to hit.")
            if amethysthp <= 0:
                print("The giant amethyst shatters, having been succesfully slain.")
                print("+7 XP, +6 GOLD.")
                exp += 7
                gold += 6
                enemy = "none"
                amethystalive = False
                levelup()

    elif object == "orc":
        if enemy == "orc1" and orc1alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You hit an attack on the ogre for" , damage , "damage.")
                orc1hp -= damage
            else:
                print("You miss your attack upon the ogre.")
            if orc_cb == 1:
                damage = random.randint(-defense, 8)
                if damage > 0:
                    print("The orc slams down fiercly with its club, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The orc slams down fiercly with its club, just to miss to the side.")
            else:
                orc_choose = random.randint(1, 3)
                if orc_choose == 3:
                    print("The orc raises its club, preparing for a crushing blow.")
                    orc_cb == 1
                else:
                    damage = random.randint(1, 4)
                    if damage > 0:
                        print("The orc swings its club at you, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
            if orc1hp <= 0:
                print("The orc falls down to the ground, now dead.")
                print("+8 XP, 6 GOLD.")
                exp += 8
                gold += 6
                orc1alive = False
                orc_cb = 0
                enemy = "none"
                levelup()
        elif enemy == "orc2" and orc2alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You hit an attack on the ogre for" , damage , "damage.")
                orc2hp -= damage
            else:
                print("You miss your attack upon the ogre.")
            if orc_cb == 1:
                damage = random.randint(-defense, 8)
                if damage > 0:
                    print("The orc slams down fiercly with its club, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The orc slams down fiercly with its club, just to miss to the side.")
            else:
                orc_choose = random.randint(1, 3)
                if orc_choose == 3:
                    print("The orc raises its club, preparing for a crushing blow.")
                    orc_cb == 1
                else:
                    damage = random.randint(1, 4)
                    if damage > 0:
                        print("The orc swings its club at you, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
            if orc2hp <= 0:
                print("The orc falls down to the ground, now dead.")
                print("+8 XP, 6 GOLD.")
                exp += 8
                gold += 6
                orc2alive = False
                orc_cb = 0
                enemy = "none"
                levelup()
     
    elif object == "stone":
        if enemy == "stone1" and stone1alive == True:
            damage == random.randint(-2, attack)
            if damage > 0:
                print("You cast your weapon on the stone for" , damage , "damage.")
                stone1hp -= damage
            else:
                print("You try to attack the stone, but the attack is absorbed.")
            damage == random.randint(-defense, 3)
            if damage > 0:
                print("The sentient stone rams into you, dealing" , damage , "damage.")
            if stone1hp <= 0:
                print("The sentient stone shatters into tens of pieces.")
                print("+7 XP, +5 GOLD.")
                exp += 7
                gold += 5
                stone1alive = False
                enemy = "none"
                levelup()
        if enemy == "stone2" and stone2alive == True:
            damage == random.randint(-2, attack)
            if damage > 0:
                print("You cast your weapon on the stone for" , damage , "damage.")
                stone2hp -= damage
            else:
                print("You try to attack the stone, but the attack is absorbed.")
            damage == random.randint(-defense, 3)
            if damage > 0:
                print("The sentient stone rams into you, dealing" , damage , "damage.")
            if stone2hp <= 0:
                print("The sentient stone shatters into tens of pieces.")
                print("+7 XP, +5 GOLD.")
                exp += 7
                gold += 5
                stone2alive = False
                enemy = "none"
                levelup()
        if enemy == "stone3" and stone3alive == True:
            damage == random.randint(-2, attack)
            if damage > 0:
                print("You cast your weapon on the stone for" , damage , "damage.")
                stone3hp -= damage
            else:
                print("You try to attack the stone, but the attack is absorbed.")
            damage == random.randint(-defense, 3)
            if damage > 0:
                print("The sentient stone rams into you, dealing" , damage , "damage.")
            if stone3hp <= 0:
                print("The sentient stone shatters into tens of pieces.")
                print("+7 XP, +5 GOLD.")
                exp += 7
                gold += 5
                stone3alive = False
                enemy = "none"
                levelup()

    elif object == "stalagmite":
        if enemy == "piercer1" and piercer1alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You make a blow at the stalagmite for" , damage , "damage.")
                piercer1hp -= damage
            piercer_choose = random.randint(1, 3)
            if piercer_choose == 3:
                damage = random.randint(-defense, 4)
                print("The stalagmite pierces you before you can react, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 5)
                if damage > 0:
                    print("The stalagmite piercer bonks you on the head, dealing" , damage , "damage.")
                else:
                    print("The stalagmite piercer attempts to bonk you on the head, but ends up missing.")
            if piercer1hp <= 0:
                print("The stalagmite collapses onto the ground, having fallen in battle.")
                print("+7 XP, +5 GOLD.")
                exp += 7
                gold += 5
                piercer1alive = False
                enemy = "none"
                levelup()
        elif enemy == "piercer2" and piercer2alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You make a blow at the stalagmite for" , damage , "damage.")
                piercer2hp -= damage
            piercer_choose = random.randint(1, 3)
            if piercer_choose == 3:
                damage = random.randint(-defense, 4)
                print("The stalagmite pierces you before you can react, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 5)
                if damage > 0:
                    print("The stalagmite piercer bonks you on the head, dealing" , damage , "damage.")
                else:
                    print("The stalagmite piercer attempts to bonk you on the head, but ends up missing.")
            if piercer2hp <= 0:
                print("The stalagmite collapses onto the ground, having fallen in battle.")
                print("+7 XP, +5 GOLD.")
                exp += 7
                gold += 5
                piercer2alive = False
                enemy = "none"
                levelup()

    elif object == "menace":
        if enemy == "menace" and crystalalive == True:
            damage = random.randint(-2, attack)
            if damage > 0:
                print("You attack the Crystal Menace with all your might to deal" , damage , "damage.")
                crystalhp -= damage
            if crystal_cb == 1:
                damage = random.randint(-defense, 8)
                if damage > 0:
                    print("The crystal menace crushes you with its stone leg, dealing" , damage , "damage.")
                else:
                    print("The crystal menace tries to lift its leg to crush you, but doesn't have the strength to.")
            else:
                crystal_choose = random.randint(1, 4)
                if crystal_choose == 4:
                    damage = random.randint(-defense, 4)
                    if damage > 0:
                        damage += 2
                        print("The Crystal Menace channels the power of the earth and deals" , damage , "damage.")
                        current_hp -= damage
                        death()
                    else:
                        print("The Crystal Menace channels the power of the earth, to no avail.")
                elif crystal_choose == 3:
                    print("The Crystal Menace starts lifting its leg, wanting to make a crushing blow.")
                    crystal_cb = 1
                else:
                    damage = random.randint(-defense, 4)
                    if damage > 0:
                        print("The Crystal Menace kicks you with its leg, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
                    else:
                        print("The Crystal Menace attempts to kick you, but is too slow.")
            if crystalhp <= 0:
                print("The Crystal Menace slowly toppes over, for you have conquered the beast.")
                print("+10 XP, +10 GOLD.")
                exp += 10
                gold += 10
                crystalalive = False
                enemy = "none"
                levelup()

    elif object == "ogre":
        if enemy == "ogre" and ogrealive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You land an attack on the ogre for" , damage , "damage.")
                ogrehp -= damage
            else:
                print("You attempt to attack the ogre, but its abs reduce the attack to nothing.")
            if orc_cb == 1:
                damage = random.randint(-defense, 10)
                if damage > 0:
                    print("The Grand Ogre pummels you to the ground, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The orc pummels the ground, as if it thinks its pummelling you.")
            else:
                orc_choose = random.randint(1, 4)
                if orc_choose == 4:
                    print("The orc screams in anger, charging itself for a crushing blow.")
                    orc_cb = 1
                elif orc_choose == 3:
                    damage = random.randint(1, 4)
                    print("The orc strikes you quicker than you can react, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    damage = random.randint(-defense, 5)
                    if damage > 0:
                        print("The orc strikes you with its fist, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
                    else:
                        print("The orc tries to strike you, but you barely duck in time.")
            if ogrehp <= 0:
                print("The ogre falls to the ground, you have succesfully slain it.")
                print("+12 XP, +12 GOLD.")
                exp += 12
                gold += 12
                ogrealive = False
                enemy + "none"
                print("'Well, I'm impressed. You have proven yourself worthy of the camp of heroes. Move on!'")
                camp()

    elif object == "guru":
        if enemy == "guru1" and guru1alive == True:
            damage = random.randint(-2, attack)
            if damage > 0:
                print("The Guru screams once more as you hit it for" , damage , "damage.")
                guru1hp -= damage
            else:
                print("The Mountain Guru lifts its hand and completely blocks the attack.")
            summit_choose = random.randint(1, 4)
            if summit_choose == 4:
                damage = random.randint(-defense, 4)
                if damage > 0:
                    print("The Mountain Guru blasts you with light for" , damage , "damage, before regenerating itself.")
                    current_hp -= damage
                    guru1hp += 5
                    death()
                else:
                    print("The Mountain Guru charges a blast of light, but cannot channel enough energy to do so.")
            elif summit_choose == 3:
                damage = random.randint(1, 3)
                print("The Mountain Guru strikes you with the side its palm quicker than you can react, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 4)
                if damage > 0:
                    print("The Guru slaps you with its bare palm, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The Guru strikes you with its bare palm, but bfailed to generate enough force for harm.")
            if guru1hp <= 0:
                print("The Guru collapses onto the ground with a dying screech.")
                print("+8 XP, +7 GOLD.")
                exp += 8
                gold += 7
                guru1alive = False
                enemy = "none"
                levelup()
        elif enemy == "guru2" and guru2alive == True:
            damage = random.randint(-2, attack)
            if damage > 0:
                print("The Guru screams once more as you hit it for" , damage , "damage.")
                guru2hp -= damage
            else:
                print("The Mountain Guru lifts its hand and completely blocks the attack.")
            summit_choose = random.randint(1, 4)
            if summit_choose == 4:
                damage = random.randint(-defense, 4)
                if damage > 0:
                    print("The Mountain Guru blasts you with light for" , damage , "damage, before regenerating itself.")
                    current_hp -= damage
                    guru2hp += 5
                    death()
                else:
                    print("The Mountain Guru charges a blast of light, but cannot channel enough energy to do so.")
            elif summit_choose == 3:
                damage = random.randint(1, 3)
                print("The Mountain Guru strikes you with the side its palm quicker than you can react, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 4)
                if damage > 0:
                    print("The Guru slaps you with its bare palm, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The Guru strikes you with its bare palm, but bfailed to generate enough force for harm.")
            if guru2hp <= 0:
                print("The Guru collapses onto the ground with a dying screech.")
                print("+8 XP, +7 GOLD.")
                exp += 8
                gold += 7
                guru2alive = False
                enemy = "none"
                levelup()
        elif enemy == "guru3" and guru3alive == True:
            damage = random.randint(-2, attack)
            if damage > 0:
                print("The Guru screams once more as you hit it for" , damage , "damage.")
                guru3hp -= damage
            else:
                print("The Mountain Guru lifts its hand and completely blocks the attack.")
            summit_choose = random.randint(1, 4)
            if summit_choose == 4:
                damage = random.randint(-defense, 4)
                if damage > 0:
                    print("The Mountain Guru blasts you with light for" , damage , "damage, before regenerating itself.")
                    current_hp -= damage
                    guru3hp += 5
                    death()
                else:
                    print("The Mountain Guru charges a blast of light, but cannot channel enough energy to do so.")
            elif summit_choose == 3:
                damage = random.randint(1, 3)
                print("The Mountain Guru strikes you with the side its palm quicker than you can react, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 4)
                if damage > 0:
                    print("The Guru slaps you with its bare palm, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The Guru strikes you with its bare palm, but failed to generate enough force for harm.")
            if guru3hp <= 0:
                print("The Guru collapses onto the ground with a dying screech.")
                print("+8 XP, +7 GOLD.")
                exp += 8
                gold += 7
                guru3alive = False
                enemy = "none"
                levelup()

    elif object == "goatman":
        if enemy == "goat1" and goat1alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You attack the goat as it lets out a cry for" , damage , "damage.")
                goat1hp -= damage
            summit_choose = random.randint(1, 3)
            if summit_choose == 3:
                damage = random.randint(1, 2)
                print("The Goat Man screams violently and unavoidably bursts your eardrums, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 3)
                if damage > 0:
                    print("The Goat Man kicks you with its hoof, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The Goat Man kicks with its hoof, but misses you entirely.")
            if goat1hp <= 0:
                print("The Goat Man falls silent, and then falls limp on the ground.")
                print("+7 XP, +5 GOLD.")
                exp += 7
                gold += 5
                goat1alive = False
                enemy = "none"
                levelup()
        elif enemy == "goat2" and goat2alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You attack the goat as it lets out a cry for" , damage , "damage.")
                goat2hp -= damage
            summit_choose = random.randint(1, 3)
            if summit_choose == 3:
                damage = random.randint(1, 2)
                print("The Goat Man screams violently and unavoidably bursts your eardrums, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 3)
                if damage > 0:
                    print("The Goat Man kicks you with its hoof, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The Goat Man kicks with its hoof, but misses you entirely.")
            if goat2hp <= 0:
                print("The Goat Man falls silent, and then falls limp on the ground.")
                print("+7 XP, +5 GOLD.")
                exp += 7
                gold += 5
                goat2alive = False
                enemy = "none"
                levelup()
        elif enemy == "goat3" and goat3alive == True:
            damage = random.randint(-1, attack)
            if damage > 0:
                print("You attack the goat as it lets out a cry for" , damage , "damage.")
                goat3hp -= damage
            summit_choose = random.randint(1, 3)
            if summit_choose == 3:
                damage = random.randint(1, 2)
                print("The Goat Man screams violently and unavoidably bursts your eardrums, dealing" , damage , "damage.")
                current_hp -= damage
                death()
            else:
                damage = random.randint(-defense, 3)
                if damage > 0:
                    print("The Goat Man kicks you with its hoof, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("The Goat Man kicks with its hoof, but misses you entirely.")
            if goat3hp <= 0:
                print("The Goat Man falls silent, and then falls limp on the ground.")
                print("+7 XP, +5 GOLD.")
                exp += 7
                gold += 5
                goat3alive = False
                enemy = "none"
                levelup()

    elif object == "golem":
        if enemy == "golem1" and golem1alive == True:
            damage = random.randint(-3, attack)
            if damage > 0:
                print("The golem's rocks start to crack as you hit it for" , damage , "damage.")
                golem1hp -= damage
            if summit_cb == 1:
                damage = random.randint(-defense, 8)
                if damage > 0:
                    print("The golem crushes you with the force of a boulder, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                    summit_cb = 0
            else:
                summit_choose = random.randint(1, 3)
                if summit_choose == 3:
                    print("The rocks that make up the golem shake as it prepares for a crushing blow.")
                    summit_cb = 1
                else:
                    damage = random.randint(-defense, 4)
                    if damage > 0:
                        print("An arm of rocks punches you from the side, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
                    else:
                        print("An arm of rocks swings at you from the side, but collapses before it can hit.")
            if golem1hp <= 0:
                print("The rocks making up the golem shatter, now reduced to pebbles, and fall to the ground.")
                print("+9 XP, +8 GOLD.")
                exp += 9
                gold += 8
                golem1alive = False
                enemy = "none"
                levelup()
        elif enemy == "golem2" and golem2alive == True:
            damage = random.randint(-3, attack)
            if damage > 0:
                print("The golem's rocks start to crack as you hit it for" , damage , "damage.")
                golem2hp -= damage
            if summit_cb == 1:
                damage = random.randint(-defense, 8)
                if damage > 0:
                    print("The golem crushes you with the force of a boulder, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                    summit_cb = 0
            else:
                summit_choose = random.randint(1, 3)
                if summit_choose == 3:
                    print("The rocks that make up the golem shake as it prepares for a crushing blow.")
                    summit_cb = 1
                else:
                    damage = random.randint(-defense, 4)
                    if damage > 0:
                        print("An arm of rocks punches you from the side, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
                    else:
                        print("An arm of rocks swings at you from the side, but collapses before it can hit.")
            if golem2hp <= 0:
                print("The rocks making up the golem shatter, now reduced to pebbles, and fall to the ground.")
                print("+9 XP, +8 GOLD.")
                exp += 9
                gold += 8
                golem2alive = False
                enemy = "none"
                levelup()

    elif object == "fragment":
        if enemy == "fragment" and corruptalive == True:
            damage = random.randint (-2, attack)
            if damage > 0:
                print("The corrupt fragment fractures as you hit it, dealing", damage , "damage.")
                corrupthp -= damage
            if summit_cb == 1:
                damage = random.randint (-defense, 10)
                if damage > 0:
                    print("The very land you stand on flings you into the sky, crushing your bones on the ground as you land for" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("As the very land tries to fling you into the sky, you stand your ground.")
            else:
                summit_choose = random.randint(1, 4)
                if summit_choose == 4:
                    print("The corrupt fragment summons an aura of purple energy around it, preparing a crushing blow.")
                    summit_cb = 1
                elif summit_choose == 3:
                    print("The corrupt fragment does not move, but you can feel your insides explode in purple blood, dealing 7 damage.")
                    current_hp -= 7
                    death()
                else:
                    damage = random.randint(-defense, 5)
                    if damage > 0:
                        print("A snowy boulder is hurled at you with a magical force, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
                    else:
                        print("A snowy boulder is hurled to the side of you.")
            if corrupthp <= 0:
                print("The Corrupt Fragment of the land shatters into hundreds of pieces, the purple energy fading away.")
                print("+10 XP, +9 GOLD.")
                exp += 10
                gold += 9
                corruptalive = False
                enemy = "none"
                levelup()
                summit_cb = 0

    elif object == "guardian":
        if enemy == "guardian" and guardianalive == True:
            damage = random.randint(-2, attack)
            if damage > 0:
                print("You clash at The Guardian's armour and wound the man inside for" , damage , "damage.")
                guardianhp -= damage
            if summit_cb == 1:
                damage = random.randint(-defense, 10)
                if damage > 0:
                    print("The Guardian slams down on you with its sword, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    print("As The Guardian slams its sword down on you, you manage to swerve to the side.")
            else:
                summit_choose = random.randint(1, 4)
                if summit_choose == 4:
                    print("The guardian raises its sword, preparing to make a crushing blow.")
                    summit_cb = 1
                elif summit_choose == 3:
                    damage = random.randint(1, 4)
                    print("The Guardian strikes you with its sword, quicker than you can react, dealing" , damage , "damage.")
                    current_hp -= damage
                    death()
                else:
                    damage = random.randint(-defense, 5)
                    if damage > 0:
                        print("The Guardian slashes powerfully at you with its sword, dealing" , damage , "damage.")
                        current_hp -= damage
                        death()
                    else:
                        print("The Guardian lifts its sword to make an attack, but it is too heavy.")
            if guardianhp <= 0:
                print("The guardian kneels down in defeat.")
                print("'Great job, fighter, you have bested me in battle. You may enter The Podium.'")
                print("+ 12XP, + 10GOLD")
                exp += 12
                gold += 10
                guardianalive = False
                enemy = "none"
                summit_cb = 0
                levelup()

    elif object == "gem":
        if enemy == "gem":
            damage = random.randint(-3, attack)
            if damage > 0:
                print("YOUR ATTACK SUCCESFULLY BRUISES THE GEM FOR" , damage , "DAMAGE.")
            else:
                print("YOUR PUNY, MORTAL ATTACK WAS NOT GOOD ENOUGH TO EVEN DENT THE GEM.")
            if summit_cb == 1:
                damage = random.randint(-defense, 12)
                if damage > 0:
                    print("THE GEM FALLS DOWN ON YOU WITH A CRUSHING FORCE, DEALING" , damage , "DAMAGE.")
                    current_hp -= damage
                    death()
                else:
                    print("THE GEM FALLS DOWN BESIDE YOU WITH A CRUSHING FORCE, SHATTERING THE GROUND TO THE SIDE.")
            else:
                summit_choose = random.randint(1, 5)
                if summit_choose == 5:
                    damage = random.randint(-defense, 2)
                    if damage > 0:
                        print("THE GEM CHANNELS ITS DIVINITY UPON YOU, AS THE LIGHT OVERCOMES YOU IN GRAND GLORY.")
                        current_hp -= 20
                        death()
                    else:
                        print("THE GEM CHANNELS ITS DIVINITY, BUT FAILS. YOU HAVE BEEN SPARED.")
                elif summit_choose == 4:
                    damage = random.randint(-defense, 6)
                    if damage > 0:
                        print("THE GEM HARNESSES THE POWER OF LIGHT TO BLIND YOU FOR" , damage , "DAMAGE AND RESTORE ITSELF.")
                        current_hp -= damage
                        gemhp += 5
                        death()
                    else:
                        print("THE GEM CHARGES THE POWER OF LIGHT, TO NO AVAIL.")
                elif summit_choose == 3:
                    for i in range(0, 2):
                        damage = random.randint(-defense, 6)
                        if damage > 0:
                            print("THE GEM HARNESSES THE POWER OF FLAME TO BURN YOU ALIVE, DEALING" , damage , "DAMAGE.")
                            current_hp -= damage
                            death()
                        else:
                            print("THE GEM HARNESSES THE POWER OF FLAME TO BURN TO ALIVE, BUT THE FLAME DOESN'T BURN BRIGHT ENOUGH.")
                elif summit_choose == 2:
                    print("THE GEM STARTS TO LEVITATE ABOVE YOU, PREPARING THE MOST DEVASTATING CRUSHING BLOW OF ALL.")
                    summit_cb = 1
                else:
                    damage = random.randint(-defense, 6)
                    if damage > 0:
                        print("THE GEM SHOOTS A MAGICAL PROJECTILE AT YOU, DEALING" , damage , "DAMAGE.")
                        current_hp -= damage
                        death()
                    else:
                        print("THE GEM SHOOTS A MAGICAL PROJECTILE, YOU WATCH IN FEAR AS IT SHOOTS TO THE SIDE.")
            if gemhp <= 0:
                print("The Gem's colour starts to fade...")
                print("Its sentience has been drained out in battle.")
                print("There it lay, on the podium, now powerless to stop you from grabbing it.")
                print("It's all yours, fighter. You have acquired THE GEM ATOP THE MOUNTAIN!")
                game_over = True

# Interact function
def interact(object):
    global location
    if object == "shop":
        if location == "goldenfalls":
            goldshop()
# Shop functions
def goldshop():
    global gold
    global shop
    global inshop
    shop = "goldenfalls"
    inshop = True
    print("'Hey there, venturer! Interested in my wares?'")
    print("The shopkeeper shows you everything in stock.")
    print("Iron Sword (weapon): 10 gold.")
    print("Potion O' Heals (potion): 5 gold.")
    print("")
    print("Shop guide!")
    print("Buy (item) - If you have the cost to buy an item, acquire it. Use the tag in brackets.")
    print("Exit - exits the shop, allowing you to move freely again.")
def rockshop():
    global gold
    global shop
    global inshop
    shop = "rockilum"
    inshop = True
    print("'Hey there, venturer! Interested in my wares?'")
    print("The shopkeeper shows you everything in stock.")
    print("Dagger Of Mounds (weapon): 20 gold.")
    print("Boar's Hide (armour): 25 gold.")
    print("Bottle O' Heals (potion): 5 gold.")
    print("")
    print("Shop guide!")
    print("Buy (item) - If you have the cost to buy an item, acquire it. Use the tag in brackets.")
    print("Exit - exits the shop, allowing you to move freely again.")
def campshop():
    global gold
    global shop
    global inshop
    shop = "camp"
    inshop = True
    print("'Hey there, venturer! Interested in my wares?'")
    print("The shopkeeper shows you everything in stock.")
    print("Gleaming Shard (weapon): 30 gold.")
    print("Arcane Plate (armour): 25 gold.")
    print("Blessed Bottle O' Heals (potion): 5 gold.")
    print("")
    print("Shop guide!")
    print("Buy (item) - If you have the cost to buy an item, acquire it. Use the tag in brackets.")
    print("Exit - exits the shop, allowing you to move freely again.")

def buy(object):
    global gold
    global shop

def exitshop():
    global inshop
    global shop
    if inshop == True:
        print("'Farewell, wish you luck with your journey!'")
        inshop = False
        shop = "none"
# Death function
def death():
    global current_hp
    global game_over

    if current_hp <=0:
        print("You have died.")
        game_over = True
# Area functions
def goldenfalls():
    global location
    global started
    global current_hp
    global max_hp
    location = "goldenfalls"
    if started == False:
        print("Welcome to the town of Goldenfalls.")
        print("You've overheard talk about a powerful gem atop the nearby treacherous mountain.")
        print("Your goal is to obtain this gem, and achieve glory.")
        started = True
    else:
        print("Welcome back to goldenfalls.")
        if current_hp < max_hp:
            current_hp = max_hp
            print("Returning to the town appears to magically restore your wounds.")
    print("As you look around, you spot a shopkeeper, training dummies, the surrounding cliffs, and the vast meadow to the north.")

def m1():
    global location
    global enemy
    global thief1alive
    location = "m1"
    print("You have wandered into the meadow.")
    if thief1alive == True:
        print("A thief stands here, seemingly wanting to fight.")
        enemy = "thief1"

def m2():
    global location
    location = "m2"
    print("You have wandered into the meadow.")

def m3():
    global location
    global enemy
    global slime1alive
    location = "m3"
    print("You have wandered into the meadow.")
    if slime1alive == True:
        print("A bouncy slime stands in front of you, as if it wants to violently play.")
        enemy = "slime1"

def m4():
    global location
    global slime2alive
    global enemy
    location = "m4"
    print("You have wandered into the meadow.")
    if slime2alive == True:
        print("A bouncy slime stands in front of you, as if it wants to violently play")
        enemy = "slime2"

def m5():
    global location
    global elitethiefalive
    global enemy
    location = "m5"
    print("You have wandered deep into the meadow, the hills infront of you.")
    if elitethiefalive == True:
        print("You see a thief, more shadowy and sinister than the rest, blocking the way ahead.")
        enemy = "elitethief"
    else:
        print("The path to the hills lays unprotected to progress.")

def m6():
    global location
    location = "m6"
    print("You have wandered into the meadow.")

def m7():
    global location
    global thief2alive
    global enemy
    location = "m7"
    print("You have climbed the clifftops of the meadow, Goldenfalls looming below you to the east.")
    if thief2alive == True:
        print("A thief stands here, seemingly wanting to fight.")
        enemy = "thief2"
def m8():
    global location
    global slime3alive
    global enemy
    location = "m8"
    print("You have climbed the clifftops of the meadow, Goldenfalls looming below you to the west.")
    if slime3alive == True:
        print("A bouncy slime stands in front of you, as if it wants to violently play")
        enemy = "slime3"

def rockilum():
    global location
    global current_hp
    global max_hp
    location = "rockilum"
    print("You have made it to the hilltop town of Rockilum, where you spot a shopkeeper and a mystical wizard.")
    print("The looming cavern still lays eastwards.")
    if current_hp < max_hp:
        current_hp = max_hp
        print("The warming presence of the hilltop town magically restores your wounds.")
def h1():
    global location
    location = "h1"
    print("You have made it to the entrance of the hills, a vast land of skeletons and jackalopes.")
    print("To the north, you see a town similar to Goldenfalls. North-east, a cavernous entrance.")
def h2():
    global location
    global enemy
    global skeleton1alive
    location = "h2"
    print("You have wandered into the hilltops.")
    if skeleton1alive == True:
        print("The reanimated skeleton of a fallen soldier nearby makes a brawling stance.")
        enemy = "skeleton1"
def h3():
    global location
    global enemy
    global jack1alive
    location = "h3"
    print("You have wandered into the hilltops.")
    if jack1alive == True:
        print("A prancing jackalope notices you, becoming filled with a sense of anger.")
        enemy = "jack1"
def h4():
    global location
    location = "h4"
    print("You have wandered into the hilltops, and the town is now within your northward reach.")
def h5():
    global location
    global enemy
    global skeleton2alive
    location = "h5"
    print("You have wandered into the hilltops.")
    if skeleton2alive == True:
        print("The reanimated skeleton of a fallen soldier nearby makes a brawling stance.")
        enemy = "skeleton2"
def h6():
    global location
    global enemy
    global amethystalive
    location = "h6"
    print("You have wandered into the hilltops.")
    if amethystalive == True:
        print("A giant living amethyst looks at you with an unhappy glare.")
        enemy = "amethyst"
def h7():
    global location
    global enemy
    global jack2alive
    location = "h7"
    print("You have wandered into the hilltops.")
    if jack2alive == True:
        print("A prancing jackalope notices you, becoming filled with a sense of anger.")
        enemy = "jack2"
def h8():
    global location
    location = "h8"
    print("You have wandered into the hilltops, and the town is now within your westward reach.")
def h9():
    global location
    global enemy
    global skeleton3alive
    location = "h9"
    print("You have wandered into the hilltops.")
    if skeleton3alive == True:
        print("The reanimated skeleton of a fallen soldier nearby makes a brawling stance.")
        enemy = "skeleton3"
def h10():
    global location
    global enemy
    global topazalive
    location = "h10"
    print("You have wandered all the way through the hilltops, the cave entrance now directly east of you.")
    if topazalive == True:
        print("However a skeleton, corrupted and covered in topaz crystals, guards the way ahead.")
        enemy = "topaz"
    else:
        print("You can look into the looming caverns ahead.")

def c1():
    global location
    location = "c1"
    print("You have wandered to the cavern's entrance, crystals and beasts lurking around.")
def c2():
    global location
    global enemy
    global orc1alive
    location = "c2"
    print("You are wandering in the caverns.")
    if orc1alive == True:
        print("A short-tempered orc stands nearby, and catches a glance at you in the dark.")
        enemy = "orc1"
def c3():
    global location
    global enemy
    global piercer1alive
    location = "c3"
    print("You are wandering in the caverns.")
    if piercer1alive == True:
        print("A living stalagmite falls down from the ceiling infront of you, begging for battle.")
        enemy = "piercer1"
def c4():
    global location
    global stone1alive
    global enemy
    location = "c4"
    print("You are wandering in the caverns.")
    if stone1alive == True:
        print("A sentient stone approaches you, and doesn't seem to like your presence.")
        enemy = "stone1"
def c5():
    global location
    location = "c5"
    print("You are wandering in the caverns.")
def c6():
    global location
    global stone2alive
    global enemy
    location = "c6"
    print("You are wandering in the caverns.")
    if stone2alive == True:
        print("A sentient stone approaches you, and doesn't seem to like your presence.")
        enemy = "stone2"
def c7():
    global location
    global orc2alive
    global enemy
    location = "c7"
    print("You are wandering in the caverns.")
    if orc2alive == True:
        print("A short-tempered orc stands nearby, and catches a glance at you in the dark.")
        enemy = "orc2"
def c8():
    global location
    global piercer2alive
    global enemy
    location = "c8"
    print("You are wandering in the caverns.")
    if piercer2alive == True:
        print("A living stalagmite falls down from the ceiling infront of you, begging for battle.")
        enemy = "piercer2"
def c9():
    global location
    global stone3alive
    global enemy
    location = "c9"
    print("You are wandering in the caverns.")
    if stone3alive == True:
        print("A sentient stone approaches you, and doesn't seem to like your presence.")
def c10():
    global location
    global crystalalive
    global enemy
    location = "c10"
    print("You are wandering in the caverns.")
    if crystalalive == True:
        print("A large crystal menace of many valuable gems lurks here.")
        enemy = "menace"
def c11():
    global location
    location = "c11"
    print("You have wandered to the end of the caverns, an exit to a snowy town is here.")

def camp():
    global location
    # Reminder: add Brawler fight after shops
    location = "camp"
    print("You are in the Camp of Heroes, where the strongest of fighters roam.")
    print("Training dummies, a shopkeeper, another wizard, you name it. It's all here atop the mountain.")
def s1():
    global location
    global guru1alive
    global enemy
    location = "s1"
    print("You have ventured onwards into the snowy summit.")
    if guru1alive == True:
        print("An old guru bearing nothing but plain robes and a long beard meditates on a sharp rock, becoming angered when he looks at you.")
        enemy = "guru1"
def s2():
    global location
    location = "s2"
    print("You have ventured onwards into the snowy summit.")
def s3():
    global location
    global goat1alive
    global enemy
    location = "s3"
    print("You have ventured onwards into the snowy summit.")
    if goat1alive == True:
        print("An almost cartoonish goat-human notices you and screams in an uncaringly paranoid manner.")
        enemy = "goat1"
def s4():
    global location
    global goat2alive
    global enemy
    location = "s4"
    print("You have ventured onwards into the snowy summit.")
    if goat2alive == True:
        print("An almost cartoonish goat-human notices you and screams in an uncaringly paranoid manner.")
        enemy = "goat2"
def s5():
    global location
    global guru2alive
    global enemy
    location = "s5"
    print("You have ventured onwards into the snowy summit.")
    if guru2alive == True:
        print("An old guru bearing nothing but plain robes and a long beard meditates on a sharp rock, becoming angered when he looks at you.")
        enemy = "guru2"
def s6():
    global location
    global golem1alive
    global enemy
    location = "s6"
    print("You have ventured onwards into the snowy summit.")
    if golem1alive == True:
        print("A pile of rocks animates into a golem as you approach it.")
        enemy = "golem1"
def s7():
    global location
    location = "s7"
    print("You have ventured onwards into the snowy summit.")
def s8():
    global location
    global corruptalive
    global enemy
    location = "s8"
    print("You have ventured onwards into the snowy summit.")
    if corruptalive == True:
        print("A fragment of the land here has been given life through corrupt energy and levitates menacingly.")
        enemy = "corruptfragment"
def s9():
    global location
    global goat3alive
    global enemy
    location = "s9"
    print("You have ventured onwards into the snowy summit.")
    if goat3alive == True:
        print("An almost cartoonish goat-human notices you and screams in an uncaringly paranoid manner.")
        enemy = "goat3"
def s10():
    global location
    global guru3alive
    global enemy
    location = "s10"
    print("You have ventured onwards into the snowy summit.")
    if guru3alive == True:
        print("An old guru bearing nothing but plain robes and a long beard meditates on a sharp rock, becoming angered when he looks at you.")
        enemy = "guru3"
def s11():
    global location
    global golem2alive
    global enemy
    location = "s11"
    print("You have ventured onwards into the snowy summit.")
    if golem2alive == True:
        print("A pile of rocks animates into a golem as you approach it.")
        enemy = "golem2"
def s12():
    global location
    global guardianalive
    global enemy
    location = "s12"
    print("You are now standing infront of the grand hall containing The Gem's podium.")
    if guardianalive == True:
        print("A large man in sapphire armour blocks the way.")
        print("'For your own safety, I must prevent you from reaching The Podium until you best me in battle.'")
        enemy = "guardian"
def s13():
    global location
    location = "s13"
    print("You've reached the top right corner of the summit.")
    print("Don't exactly know why you're here, this tile is pretty uneventful.")
    print("The Podium's directly to the west, you know?")
def podium():
    global location
    global enemy
    location = "podium"
    print("You have finally made it to the Gem Atop The Mountain.")
    print("It's all yours traveller, interact with it and claim your prize.")

# THE MOVE FUNCTION ALONE.
def move(direction):
    global location
    global enemy

    if enemy == "gem":
        print("AS YOU TRY TO ESCAPE, THE POWER OF THE GEM PULLS YOU BACK. THERE IS NO RUNNING.")
    elif enemy == "ogre":
        print("You scramble around, looking for an escape from the colloseum, to no avail.")
    if inshop == True:
        print("You are currently shopping. Type 'exit' to stop.")
    enemy == "none"
    if location == "goldenfalls":
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
        else:
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

    elif location == "h1":
        if direction == "north":
            h4()
        elif direction == "east":
            h2()
        elif direction == "south":
            m5()
        else:
            print("You cannot move that way.")
    elif location == "h2":
        if direction == "north":
            h5()
        elif direction == "east":
            h3()
        elif direction == "west":
            h1()
        else:
            print("You cannot move that way.")
    elif location == "h3":
        if direction == "north":
            h6()
        elif direction == "west":
            h2()
        else:
            print("You cannot move that way.")
    elif location == "h4":
        if direction == "north":
            rockilum()
        elif direction == "east":
            h5()
        elif direction == "south":
            h1()
        else:
            print("You cannot move that way.")
    elif location == "h5":
        if direction == "north":
            h8()
        elif direction == "east":
            h6()
        elif direction == "west":
            h4()
        elif direction == "south":
            h1()
        else:
            print("You cannot move that way.")
    elif location == "h6":
        if direction == "north":
            h9()
        elif direction == "east":
            h7()
        elif direction == "west":
            h5()
        elif direction == "south":
            h3()
        else:
            print("You cannot move that way.")
    elif location == "h7":
        if direction == "north":
            h10()
        if direction == "west":
            h6()
        else:
            print("You cannot move that way.")
    elif location == "h8":
        if direction == "east":
            h9()
        if direction == "west":
            rockilum()
        if direction == "south":
            h5()
        else:
            print("You cannot move that way.")
    elif location == "h9":
        if direction == "east":
            h10()
        elif direction == "west":
            h8()
        elif direction == "south":
            h6()
        else:
            print("You cannot move that way.")
    elif location == "h10":
        if direction == "west":
            h9()
        elif direction == "south":
            h7()
        elif direction == "east":
            if topazalive == False:
                c1()
            else:
                print("As you try to pass, a giant wall of topaz blocks the entrance, falling down once you step back.")
        else:
            print("You cannot move that way.")
    elif location == "rockilum":
        if direction == "east":
            h8()
        elif direction == "south":
            h4()
        else:
            print("You cannot move that way.")

    elif location == "c1":
        if direction == "east":
            c2()
        elif direction == "west":
            h10()
        elif direction == "south":
            c5()
        else:
            print("You can't move that way.")
    elif location == "c2":
        if direction == "east":
            c3()
        elif direction == "west":
            c1()
        elif direction == "south":
            c6()
        else:
            print("You cannot move that way.")
    elif location == "c3":
        if direction == "east":
            c4()
        elif direction == "west":
            c2()
        else:
            print("You cannot move that way.")
    elif location == "c4":
        if direction == "west":
            c3()
        elif direction == "south":
            c7()
        else:
            print("You cannot move that way.")
    elif location == "c5":
        if direction == "north":
            c1()
        elif direction == "east":
            c6()
        elif direction == "south":
            c8()
        else:
            print("You cannot move that way.")
    elif location == "c6":
        if direction == "north":
            c2()
        elif direction == "west":
            c5()
        elif direction == "south":
            c9()
        else:
            print("You cannot move that way.")
    elif location == "c7":
        if direction == "north":
            c4()
        elif direction == "south":
            c11()
        else:
            print("You cannot move that way.")
    elif location == "c8":
        if direction == "north":
            c5()
        elif direction == "east":
            c9()
        else:
            print("You cannot move that way.")
    elif location == "c9":
        if direction == "north":
            c6()
        elif direction == "east":
            c10()
        elif direction == "west":
            c8()
        else:
            print("You cannot move there.")
    elif location == "c10":
        if direction == "east":
            c11()
        elif direction == "west":
            c9()
    elif location == "c11":
        if direction == "north":
            c7()
        elif direction == "east":
            if ogrealive == False:
                camp()
            else:
                print("You attempt to move to The Summit, when a man blocks your path.")
                print("'Ey, if you think you're worthy of entering our Camp of Heroes, you'll have to prove yourself!'")
                print("You are then escorted to a colloseum, where a giant green beast stands in the center.")
                print("'Your task is simple, defeat The Grand Ogre!'")
                print("The ogre snarls and looks at you with bloodthirst.")
                enemy = "ogre"
        elif direction == "west":
            c10()

    elif location == "camp":
        if direction == "north":
            s3()
        elif direction == "east":
            s1()
        else:
            print("You cannot move that way.")
    elif location == "s1":
        if direction == "north":
            s4()
        elif direction == "east":
            s2()
        elif direction == "west":
            camp()
        else:
            print("You cannot move that way.")
    elif location == "s2":
        if direction == "north":
            s5()
        elif direction == "west":
            s1()
        else:
            print("You cannot move that way.")
    elif location == "s3":
        if direction == "north":
            s7()
        elif direction == "east":
            s4()
        elif direction == "south":
            camp()
        else:
            print("You cannot move that way.")
    elif location == "s4":
        if direction == "north":
            s8()
        elif direction == "east":
            s5()
        elif direction == "west":
            s3()
        elif direction == "south":
            s1()
        else:
            print("You cannot move that way.")
    elif location == "s5":
        if direction == "north":
            s9()
        elif direction == "east":
            s6()
        elif direction == "west":
            s4()
        elif direction == "south":
            s2()
        else:
            print("You cannot move that way.")
    elif location == "s6":
        if direction == "north":
            s10()
        elif direction == "west":
            s5()
        else:
            print("You cannot move that way.")
    elif location == "s7":
        if direction == "east":
            s8()
        elif direction == "south":
            s3()
        else:
            print("You cannot move that way.")
    elif location == "s8":
        if direction == "north":
            s11()
        elif direction == "east":
            s9()
        elif direction == "west":
            s7()
        elif direction == "south":
            s4()
        else:
            print("You cannot move that way.")
    elif location == "s9":
        if direction == "north":
            s12()
        elif direction == "east":
            s10()
        elif direction == "west":
            s8()
        elif direction == "south":
            s5()
        else:
            print("You cannot move that way.")
    elif location == "s10":
        if direction == "north":
            s13()
        elif direction == "west":
            s9()
        elif direction == "south":
            s6()
        else:
            print("You cannot move that way.")
    elif location == "s11":
        if direction == "east":
            s12()
        elif direction == "south":
            s8()
        else:
            print("You cannot move that way.")
    elif location == "s12":
        if direction == "north":
            if guardianalive == False:
                podium()
            else:
                print("The guardian stands in the way still.")
        elif direction == "east":
            s13()
        elif direction == "west":
            s11()
        elif direction == "south":
            s9()
        else:
            print("You cannot move that way.")
    elif location == "s13":
        if direction == "west":
            s12()
        elif direction == "south":
            s10()
        else:
            print("You cannot move that way.")
    elif location == "podium":
        if direction == "south":
            s12()
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
        print("stats - allows you to check your stats.")
        print("interact (person/object) - allows you to potentially talk to someone, or check out something.")
        print("attack (enemy) - allows you to attack a potential threat that's around.")

    if commands[0] == "move":
        move(commands[1])

    if commands[0] == "stats":
        print("You have" , current_hp , "out of" , max_hp , "HP.")
        print("You have" , attack , "attack.")
        print("You have" , defense , "defense.")
        print("You are level", level, "and you have" , exp , "XP.")
        print("You have" , gold , "Gold.")

    if commands[0] == "interact":
        interact(commands[1])

    if commands[0] == "attack":
        fight(commands[1])

    if commands[0] == "exit":
        exitshop()

    if commands[0] == "buy":
        buy(commands[1])