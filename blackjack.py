def game():
    durvis = [1,2,3]
    import random
    random.shuffle(durvis)

    print('Поиграем в очко?')
    count = 0

    while True:
        choice = input('Будете брать карту? y/n\n')
        if choice == 'y':
            random.shuffle(durvis)
            current = durvis[1]
            print('Вам попалась карта достоинством %d' %current)
            count += current
            
            if count > 21:
                print('Извините, но вы проиграли')
                break
            elif count == 10:
                print('Поздравляю, вы набрали 21!')
                break
            else:
                print('У вас %d очков.' %count)
        elif choice == 'n':
            print('У вас %d очков и вы закончили игру.' %count)
            break

    print('До новых встреч!')
game()
