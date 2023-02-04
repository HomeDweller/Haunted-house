from random import randint
import time

lives = 1
hasNecklace = False
hasRing = False
score = 0
dffclt = input("Please select difficulty: easy, medium, hard ")#Difficulty


if dffclt == "easy":
    print("In front of you there are 6 doors")
    time.sleep(1)
    print("behind one of them hides a ghost")
    time.sleep(1)
    print("you have to guess the door that doesn't have a ghost")
    time.sleep(1)
            
    while lives==1:
        ghost_door = randint(1,6)
        door = int(input("Pick the door "))
        if door == ghost_door:
             print("You're dead lmao")
             lives =0
        else:
             print("It's empty")
             score = score+1
        if score == 5:
            print("You have managed to escape")
            break

            
    time.sleep(2)
    print()
elif dffclt == "medium":
    print("In front of you there are 6 doors")
    time.sleep(1)
    print("behind two of them two ghosts are hiding")
    time.sleep(1)
    print("you have to guess the door that doesn't have a ghost")
    time.sleep(1)
    while lives==1:
        ghost_door1 = randint(1,6)
        ghost_door2 = randint(1,6)
        door = int(input("Pick the door "))
        if door == ghost_door1 or door == ghost_door2 and hasNecklace == False:
            print("You're dead lmao")
            lives =0
        elif hasNecklace == True:
            print("You remain unharmed, but, somehow, necklace dissapears")
            hasNecklace = False
        else:
            print("It's empty")
            score = score+1
             
        if score == 5:
            print("You have found a room with an oddly attractive necklace. You put it on and feel warmth.")
            time.sleep(1)
            print("Anyway, it's time to go")
            time.sleep(1)
            print("You feel safer")
            hasNecklace = True
        if score == 15 and hasNecklace == True:#Necklace ending
            print("You have managed to escape")
            time.sleep(1)
            print("You feel that this necklace brings you luck, so you decided to keep it")
            break
        elif score == 15:#Surving is still pretty cool ending 
            print("You have managed to escape")
        break
elif dffclt == "hard":
    print("In front of you there are 3 doors")
    time.sleep(1)
    print("behind two of them two ghosts are hiding")
    time.sleep(1)
    print("you have to guess the door that doesn't have a ghost")
    time.sleep(1)
    
    while lives==1:
        ghost_door1 = randint(1,3)
        ghost_door2 = randint(1,3)
        door = int(input("Pick the door "))
        if door == ghost_door1 or door == ghost_door2 and hasNecklace == False and hasRing == False:
            print("You're dead lmao")
            lives =0
        elif door == ghost_door1 or door == ghost_door2 and hasNecklace == True:
            print("You remain unharmed, but, somehow, necklace dissapears")
            hasNecklace = False
        elif door == ghost_door1 or door == ghost_door2 and hasRing == True:
             print("You remain unharmed, but, somehow, silver ring dissapears")
             hasRing = False
        else:
            print("It's empty")
            score = score+1             
        if score == 5:
            print("You have found a room with an oddly attractive necklace. You put it on and feel warmth.")
            time.sleep(1)
            print("Anyway, it's time to go")
            time.sleep(1)
            hasNecklace = True
        if score == 15:
            print("You have found a room with a silver ring. You put iy on your finger")
            hasRing = True

           
        if score == 25 and hasNecklace == True and hasRing == True:#Jewelery ending
            print("You have managed to escape")
            time.sleep(1)
            print("You feel that theese accessories bring luck and keep you safe, so you decided to keep them")
            break
        if score == 25 and hasNecklace == True:#Necklace ending
            print("You have managed to escape")
            time.sleep(1)
            print("You feel that this necklace brings you luck, so you decided to keep it")
            break
        if score == 25 and hasRing == True:#Ring ending
            print("You have managed to escape")
            time.sleep(1)
            print("You feel that this ring keeps you safe, so you decided to keep it")
            break
        if score == 25:
            print("You have managed to escape")#Surviving this is the best trophy ending
            break
        
print("youre score is ",score)
