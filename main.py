import os
import time
room = 1
inventory = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def scroll(text, delay=0.02):
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
    scroll("There is a brass key, a theatre ticket, and a piece of paper in your pockets.")
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
    scroll("To find answers on your own, press 2.")
    question()
    if cont == 1:
        room = 2
    elif cont == 2:
        room = 1000
if room == 2:
    scroll("You follow the man, and he leads you to a nearby cafe.")
    scroll("As you enter the cafe and go up the staircase, you realize you have no idea who this man you're following is.")
    scroll("You decide to ask him. 'Excuse me, who are you?'")
    scroll("He turns around, smiling. 'Oh, I'm Watson. Dr. John H. Watson!")
    scroll("'I'm Sherlock Holmes' best friend and confidant, as well as the person who logs his work!'")
    scroll("'But again, who are you?' he asks.")
    scroll("You shrug helplessly. 'I don't know,' you respond.")
    print()
    scroll("Watson stares at you. 'A true mystery! You are an amnesiac, then - you have lost your memory entirely!'")
    scroll("He examines you. 'You appear to have suffered a blow to the head.'")
    scroll("'Well, I suppose I should tell you what I am doing. Holmes is missing,' Watson sighs.")
    scroll("'There is something truly amiss here. I am following a lead on Holmes, and I cannot seem to figure out what happened.'")
    scroll("'You should accompany me. When I find Holmes, he will be able to deduce your identity, I am sure of it.'")
    scroll("You sit down at a table and think about it, as Watson orders you some tea.")
    print()
    scroll("To accompany Watson, press 1.")
    scroll("To try to find answers on your own, press 2.")
    question()
    if cont == 1:
        room = 3
    elif cont == 2:
        room = 1000
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
    scroll("A magnifying glass and a collection of labelled specimens gives a feeling of familiarty.")
    print()
    scroll("Watson explains that Holmes's investigation includes a missing inheritance document, several peculiar letters, and a vanished man.")
    scroll("You offer your help to Watson, since you have nothing better to do, and out of gratitude.")
    scroll("You begin to hope that you may be a detective yourself.")
    scroll("To follow Watson around London, press 1.")
    scroll("To look further around 221B Baker Street first, press 2.")
    question()
    if cont == 1:
        room = 4
    if cont == 2:
        room = 400
if room == 4:
    scroll("Watson says that the places he remembers Holmes going to were a gentlemen's club.")
    scroll("You discover, as you go to these places, that you are surprisingly good at noticing things.")
    scroll("You can tell which customers have been waiting longest, which shopkeepers are distracted, and other small details.")
    scroll("Unfortunately, you still can't remember your own name.")
    print()
    scroll("At the gentlemen's club, you are mistaken for an expected guest and ushered into a private dining room.")
    scroll("Three elderly gentlemen come up to you and discuss horse racing.")
    scroll("You seem to be well-respected, although no one else seems to notice that you yourself cannot remember things.")
    scroll("You begin to suspect that you may have visited places like this frequently.")
    print()
    scroll("You visit a theatre mentioned in Holmes's notes. The manager greets you like an old acquaintance, then realizes you don't remember him.")
    scroll("An actress remembers that you had once helped recover a necklace that she had lost.")
    scroll("This delights you, as this means that your former identity was useful.")
    scroll("The actress also recalls that Holmes had been asking questions about a missing document and a country house.")
    scroll("She remarks that you was once very particular about the arrangement of books and papers.")
    scroll("Watson looks at you with renewed interest. Apparently you were an intellectual!")
    print()
    scroll("You examine your possessions more thoroughly.")
    scroll("The brass key appears to fit a small, well-made lock, and it has an address on it! The theatre ticket bears a date from the previous week, and is to the theatre you are in now.. The reciept is from a place called Little Samson.")
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
    scroll("He smiles. 'You are perfectly fine, now. And I may have a case that you can help me with later, if needed. Your detective skills are fair, if anything.")
    scroll("Grinning, you say that you'll think about it, but as you walk away, you know that of course you'll say yes.")
    scroll("After all, who doesn't want a chance to work on a case with the great Sherlock Holmes?")
    print()
    scroll("The End")
if room == 1000:
    scroll("Politely, you turn him down on his offer, and walk away. He looks a bit surprised but allows you to leave without question.")
    scroll("As you walk away, you now have to decide what to do.")
    scroll("You have a few choices.")
    scroll("To try to find out what happened to you, press 1.")
    scroll("To start a new life, press 2.")
    question()
    if cont == 1:
        room = 1001
    elif cont == 2:
        room = 10000
if room == 400:
    scroll("You decide to look further around the apartment first, to see if you can find anything.")
    scroll("Watson insists that there is nothing, but you have to know. Watson sighs and leaves for the rest of London.")
    scroll("A few minutes after Watson leaves, you find a note stuck to Holmes's violin case.")
    scroll("It says that he has left to solve the case, and tthat afterwards, he will be staying at a country inn to relax if Watson needs him.")
    scroll("The note gives the address of the country inn.")
    scroll("You decide to go to the address to meet with Holmes.")
    print()
    scroll("The country inn is small and peaceful. There's a garden with tables, and a man sitting at one of them, eating biscuits and reading his newspaper.")
    scroll("Inside the inn, a man, presumably the manager, is sitting at a desk, looking bored. You can't see anyone else inside.")
    print()
    scroll("To talk to the manager, press 1.")
    scroll("To go to the man in the garden, press 2.")
    question()
    if cont == 1:
        room = 401
    elif cont == 2:
        room = 402
if room == 401:
    scroll("You go inside, and ask the manager if someone is staying here by the name of Holmes. The manager tells you that he can't give you that information.")
    scroll("Frustrated, you go outside. The man is still there. You decide you may as well talk to him.")
    print()
    room = 402
if room == 402:
    scroll("You go up to the man in the garden. He looks up at you, and smiles. 'You're Herbert Taylor.' It's not a question.")
    scroll("Shocked, you step back. 'How do you know?'")
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
    scroll("Finally, the key")
if room == 10000:
    scroll("You decide to start a new life. By the looks of it, you were rich and maybe a bit greedy - this is a chance to start over.")
    scroll("You go up to a nearby store, Little Samson, and walk in. The cashier looks at you. 'What do you need?' she asks.")
    scroll("You consider going back, but you shake off that instinct. 'Can I get a job, please?'")
    print()
    scroll('The End')