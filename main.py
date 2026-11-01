import os
import time
room = [0, 0]
inventory = []
stay = 0
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def scroll(text, delay=0.0):
    print(end="", flush=True)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def question():
    global cont
    global stay
    global n, e, s, w
    while 1:
        scroll("Where do you go?")
        x = input()
        if x == 'n' and n == True:
            room[1] += 1
            clear_screen()
            stay = 0
            break
        elif x == 's' and s == True:
            room[1] -= 1
            clear_screen()
            stay = 0
            break
        elif x == 'e' and e == True:
            room[0] += 1
            clear_screen()
            stay = 0
            break
        elif x == 'w' and w == True:
            room[0] -= 1
            clear_screen()
            stay = 0
            break
        elif x == 'stay':
            clear_screen()
            stay += 1
            break
        else:
            scroll("Invalid input. Try again!")
watson_pos = [0, 0]
intro = 1
while 1:
    if room == [0, 0]:
        if intro == 0:
            scroll("You are in the middle of a London street. A cafe is north, a grocery store (Little Samson) is south, and to your west and east is the road.")
        elif intro == 1:
            scroll(f"\033[33m'Who are you?'\033[0m")
            time.sleep(1)
            scroll("You've woken up in a street. You don't know who you are, only that your head hurts slightly.")
            scroll("Your clothing seems expensive, but ripped. There's a nametag on it.")
            scroll("You are well-dressed, well-groomed, and you have a watch. Your boots are expensive and your coat is well-made.")
            scroll("There is a brass key, a theatre ticket, and a piece of paper in your pockets.")
            scroll("There's a man standing over you. He has a grand mustache, and his arms are crossed.")
            scroll(f"He frowns. \033[33m'Well, this is a mystery! It's too bad Sherlock's not here, he would instantly know where you're from.'\033[0m")
            scroll(f"His eyes grow sad. \033[33m'He always could instantly solve those things about where you came from.'\033[0m")
            print()
            scroll("You look up. You've heard that name before somewhere.")
            scroll(f"\033[31m'Sherlock Holmes?'\033[0m you ask.")
            scroll(f"His eyes light up. \033[33m'You know him! Ah yes, but of course, all of England knows him.'\033[0m")
            scroll(f"He smiles. \033[33m'Well, I guess you must need help. Come into this cafe here, I shall buy you a drink.'\033[0m")
            scroll(f"\033[33m'So come, follow me!'\033[0m He beckons north.")
            print()
            intro = 0
            watson_pos = [0, 1]
        scroll("Current position: Road")
        scroll("North: Cafe")
        scroll("East: Road")
        scroll("West: Road")
        scroll("South: Little Samson")
        n, e, s, w = True, True, True, True
        question()
    if room == [0, 1]:
        scroll("You are now in a cafe.")
        if watson_pos == [0, 1]:
            scroll("As you enter the cafe and go up the staircase, you realize you have no idea who this man you're following is.")
            scroll(f"You decide to ask him. \033[31m'Excuse me, who are you?'\033[0m")
            scroll(f"He turns around, smiling. \033[33m'Oh, I'm Watson. Dr. John H. Watson!'\033[0m")
            scroll(f"\033[33m'I'm Sherlock Holmes' best friend and confidant, as well as the person who logs his work!'\033[0m")
            scroll(f"\033[33m'But again, who are you?'\033[0m he asks.")
            scroll(f"You shrug helplessly. \033[31m'I don't know,'\033[0m you respond.")
            print()
            scroll(f"Watson stares at you. \033[33m'A true mystery! You are an amnesiac, then - you have lost your memory entirely!'\033[0m")
            scroll(f"He examines you. \033[33m'You appear to have suffered a blow to the head.'\033[0m")
            scroll(f"\033[33m'Well, I suppose I should tell you what I am doing. Holmes is missing,'\033[0m Watson sighs.")
            scroll(f"\033[33m'There is something truly amiss here. I am following a lead on Holmes, and I cannot seem to figure out what happened.'\033[0m")
            scroll(f"\033[33m'I will stay here. When you find Holmes, he will be able to deduce your identity, I am sure of it.'\033[0m")
            scroll(f"Watson explains that Holmes's investigation includes a missing inheritance document, several peculiar letters, and a vanished man.")
            scroll("You sit down at a table and think about it, as Watson orders you some tea.")
            print()
            scroll("You agree to accompany Watson. He looks pleased, and you both sit up, tea in hand.")
            scroll("As you do, a pocket watch falls out of your pocket. You grab it and put it back into your pocket.")
            scroll(f"Watson grabs it back. \033[33m'There's an engraving on this I've never seen before!'\033[0m")
            scroll("You turn it around. Sure enough, an engraving is on the back. You've also never seen it before.")
            scroll(f"Watson looks interested. \033[33m'Do you have any idea what this could be?'\033[0m")
            scroll(f"You shake your head. \033[31m'No idea,'\033[0m you say.")
            scroll("It seems like it could be important, but perhaps not. You throw out the tea. It tastes horrible.")
            scroll("Watson gives you a key.")
            inventory.append('holmes_key')
        scroll("Current position: Cafe")
        scroll("South: Road")
        n, e, s, w = False, False, True, False
        question()
    if room == [0, -1]:
        scroll("You are in Little Samson. There is a cashier, who looks up briefly as you walk in.")
        scroll("Current position: Little Samson")
        scroll("North: Road")
    if room == [1, 0]:
        scroll("You are on a road. To the north is an apartment, to the south is a theatre, to the east is a country inn, and to the west is a road.")
        scroll("Current position: Road")
        scroll("North: Apartment")
        scroll("East: Country Inn")
        scroll("South: Theatre")
        scroll("West: Road")
        n, e, s, w = True, True, True, True
        question()
    if room == [1, 1]:
        if 'holmes_key' in inventory:
            scroll("You are in Holmes's home - 221B Baker Street.")
            scroll("There is a magnifying glass and a collection of labelled specimens that give off an odd feeling of familiarity.")
            scroll("There is a violin case on the floor, but otherwise the apartment is quite neat.")
            print()
            scroll("You pick up the violin case, and you gasp in shock. There is a note on it!")
            scroll("It says that he has left to solve the case, and that afterwards, he will be staying at a country inn to relax if Watson needs him.")
            print()
            scroll("Current position: 221B Baker Street")
            scroll("South: Road")
            n, e, s, w = False, False, True, False
            question()
        else:
            scroll("The door is locked.")
            print()
            roon = (1, 0)
    if room == [1, -1]:
        scroll("The theatre is locked.")
        room == [1, 0]
    if room == [2, 0]:
        scroll("The country inn is small and peaceful. There's a garden with tables to the south, and a man sitting at one of them, eating biscuits and reading his newspaper.")
        scroll("Inside the actual inn itself, to the east, a man, presumably the manager, is sitting at a desk, looking bored. You can't see anyone else inside.")
        print()
        scroll("Current position: Country Inn Entrance")
        scroll("East: Country Inn Building")
        scroll("South: Country Inn Gardens")
        scroll("West: Road")
        n, e, s, w = False, True, True, True
        question()
    if room == [3, 0]:
        scroll("You go inside the inn.")
        scroll("You ask the manager of the inn if someone is staying here by the name of Holmes.")
        scroll("The manager says he can't give you that information, and asks you to leave.")
        scroll("Current position: Country Inn Building")
        scroll("West: Country Inn Entrance")
        n, e, s, w = False, False, False, True
        question()
    if room == [2, -1]:
        scroll(f"You enter the gardens. The man sitting at the table looks up at you, as you approach him. \033[31m'Hello, sorry to disturb you - '\033[0m")
        scroll(f"The man smiles. \033[33m'You're Herbert Taylor.' \033[0mIt's not a question.")
        scroll("Shocked, you step back. \033[31m'How do you know?'\033[0m")
        scroll("The man smiles, and points to the newspaper. It shows that you were walking from a train station, when you fell down, apparently losing your memory.")
        scroll("You know this must be Sherlock Holmes. Not many people could identify you just by looking at a newspaper.")
        scroll("When you say this to him, he looks a bit surprised. 'How do you know me, and where I was?'")
        scroll("You hesitate. Should you tell him that you were with Watson?")
        print()
        scroll("You decide to tell him, to avoid any suspicion. 'I was with Watson. He found me and took me to your apartment. I found your note.'")
        scroll("Holmes smiles, tension gone from his face. 'Ah, Watson. Where is he now?'")
        scroll("You cringe. 'Um... looking around London for you. He didn't want to wait for me looking around the apartment some more.'")
        scroll("Holmes blinks, then laughs. 'He will find me eventually, if he follows the clues well enough. I will stay here, and as for you, I suggest that you leave and find your old family. Take this newspaper and read about yourself - you should be able to figure it out.")
        scroll("You thank Holmes, and after saying goodbye, leave the inn. You smile, knowing that Holmes was safe. Only after you get back to your old family do you realize that you don't know if the case Holmes was working on was solved...")
        print()
        scroll('The End')
        break


    
    if room == [1, 3]:
        print()
        scroll("You and Watson decide the best place to start is Holmes' home - 221B Baker Street.")
        scroll("You walk over, with Watson occasionally asking the occasional question to attempt to trigger your memory.")
        scroll("Nothing works, sadly, and Watson has just given up when you round the corner and see the apartment.")
        scroll("You enter 221B Baker Street and start looking around. You feel oddly comfortable in the room.")
        scroll("A magnifying glass and a collection of labelled specimens gives a feeling of familiarty.")
        print()
        scroll("To follow Watson around London, press 1.")
        scroll("To look further around 221B Baker Street first, press 2.")
        question()
        if cont == 1:
            room = 4
        if cont == 2:
            room = 400
    if room == [3, 0]:
        scroll("Watson says that the place he remembers Holmes going to was the countryside estate.")
        print()
        scroll("As you go there, you examine your possessions more thoroughly.")
        scroll("The brass key appears to fit a small, well-made lock, and it has an address on it, although it's smudged. ")
        scroll("The theatre ticket bears a date from the previous week, and is to the theatre you are in now.. ")
        scroll("The reciept is from a place called Little Samson.")
        scroll("Watson suggests that the key is most likely for your home or office. You delight in the idea that you may have an office.")
        print()
        scroll("Following a clue from Holmes's notes, you follow Watson into the countryside to investigate the missing inheritance document.")
        scroll("The household is quite eccentric.")
        scroll("The butler is forgetful, the housekeeper is suspicious of everyone, and the elderly owner is delighted to have visitors.")
        scroll("While Watson interviews the household, you help the librarian sort a collection of books.")
        scroll("You instinctively arrange them by subject, and then discover that you have placed several books exactly where their owner remembers keeping them years before.")
        scroll("You get a sense of recognition, then it disappears.")
        scroll("You notice that the household's routines have changed, helping discover that the document was accidentally misplaced in one of the library books.")
        scroll("Among the papers, you find a note written by Holmes. His handwriting sparks a memory of working at a desk with someone nearby.")
        scroll("You suspect you have met him before.")
        print()
        scroll("Watson learns from the librarian that Holmes went to a country inn.")
        scroll("As you travel there, fragments of life start coming back: a writing desk, a train journey, someone calling your name.")
        scroll("Watson finds Holmes sitting peacefully in the inn's garden, reading a newspaper and eating biscuits.")
        scroll("Watson is relieved but furious that Holmes has beeen away so long and didn't tell him why. Holmes is bemused, as he's certain he left a note somewhere near his violin.")
        scroll("After Holmes sees you, he asks you a few questions to help you figure out your identity.")
        scroll("Holmes examines you and tells you that you are a young solicitor who had been helping organize papers connected to the original case.")
        scroll("He pulls out a newspaper and shows you the article. Your name is Herbert Taylor. ")
        scroll("You were walking from the train station when you fell and hit your head, losing your memory.")
        scroll(f"He smiles. \033[32'You are perfectly fine, now. And I may have a case that you can help me with later, if needed. Your detective skills are fair, if anything.'\033[0m")
        scroll("Grinning, you say that you'll think about it, but as you walk away, you know that of course you'll say yes.")
        scroll("After all, who doesn't want a chance to work on a case with the great Sherlock Holmes?")
        print()
        scroll("The End")
    if room == [0, 4]:
        scroll("You decide to look further around the apartment first, to see if you can find anything.")
        scroll("Watson insists that there is nothing, but you have to know. Watson sighs and leaves for the rest of London.")
        scroll("A few minutes after Watson leaves, you find a note stuck to Holmes's violin case.")
        scroll("The note gives the address of the country inn.")
        scroll("You decide to go to the address to meet with Holmes.")
        print()
        print()
        scroll("To talk to the manager, press 1.")
        scroll("To go to the man in the garden, press 2.")
        question()
        if cont == 1:
            room = 401
        elif cont == 2:
            room = 402
    if room == [0, 5]:
        scroll("You go inside, and ask the manager if someone is staying here by the name of Holmes. The manager tells you that he can't give you that information.")
        scroll("Frustrated, you go outside. The man is still there. You decide you may as well talk to him.")
        print()
        room = (0, 6)
    if room == (0, 6):
        scroll("You go up to the man in the garden. He looks up at you, and smiles. 'You're Herbert Taylor.' It's not a question.")
    if room == 1001:
        scroll("You decide to try to find out what happened to you.")
        scroll("You look around. You are in the middle of a sidewalk. To your left stands a train station. To your right is the cafe. Ahead is the long road in what you presume to be London, with many shops and buildings.")
        scroll("You look down, and see what are probably your footprints coming from... the train station.")
        scroll("So obviously you came from the train station, right?")
        scroll("To go to the train station, press 1.")
        scroll("To examine yourself and your belongings, press 2.")
        question()
        if cont == 1:
            room == 1002
        elif cont == 2:
            room == 1010
    if room == 1010:
        scroll("You decide to look at yourself and your belongings some more.")
        scroll("You start with the piece of paper. It turns out to be a reciept from a store called Little Samson, although the only items on it are a brand of biscuits you haven't really heard of - Moose Spy Biscuits.")
        scroll("They are quite expensive, as it turns out. You seem to have been very, very well-off.")
        scroll("Next, the theatre ticket. It's to The Merchant of Venice, a Shakespeare play, well-known, although somehow, you remember having mixed feelings about it... it was held one week ago.")
        scroll("Finally, the key, which seems... to have an address on it! It most likely is a home or office key, and you love the idea that you have your own office. The address is smudged, though, and unreadable.")
        scroll("To go to Little Samson, press 1.")
        scroll("To go to the theatre, press 2.")
        question()
        if cont == 1:
            room == 1011
        elif cont == 2:
            room == 1021
    if room == 1021:
        scroll("You visit the theatre. The manager greets you like an old acquaintance, then realizes that you can't remember him, blushing.")
        scroll("As you look around the theatre, you ask if you were ever here before. The manager smiles. 'All the time!'")
        scroll("His smile fades, and he looks a bit worried. 'Do you need to see a doctor? You have amnesia of some sort, that's clear.'")
        scroll("You tell ")
    if room == 10000:
        scroll("You decide to start a new life. By the looks of it, you were rich and maybe a bit greedy - this is a chance to start over.")
        scroll("You go up to a nearby store, Little Samson, and walk in. The cashier looks at you. 'What do you need?' she asks.")
        scroll(f"You consider going back, but you shake off that instinct. \033[31m'Can I get a job, please?'\033[0m")
        print()
        scroll('The End')