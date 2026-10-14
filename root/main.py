import time

def do_hallway():
    print(" WE START OUR VERY INTRESTING STORY AT THE WELL KOWN SWELLVIEW JR HIGH HALLWAY\nAt the lockers. Jasper runs up to you and Charlotte. He whispers 'I saw Henry blow a bubble and transform!' Charlotte shushes him. Henry spots you guys and sprints down the hall!\n")
    while True:
        print("What do you want to do?\n1. Check the History Classroom\n2. Follow Schwoz to the Janitor's Closet\n3. Leave school and go to Henry's Porch\n")
        answer = input("Pick a choice: ")
        if answer == "1":
            return "classroom"
        elif answer == "2":
            return "closet"
        elif answer == "3":
            return "porch"
        else:
            print("Not an option. Pick 1, 2, or 3.\n")

def do_classroom(mirror):
    if mirror == False:
        print("HISTORY CLASSROOM\nEmpty room. Something shiny is on a desk.\nIt's a hand mirror. Could be useful to reflect stuff(hint hint nudge nudge).\nYOU HAVE FOUND A MIRROR! \n")
        mirror = True
    else:
        print("HISTORY CLASSROOM\nEmpty desks. You already took the mirror. Nothing else to do here.\n")

    while True:
        print("1. Go back to the Hallway\n")
        answer = input("Pick a choice: ")
        if answer == "1":
            return "hallway", mirror
        else:
            print("Not an option. Type 1.\n")

def do_closet(laser_device):
    if laser_device == False:
        print("JANITOR'S CLOSET\nSchwoz is messing with a weird machine. He mutters about wiping memories and leaves.\nHe dropped a laser diode on the shelf. You grab it.\n YOU GOT THE LASER REMOTE DEVICE! \n")
        laser_device = True
    else:
        print("JANITOR'S CLOSET\nSchwoz is gone. Smells like bleach. You already grabbed the laser(bruh go away).\n")

    while True:
        print("1. Go back to the Hallway\n")
        answer = input("Pick a choice: ")
        if answer == "1":
            return "hallway", laser_device
        else:
            print("Not an option. Type 1.\n")

def do_porch():
    print("HENRY'S FRONT PORCH\nFront door is cracked open. You can see the Junk and Stuff store down the street.\n")
    while True:
        print("1. Enter the Living Room\n2. Walk down to Junk and Stuff\n3. Go back to School\n")
        answer = input("Pick a choice: ")
        if answer == "1":
            return "living_room"
        elif answer == "2":
            return "junk_and_stuff_store"
        elif answer == "3":
            return "hallway"
        else:
            print("Please pick 1, 2, or 3.\n")

def do_living_room():
    print("LIVING ROOM\nInside the house. Super quiet. Piper isn't even yelling. Gotta figure out how to bypass the store security.\n")
    while True:
        print("1. Sneak into the Kitchen\n2. Sneak upstairs to Henry's Bedroom\n3. Go back outside to the Porch\n")
        answer = input("Pick a choice: ")
        if answer == "1":
            return "kitchen"
        elif answer == "2":
            return "bedroom"
        elif answer == "3":
            return "porch"
        else:
            print("Come on, pick a valid number.\n")

def do_kitchen(bubblegum):
    if bubblegum == False:
        print("KITCHEN\nSearching the cabinets. Found a metallic tube behind the cereal.\nIt's Kid Danger's transformation bubblegum! But there's a voice lock.\nTube says: 'SECURITY QUESTION. SOLVE TO OPEN.'\n")
        math_answer = input("What is 32 * 9 + 3985-0.5? Type answer here: ")
        if math_answer == "4272.5":
            print("Tube clicks open! You grab a what is inside.\n YOU GOT THE BUBBLEGUM! \n")
            bubblegum = True
        else:
            print("BUZZ! Tube locks tight. Come back another time.\n")
    else:
        print("KITCHEN\nAlready took the bubblegum. Kitchen is clear move to another room.\n")

    while True:
        print("1. Go back to the Living Room\n")
        answer = input("Pick a choice: ")
        if answer == "1":
            return "living_room", bubblegum
        else:
            print("Type 1.\n")

