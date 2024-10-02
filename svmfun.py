import random

places = []
nbOfWords = int(input("Enter Number of Words: "))
nbOfPlayers = int(input("Enter Number of Players: "))

for i in range(nbOfWords):
    places.append(input("Enter Word: "))
    for j in range(20):
        print()

random.shuffle(places)
input("Start Game?")
for i in range(20):
    print()
for j in places:
    spy = random.randint(0, nbOfPlayers-1)
    for i in range(nbOfPlayers):
        if i == spy:
            print("Du bist der Spion, lass dich nicht entdecken!")
            input()
        else:
            print("Du bist ein Spieler, das Wort ist: ", j)
            input()
        for k in range(20):
            print()
        input()
        for k in range(20):
            print()
    print("Round Complete")