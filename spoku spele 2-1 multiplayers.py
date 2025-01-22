#Spoku spele
import time
from random import randint
choice = input('Start? y/n\n')
jūtos_drosmīgs = True
if choice == 'y':
    # Spēlē ar 1 spēlētaju
    players1 = input('Tavs vards:  ')    
    rezultāts1 = 0
    #time.sleep(1)
    while jūtos_drosmīgs:
        spoka_durvis = randint (1,3)
        print (players1,'Tev priekšā ir trīs durvis...')
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
        rezultāts1 = rezultāts1 + 1  
   
    print('Spēle beigusies. Tu,', players1,', ieguvi', rezultāts1, 'punktus.')

     # Spēlē ar 2 spēlētaju
    print('Nakamais spēlētajs')
    players2 = input ('Tavs vards: ')
    #time.sleep(1)
    jūtos_drosmīgs = True
    rezultāts2 = 0    
    while jūtos_drosmīgs:
        spoka_durvis = randint (1,3)
        print (players2, 'Tev priekšā ir trīs durvis...')
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
        rezultāts2 = rezultāts2 + 1
    print('Spēle beigusies. Tu,', players2,', ieguvi', rezultāts2, 'punktus.')

    
else: print ('Spēle beigusies')

print ('Dalibnieku rezultati:')
rez = dict()
rez[players1]=rezultāts1
rez[players2]=rezultāts2

for key in rez:
    print(key, rez[key])
time.sleep(1)
if rezultāts1 > rezultāts2:
    print('Uzvareja', players1)

elif rezultāts1 == rezultāts2:
    print('NEIZŠĶIRTS')
else:
    print('Uzvareja', players2)

    
 
