import random

while True:
    f = input("Spelejam? y/n\n")
    if f == "y":
        ver = 0
        while (ver == 0):
            player = int(input("1 - камень, 2 - ножницы, 3 - бумага. \n"))
            if (player == 1 or player == 2 or player == 3):
                ver = 1    
        if player == 1:
                print("Вы выбрали камень.")  
        if player == 2:
                print("Вы выбрали ножницы.") 
        if player == 3:
                print("Вы выбрали бумагу.")  
        comp = random.randint(1, 3)
        if comp == 1:
                print("Компьютер выбрал камень.") 
        if comp == 2:
                print("Компьютер выбрал ножницы.")
        if comp == 3:
                print("Компьютер выбрал бумагу.")
        # определяем победителя
        if player == comp:
                win = 0
        if player == 1 and comp == 2:
                win = 1 
        if player == 1 and comp == 3:
                win = 2 
        if player == 2 and comp == 1:
            win = 2  
        if player == 2 and comp == 3:
                win = 1 
        if player == 3 and comp == 1:
                win = 1
        if player == 3 and comp == 2:
                win = 2
        if win == 0:
                print("Ничья!")
        if win == 1:
                print("Победил игрок!")
        if win == 2:

                print("Победил компьютер!")

    else:
        break
