from random import shuffle
rez = dict()

while True:
    choice = input ('Spelejam? y/n\n')
    if choice == 'y':
        players = input('Tavs vards:  ')
        doors = ['dragon', 'water', 'empty']
        lives = 1
        score = 0
        while True:
            choice = int(input('Ievādi durvu numuru (1, 2 vai 3): '))
            shuffle(doors)
            score += 100
            if choice > 3:
                print('Nekas nav noticis.')
                print ('Meginiet velreiz!')
                continue
            if choice < 1:
                print('Nekas nav noticis.')
                print ('Meginiet velreiz!')
                continue
            if doors[choice - 1] == 'dragon':
                print('Jūs cīnījāties ar pūķi un zaudējāt dzīvību.')
                lives -= 1
                print('Tev palika', lives, 'dzīvēs!')

            elif doors[choice - 1] == 'water':
                print('Jūs dzērāt dzīvo ūdeni un ieguvāt dzīvību.')
                lives += 1
                print('Tev tagad ir ', lives, 'dzīvēs!')

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
    

