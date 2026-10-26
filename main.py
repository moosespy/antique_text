import os
import time
room = 0
inventory = []

def scroll(text, delay=0.02):
    print(end="", flush=True)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def question(txt):
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
    scroll("There's a man standing over you. He has a grand mustache, and his arms are crossed.")
    scroll("He frowns. 'Well, this is a mystery! It's too bad Sherlock's not here, he would instantly know where you're from.'")
    scroll("His eyes grow sad. 'He always could instantly solve those things about where you came from.'")
    print()
    scroll("You look up. You've heard that name before somewhere.")
    scroll("'Sherlock Holmes?' you ask.")
    scroll("His eyes light up. 'You know him! Ah yes, but of course, all of England knows him.'")
    scroll("He smiles. 'Well, I have nothing to do, and you look like in need of Sherlock Holmes!")
    scroll("'So come, follow me. We must go on a search for Sherlock Holmes!")
    print()
    scroll("To follow the man, press 1.")
    question()
    if cont == 1:
        room == 2
if room == 2:
    scroll("You follow the man, and he leads you to an apartment: 221B Baker Street.")
    scroll("As you enter the apartment and go up the staircase, you realize you have no idea who this man you're following is.")
    scroll("You decide to ask him. 'Excuse me, who are you?'")
    scroll("He turns around, smiling. 'Oh, I'm Watson. Dr. John H. Watson!")
    scroll("'I'm Sherlock Holmes' best friend and confidant, as well as the person who logs his work!'")
    scroll("'But again, who are you?'")
    scroll("You shrug helplessly. 'I don't know,' you respond.")