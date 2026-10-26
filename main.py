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
                clear_screen()
                break
            elif x == 2:
                cont = 2
                clear_screen()
                break
            else:
                scroll("Invalid input. Try again!")
        except ValueError:
            print("Invalid input. Try again!")

if room == 1:
    scroll("'Who are you?'")
    time.sleep(1)
    scroll("You've woken up in a street. You don't know who you are, only that your head hurts slightly.")
    scroll("Your clothing seems expensive, but ripped. There's a nametag on it.")
    scroll("You are well-dressed, well-groomed, and you have a watch. Your boots are expensive and your coat is well-made.")
    scroll("There is a brass key, a theatre ticket, and a shopping list in your pockets. The list has absurdly expensive biscuits on it. ")
    scroll("Evidently, you are someone of excellent taste.")
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
    scroll("He examines you. 'You appear to have suffered a blow to the head.'")
    scroll("'Well, I suppose I should tell you what I am doing. Holmes is missing,' Watson sighs.")
    scroll("'There is something truly amiss here. I am following a lead on Holmes, and I cannot seem to figure out what happened.'")
    scroll("'You should accompany me. When I find Holmes, he will be able to deduce your identity, I am sure of it.'")
    scroll("You sit down at a table and think about it, as Watson orders you some tea.")
    print()
    scroll("To accompany Watson, press 1.")
    question()
    if cont == 1:
        room = 3
if room == 3:
    scroll("You agree to accompany Watson. He looks pleased, and you both sit up, tea in hand.")
    scroll("As you do, a pocket watch falls out of your pocket. You grab it and put it back into your pocket.")
    scroll("Watson grabs it back. 'There's an engraving on this I've never seen before!'")
    scroll("You turn it around. Sure enough, an engraving is on the back. You've also never seen it before.")
    scroll("Watson looks interested. 'Do you have any idea what this could be?'")
    scroll("You shake your head. 'No idea,' you say.")
    scroll("It seems like it could be important, but perhaps not. You follow Watson out of the cafe, throwing out the tea. It tastes horrible.")
    print()
    scroll("You and Watson decide the best place to start is Holmes' home - 221B Baker Street.")
    scroll("You walk over, with Watson occasionally asking the occasional question to attempt to trigger your memory.")
    scroll("Nothing works, sadly, and Watson has just given up when you round the corner and see the apartment.")
    scroll("You enter 221B Baker Street and start looking around. You feel oddly comfortable in the room.")
    scroll("A magnifying glass")
    scroll("Nothing pops out, until Watson shouts 'A-ha!'")
    scroll("You turn around and see Watson holding a book. The book itself is nothing special - it's about certain legal cases - but there is a note inside of it.")
    scroll("Watson takes the note out and reads: 'The records are incomplete. Ask the former secretary what became of the original.'")
    scroll("This doesn't mean much to you, but Watson is excited.")
    scroll("He explains that Holmes had recently been investigating an old collection of legal documents of some sort.")
    scroll("What's curious is that you actually seem to recognize Holmes' handwriting. You guess that you must have seen it around when in his study and you are already used to it.")
    print()
    scroll("Watson smiles. 'Shall we go to a public records office, then? That will allow us to find what records Holmes was looking for.'")
    scroll("'Or shall we keep looking for clues here?'")
    print()
    scroll("To go to a public records office, press 1.")
    question()
    if cont == 1:
        room = 4
if room == 4:
    scroll("You decide to walk to a public records office. There should be clues there about the records.")
    scroll("At the office, you locate an old register. It lists the people who handled the documents Holmes was investigating.")
    scroll("Several names have been recorded, but one of the entries appears to be crossed out.")
    scroll("Beside it is a note - 'Resigned unexpectedly. Papers transferred to London.'")
    scroll("After examining the entry, you realize that the handwriting of the name resembles the writing of the nametag on your clothing.")
    scroll("After you tell Watson, he looks impressed. 'You know, you're not too bad of a detective youself.'")
    scroll("You wonder if you have ever met Holmes before, or even worked with him.")
    scroll("You return back to 221B Baker Street, something amiss in your mind.")
    print()
    scroll("After returning, Mrs. Hudson, the landlady of 221B Baker Street, runs up to Watson.")
    scroll("'Watson!' she gasps. 'I might have a clue for you!'")
    scroll("Watson sits up. 'What is it?' he asks excitedly.")
    scroll("'Remember when Holmes visited a stationer's shop a few days before he disappeared?' asks Mrs. Hudson.")
    scroll("'Yes, I remember now! I had forgotten about that!' Watson exclaims. 'So what about it?'")
    scroll("'Well, the shopkeeper still has the order book from that week. You should go there to check!")
    scroll("Before Mrs. Hudson finishes her sentence, Watson is already rushing off to the stationer's shop, pulling you along.")
    print()
    scroll("To get more information from Mrs. Hudson, press 2.")
    question()
    if cont == 2:
        room = 5
if room == 5:
    scroll("'Wait!' you cry at Watson. To Mrs. Hudson, you say, 'Is there anything else?'")
    scroll("'Why yes!' she beams. 'I also have a letter from him here. He sent it, but it was returned to the original address, which happened to get to me!'")
    scroll("You take the letter. It's addressed to someone named Herbert Taylor.")
    scroll("You pocket the letter. 'Anything else?'")
    scroll("Mrs. Hudson blinks. 'You want more? I can try to remember, but I don't know right now.'")
    scroll("You thank her and race after Watson.")
    print()
    room = 6
if room == 6:
    scroll("As you catch up to Watson, he's panting, and pointing at the building in front of you.")
    scroll("'That's the stationer's,' he says. 'Maybe you go in first... I'm a bit tired.'")
    scroll("You walk in, and immediately you get the sensation that you've been here.")
    scroll("That sensation is immediately amplified by the fact that there is an engraving on a piece of paper - the same one on your watch!")
    
#notes: r