def do_bedroom(code_paper, man_cave_code):
    if code_paper == False:
        print(f"HENRY'S BEDROOM\nSuper messy in here. You found a crumpled paper under the bed next to a henrys backpack.\nSchwoz's terrible handwriting says: ""Man Cave Elevator Code: 6767 \n YOU GOT THE SECRET CODE! \n")
        code_paper = True
    else:
        print("HENRY'S BEDROOM\nStill a mess. You already found the code paper.\n")

    while True:
        print("1. Go back to the Living Room\n")
        answer = input("Pick a choice: ")
        if answer == "1":
            return "living_room", code_paper
        else:
            print("Just type 1.\n")

def do_junk_and_stuff_store(bubblegum, laser_device):
    if bubblegum == True and laser_device == True:
        print("JUNK AND STUFF STORE\nSecurity system is on. You chew the gum,blow the bubble, pop a bubble, and your face is disguised!\nYou use the laser to fry the camera. Path to the back elevator is clear!\n")
        while True:
            print("1. Enter the secret Elevator\n2. Go back to the Porch\n")
            answer = input("Pick a choice: ")
            if answer == "1":
                return "elevator"
            elif answer == "2":
                return "porch"
            else:
                print("Not a valid option.\n")
    else:
        print("JUNK AND STUFF STORE\nA red laser grid blocks the back. You need a disguise (Bubblegum) and a grid breaker (Laser) to get past.\n")
        while True:
            print("1. Go back to the Porch to keep searching\n")
            answer = input("Pick a choice: ")
            if answer == "1":
                return "porch"
            else:
                print("Please type 1.\n")

def do_elevator(code_paper, man_cave_code):
    print("SECRET ELEVATOR\nNo regular buttons here. Just a digital keypad asking for 4 digits.\n")
    guess = input("Enter the 4-digit passcode (or type 'back' to leave): ")
    if guess.lower() == "back":
        return "junk_and_stuff_store"
    elif guess == man_cave_code and code_paper == True:
        print("Keypad goes green. ""ACCESS GRANTED."" Elevator drops fast...\n")
        return "man_cave"
    else:
        print(" Keypad flashes red. Go check Henry's room if you don't know it.\n")
        return "junk_and_stuff_store"

def do_man_cave(mirror, memory_wiped):
    print("THE MAN CAVE\nDoors open. Captain Man, Kid Danger, Charlotte, and Schwoz are waiting.\nCaptain Man: ""You know our secret dont you.""""\nSchwoz rolls out a giant machine: ""Time for the memory wipe!""""\n")
    while True:
        print("What are you going to do?\n1. Accept your fate and let them wipe your memory\n2. Pull out the mirror to reflect the memory wipe ray\n")
        answer = input("Pick a choice: ")
        if answer == "1":
            memory_wiped = True
            print("Schwoz shoots the machine.\nYou wake up in your bed. Yesterday is a memory of the past .\nGAME OVER.\n")
            return "end", memory_wiped
        elif answer == "2":
            if mirror == True:
                memory_wiped = False
                print("You pull out the mirror just as Schwoz fires!\nThe beam reflects and hits Captain Man and Schwoz instead! Their memories are wiped!\nYOU WIN! YOUR HAS BEEN MEMORY SAVED!\n")
                return "end", memory_wiped
            else:
                memory_wiped = True
                print("You try to block it but you have nothing to reflect the laser!\nSchwoz fires.  You wake up remembering nothing.\nGAME OVER.\n")
                return "end", memory_wiped
        else:
            print("Come on, pick 1 or 2.\n")

def play():
    state = "hallway"
    laser_device = False
    code_paper = False
    bubblegum = False
    mirror = False
    man_cave_code = "6767"
    memory_wiped = False

    print("WELCOME TO I KNOW YOUR SECRET\nCan you protect your memory?\n")

    while not (state == "end"):
        if state == "hallway":
            state = do_hallway()
        elif state == "classroom":
            state, mirror = do_classroom(mirror)
        elif state == "closet":
            state, laser_device = do_closet(laser_device)
        elif state == "porch":
            state = do_porch()
        elif state == "living_room":
            state = do_living_room()
        elif state == "kitchen":
            state, bubblegum = do_kitchen(bubblegum)
        elif state == "bedroom":
            state, code_paper = do_bedroom(code_paper, man_cave_code)
        elif state == "junk_and_stuff_store":
            state = do_junk_and_stuff_store(bubblegum, laser_device)
        elif state == "elevator":
            state = do_elevator(code_paper, man_cave_code)
        elif state == "man_cave":
            state, memory_wiped = do_man_cave(mirror, memory_wiped)

play()