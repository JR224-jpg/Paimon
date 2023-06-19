# Chapter 1
import random

def Paimon():
    global npcName
    global response
    responses = ["Hi", "Are you hurt?", "Are you from this region?"]
    npcNameChoices = ["LILSKRA", "Juan", "Kate", "Roxy"]
    shuffle(npcNameChoices)
    npcName = npcNameChoice[0]
    print( npcName, ":] Hello, I am", npcName, " , Would you be able to help me out?")
    shuffle(responses)
    answer = input("Press j to talk to Paimon: ")
    if answer == "j":
        print(npcName, ":] ", responses[0])
    else:
        print(npcName, ":] Goodbye")
    return npcName

npcName= ''
responses= ''
Paimon()

#Chapter 2
def Dragon():
    outcomes= ['Win', 'Lose', 'Still Fighting..']
    print("\nlt you have encountered the Dragon, get ready to fight... Let's see what the outcomes is...")
    sleep(1) # Pause for a second
    return outcomes[randit(0,2)]

Ride == False

while Ride == False:
    result = Dragon()
    print(result)
    if result == 'Win':
        Ride = True
        print("You got a free ride to the next chapter!")


# Chapter 3

def DragonRide():
    global npcName
    global response
    reponses = [ "Why was I in a cave?, I was waiting for you...", "Who put me under a spell?, the evil organization named the 'Fatui'", "Have I seen you're lost twin sister?, sorry I have not"]
    npcNameChoices = ("LILSKRA", "Juan", "Kate", "Roxy")
    shuffle(npcNameChoice)
    npcName = npcNameChoice[0]
    print( npcName, ":] Hey let me introduce myslef, my name is" , npcName, ", could I ask you a couple of questions about this world and someone important to me?")
    shuffle(responses)
    answer = input("Press j to talk to the Dragon: ")
if answer == "j":
    print(npcName, ":]", responses[0])
else:
    print(npcName, ":] Silence!!!")
    return npcName

npcName = ''
response = ''
DragonRide()

# Chapter 4

def Fatui():
    outcomes = ['Win', 'Lose', 'Still Fighting...']
    print('\nlt You have encounter a member of the evil organization named the "Fatui", get ready to fight... Let\'s see what the outcome is..')
    sleep(1)
    return outcomes[randint(0,2)]

vision

while vision == False:
    result = Fatui()
    print(result)
    if result == 'win':
        vision = True
        print("The Fatui member has offered to give you a vison for you're victory...a vison about you're lost twin sister!")

# Chapter 5

def TaskAction():
    rest = False
    walk = False
    while 1:
        choice = int(input("What would you like to do? n1. Get some rest n2. Walk around n3. Move on to explore a new region. Enter your choice (1, 2 or 3): "))
        if choice == 1 and rest == False:
            print('You got some food and sleep')
            rest = True
        elif choice == 1 and rest == True:
            print("You already got some food and sleep, go on and explore adventurer!")
        elif choice == 2 and walk == False:
            print("You are all rest up. Walk around to clear youre head after the fight")
        elif choice == 2 and rest == True and walk == False:
            print("You have walked enough, stamina will run out!")
            walk = True
        elif choice == 2 and walk == True:
            print("You are all rest up and have a clear mind.. You are ready to explore...")
        elif choice == 3 and walk == True:
            print("You are all clear, go explore traveler!")
            break
        elif choice == 3 and rest == False:
            print("You need some food and sleep in order to explore the new region!")
        else:
            print("Sorry invalid input, please try again!")
