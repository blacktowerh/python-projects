

#print(Players[0])

from random import choice

Players = []
file = open('C:\Users\Harry Torrenegra\PycharmProjects\python-projects\players.txt', 'r')
#print(playerA)

teamA = []
teamB = []

while len(Players) > 0:
    playerA = choice(Players)

    teamA.append(playerA)
    Players.remove(playerA)

    playerB = choice(Players)

    teamB.append(playerB)
    Players.remove(playerB)

    #print("Players left: ", Players)

print("Team A: ", teamA)
print("Team B: ", teamB)


