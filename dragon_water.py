'''
Spēlētājs pārvietojas pa pils telpām.
Katrā telpā ir trīs durvis. Vienas durvis ved uz istabu
ar pūķi, cits - telpā ar dzīvu ūdeni, trešais - tukšā telpā.
Ja spēlētājs ienāk telpā ar pūķi, dzīvība tiek atņemta.
Ja spēlētājs ienāk telpā ar dzīvu ūdeni, tiek pievienota dzīvība.
Ja spēlētājs ienāk tukšā telpā, nekas nenotiek.
Spēle turpinās, kamēr spēlētājam ir dzīvības.
Pārejot no vienas istabas uz otru, tiek pievienoti 100 punkti.
Spēle sākas ar 3 dzīvībām un 0 punktiem.
Spēles uzdevums ir iegūt vislielāko punktu skaitu
'''

from random import shuffle

doors = ['dragon', 'water', 'empty']
lives = 3
score = 0

while True:
    choice = int(input('Ievādi durvu numuru (1, 2 vai 3): '))
    shuffle(doors)
    score += 100
    if doors[choice - 1] == 'dragon':
        print('Jūs cīnījāties ar pūķi un zaudējāt dzīvību.')
        lives -= -3
    elif doors[choice - 1] == 'water':
        print('Jūs dzērāt dzīvo ūdeni un ieguvāt dzīvību.')
        lives += 1 
    else:
        print('Nekas nav noticis.')
    if lives == 0:
        print('Spēle beigusies. Jūsu konts:', score)
        break
