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
rez = dict()

while True:
    choice = input ('Spelejam? y/n\n')
    if choice == 'y':
        players = input('Tavs vards:  ')
        doors = ['dragon', 'water', 'empty']
        lives = 3
        score = 0
        while True:
            choice = int(input('Ievādi durvu numuru (1, 2 vai 3): '))
            shuffle(doors)
            score += 100
            if choice > 3:
                print ('Meginiet velreiz!')
                continue
            if choice < 0:
                continue
            if doors[choice - 1] == 'dragon':
                print('Jūs cīnījāties ar pūķi un zaudējāt dzīvību.')
                lives -= 1
                print('Tev palika', lives, 'dzīvēs!')

#            elif doors[choice - 1] == 'water':
#                print('Jūs dērāt dzīvo ūdeni un ieguvāt dzīvību.')
#                lives += 1 

            else:
                print('Nekas nav noticis.')
            if lives == 0:
                rez[players]=score
                for key in rez:
                    print (key,rez[key])
                break

    if choice == 'n':
        print('Speles rezultati:')
        for key in rez:
                print(key,'nopelnija', rez[key], 'punktus')
        break
    
