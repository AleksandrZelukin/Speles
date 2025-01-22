#Spoku spele
import time
from random import randint
rez = dict()


while True:
    choice = input ('Spelejam? y/n\n')
    if choice == 'y':
        players = input('Tavs vards:  ')    
        rezultāts = 0
        jūtos_drosmīgs = True
        while jūtos_drosmīgs:
            spoka_durvis = randint (1,3)
            print (players,', Tev priekšā ir trīs durvis...')
            print ('Āiz vienām ir spoks.')
            durvis = input('1,2 vai 3?\n')
            durvju_num = int(durvis)
            if durvju_num == spoka_durvis:
                print('SPOKS!')
                jūtos_drosmīgs = False
            elif durvju_num > 3:
                print ('Neparezi durvju numurs, mēģini velreiz')
            elif durvju_num == 0:
                jūtos_drosmīgs = False
            else:
                print('Spoka nav!')
                print('Tu vari ienākt nākamajā istabā.')
            rezultāts = rezultāts + 1
            rez[players]=rezultāts
            
    if choice == 'n':
        
        print('Speles rezultati:')
        
        for key in rez:
            print(key,'nopelnija', rez[key], 'punktus')
        break
