# Spoku spele
from random import randint
print ('Spoku spēle')
jūtos_drosmīgs = 3
rezultāts = 0
while jūtos_drosmīgs > 0:
    spoka_durvis = randint (1,3)
    print ('Tev priekšā ir trīs durvis...')
    print ('Āiz vienām ir spoks.')
    durvju_num = int(input('1,2 vai 3?'))
    
    if durvju_num == spoka_durvis:
        print('SPOKS!')
        jūtos_drosmīgs -= 1
        print(f"Tev palikā {jūtos_drosmīgs} dzīves")
    else:
        print('Spoka nav!')
        print('Tu vari ienākt nākamajā istabā.')
        rezultāts += 1

print('Bēdz prom!')
print(f'Spēle beigusies. Tu ieguvi {rezultāts} punktus.')