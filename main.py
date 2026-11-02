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
    if room == [-2, 0]:
        scroll("You try to enter the estate, but the gate is locked.")
        print()
        room == [-1, 0]
    if room == [-1, 0]:
        scroll("You are on a road. A grand estate is to the west.")
        scroll("Current position: Road")
        scroll("East: Road")
        scroll("West: Estate")
    if room == [0, 0]:
        if intro == 0:
            scroll("You are in the middle of a London street. A cafe is north, a grocery store (Little Samson) is south, and to your west and east is the road.")
        elif intro == 1:
            scroll(f"\033[33m'Who are you?'\033[0m")
            time.sleep(1)
            scroll("You've woken up in a street. You don't know who you are, only that your head hurts slightly.")
            scroll("Your clothing seems expensive, but ripped. There's a nametag on it.")
            scroll("You are well-dressed, well-groomed, and you have a watch. Your boots are expensive and your coat is well-made.")
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
        if room != [0, 1]:
            watson_pos = [1000, 1000]
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
            scroll(f"\033[33m'I will be somewhere else. When you find Holmes, he will be able to deduce your identity, I am sure of it.'\033[0m")
            scroll(f"Watson explains that Holmes's investigation includes a missing inheritance document, several peculiar letters, and a vanished man.")
            scroll("You sit down at a table and think about it, as Watson orders you some tea.")
            print()
            scroll("You agree to accompany Watson. He looks pleased, and you both sit up, tea in hand.")
            scroll("You take a sip, then throw out the tea. It tastes horrible.")
            scroll("Watson gives you a key. He says to go to 221B Baker Street with it.")
            inventory.append('holmes_key')
        else:
            scroll("You decide to sit down and relax. The cafe rings out with conversation, and it's a very nice environment.")
            scroll("In fact, maybe you should look through your pockets and such to see if there are any clues towards yourself.")
            scroll("You find a shopping list, a small brass key, and a theatre ticket.")
            scroll("The shopping list is to Little Samson, and the key has an office number on it. The theatre ticket is for today, to 'The Merchant of Venice'.")
            inventory.append('shoppping_list')
            inventory.append('office_key')
            inventory.append('theatre_ticket')
        scroll("Current position: Cafe")
        scroll("South: Road")
        n, e, s, w = False, False, True, False
        question()
    if room == [0, -1]:
        scroll("You are in Little Samson. There is a cashier, who looks up briefly as you walk in.")
        if 'shopping_list' in inventory:
            scroll("You don't really know what to do now, so you pull out your shopping list and decide to shop for a bit.")
            scroll("You look at it closer. Why are there 10 different flavors of biscuits on here? You really loved them or something...")
            scroll("Either way, you decide to buy them. Maybe there is a reason for these biscuits.")
            scroll("You find the biscuits and buy them. At the cash register, the cashier takes the biscuits and stares at them. \033[33m'You're the second person this week who bought these!'\033[0m")
            scroll("You blink. 'The second person? Who was the first?'")
            scroll("She rolls her eyes. 'That hotel manager, Herbert Taylor. Similar-looking to you, now that I think of it.'")
            scroll("She squints at you. 'Actually... it is you, isn't it. You ran out of biscuits the first time, is that it? I'm not complaining, though, you're the only one that buys these things.'")
            scroll("She hands you back the money, and dazed, you stumble out of the shop.")
            scroll("At least you know who you are now... and that's the important part, you guess...")
            print()
            scroll("The End")
            break
        scroll("Current position: Little Samson")
        scroll("North: Road")
        question()
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
            scroll("You use the key Watson gave you to get into Holmes's home - 221B Baker Street.")
            scroll("There is a magnifying glass and a collection of labelled specimens that you quite like. They remind you of something.")
            scroll("There is a violin case on the floor, but otherwise the apartment is quite neat.")
            print()
            scroll("You pick up the violin case, and you gasp in shock. There is a note on it!")
            scroll("It says that he has left to solve the case, and that afterwards, he will be staying at a country inn to relax if Watson needs him.")
            print()
            inventory.append('holmes_note')
            scroll("Current position: 221B Baker Street")
            scroll("South: Road")
            n, e, s, w = False, False, True, False
            question()
        else:
            scroll("The door is locked.")
            print()
            room = (1, 0)
    if room == [1, -1]:
        scroll("You go up to the theatre.")
        scroll("A woman is collecting tickets, looking bored. \033[33m'Ticket, please,'\033[0m she says.")
        if 'theatre_ticket' in inventory:
            scroll("You hand her the ticket. She accepts it and you go inside the theatre.")
            scroll("Many people seem to recognize you. You smile politely and sit down to watch the show.")
            scroll("After the show, you walk out. A man grabs your arm. \033[33m'Hey, you there. Are you Herbert Taylor?'\033[0m")
            scroll("You stop suddenly and turn around. \033[31m'What did you say?\033[0m")
            scroll("He smiles. 'You are! I'm your uncle! I was so worried about you, you seemed to disappear after that grocery store trip.'")
            scroll("'Anyways, come home with me! I appreciate that you still go to the theatre, very reminiscient of your old life!'")
            scroll("After some more discussion, you go home with the man, content that you have found a family.")
            print()
            scroll("The End")
            break
        else:
            scroll("You walk away, mumbling about not having a ticket.")
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
        if holmes_note in inventory:
            scroll("You go inside the inn.")
            scroll("You ask the manager of the inn if someone is staying here by the name of Holmes.")
            scroll("The manager looks stressed. He says he can't give you that information, and asks you to leave.")
            scroll("He doesn't even look up at you as he sorts through a pile of paperwork, mumbling about a missing key.")
            print()
            if 'office_key' in inventory:
                scroll("You blink, and then realize something. You have an office key, in your pocket. It may be the one he is looking for!")
                scroll("You take out the key. 'Excuse me, do you need this, sir?'")
                scroll("He glances briefly, then looks down. 'Probably not, sorry - wait, is that...'")
                scroll("He looks at you sharply. 'Herbert Taylor! Where did you come from? Didn't you disappear?'")
                scroll("You look at him, surprised. 'Did I know you?'")
                scroll("He looks shocked. 'Do you not remember me? I'm your assistant manager! You're the manager here!'")
                scroll("He smiles suddenly. 'If you are back... maybe that is the key! And I don't have to deal with all this!'")
                scroll("You hold out the key, and he grabs it and goes to a locked door. He opens it easily, sighing with relief. 'Well, this is all your problem now. I'm taking a break.'")
                scroll("He leaves without further conversation, leaving you with a pile of paperwork and an job in an office as something you don't know how to do...")
                print()
                scroll("The End") 
                break
        else:
            scroll("The inn is peaceful inside, with artwork surrounding... everywhere.")
            scroll("THe manager looks stressed, with a pile of paperwork on his desk, mumbling something indecipherable.")
            print()
        scroll("Current position: Country Inn Building")
        scroll("West: Country Inn Entrance")
        n, e, s, w = False, False, False, True
        question()
    if room == [2, -1]:
        if holmes_note in inventory:
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
        else:
            scroll("The gardens are peaceful. You don't want to disturb the man sitting at the table, or anything else for that matter, in fear of disturbing the peace.")
            scroll("Current position: Country Inn Gardens")
            scroll("North: Country Inn Entrance")
            n, e, s, w = True, False, False, False
            question()