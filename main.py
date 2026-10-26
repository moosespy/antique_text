import os
import time
room = 1
inventory = []

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
    while 1:
        try:
            x = int(input())
            if x == 1:
                cont = 1
                break
            elif x == 2:
                cont = 2
                break
            else:
                scroll("Invalid input. Try again!")
        except ValueError:
            print("Invalid input. Try again!")

if room == 1:
    scroll("'Who are you?'")
    time.sleep(1)
    scroll("You've woken up in a street. You don't know who you are, only that your head hurts slightly.")
    scroll("Your clothing is expensive")
    scroll("There's a man standing over you. He has a grand mustache, and his arms are crossed.")
    scroll("He frowns. 'Well, this is a mystery! It's too bad Sherlock's not here, he would instantly know where you're from.'")
    scroll("His eyes grow sad. 'He always could instantly solve those things about where you came from.'")
    print()
    scroll("You look up. You've heard that name before somewhere.")
    scroll("'Sherlock Holmes?' you ask.")
    scroll("His eyes light up. 'You know him! Ah yes, but of course, all of England knows him.'")
    scroll("He smiles. 'Well, I guess you must need help. Come into this cafe here, I shall buy you a drink.")
    scroll("'So come, follow me!")
    print()
    scroll("To follow the man, press 1.")
    question()
    if cont == 1:
        room = 2
if room == 2:
    scroll("You follow the man, and he leads you to a nearby cafe.")
    scroll("As you enter the cafe and go up the staircase, you realize you have no idea who this man you're following is.")
    scroll("You decide to ask him. 'Excuse me, who are you?'")
    scroll("He turns around, smiling. 'Oh, I'm Watson. Dr. John H. Watson!")
    scroll("'I'm Sherlock Holmes' best friend and confidant, as well as the person who logs his work!'")
    scroll("'But again, who are you?'")
    scroll("You shrug helplessly. 'I don't know,' you respond.")
    scroll("Watson stares at you. 'A true mystery! You are an amnesiac, then - you have lost your memory entirely!'")
    scroll("'Well, I suppose I should tell you what I am doing. Holmes is missing,' Watson sighs.")
    scroll("'There is something truly amiss here. I am following a lead on Holmes, and I cannot seem to figure out what happened.'")
    scroll("'You should accompany me. When I find Holmes, he will be able to deduce your identity, I am sure of it.'")
    scroll("You sit down at a table and think about it.")
    print()
    scroll("To accompany Watson, press 1.")
    question()
    if cont == 1:
        room = 3
if room == 3:
    scroll("You agree to accompany Watson. He looks pleased, and you both sit up.")
    scroll("As you do, a pocket watch falls out of your pocket. You grab it and put it back into your pocket.")
    scroll("Watson grabs it back. 'There's an engraving on this I've never seen before!'")
    scroll("You turn it around. Sure enough, an engraving is on the back. You've also never seen it before.")
