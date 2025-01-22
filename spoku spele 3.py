print ('Paspelesim')
def start():
    if i == 2:
        count = [0,0]
    elif i == 3:
        count = [0,0,0]
    elif i == 4:
        count = [0,0,0,0]

    from random import randint

    n = int('0')
    while n<i:
        print('Spelētajs nr. %d' %n)
        while True:
            
            choice = input('Start? y/n\n')
            jūtos_drosmīgs = True
            if choice == 'y':
                current = 0
                while jūtos_drosmīgs:
                    spoka_durvis = randint (1,3)
                    print ('Tev priekšā ir trīs durvis...')
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
                    current = current + 1
                    count [n] += current
                    #rezultāts = rezultāts + 1
                    
                    print('Bēdz prom!')
                

                    print('Spēle beigusies. Tu ieguvi', count[n], 'punktus.')

        n+=1
    res = int ('0')
    chemp = int('0')
    n=0
    while n<i:
        if res<count[n]:
            res=count[n]
            chemp = n
            n+=1
    print ('Spēlētajs %d Uzvārja!' %chemp)
    game()


def game():
      choice = input ('Spēlējam atkāl? y/n\n')
      if choice == 'y':
            start ()
      elif choice == 'n':
            print('Spēle beidzas,Uz redzešanos!')


choice = input('Spēlējam? y/n\n')
if choice == 'y':
    choice = input ('Cik spēlētajos? 2,3,4\n')
    if choice == '2':
        i=int('2')
    elif choice == '3':
        i=int('3')
    elif choice == '4':
        i=int('4')
    start()
elif choice == 'n':
    print('Uz priekšu!')
