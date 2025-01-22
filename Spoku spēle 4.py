# Spoku spele
from random import randint
print ('Spoku spēle')
jūtos_drosmīgs = True
rezultāts = 0
while jūtos_drosmīgs:
    spoka_durvis = randint (1,3)
    print ('Tev priekšā ir trīs durvis...')
    print ('Āiz vienām ir spoks.')
    durvis = input('1,2 vai 3?')
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
print('Bēdz prom!')
print('Spēle beigusies. Tu ieguvi', rezultāts, 'punktus.')

