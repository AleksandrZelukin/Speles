from tkinter import *
from random import shuffle, randint
from tkinter import Label, Entry, Button, PhotoImage, Tk
rez = dict()

root = Tk()
root.geometry("450x300+200+200")
root.title("Dragon Water")
root.resizable(False, False)
root["bg"] = "#FFF"
#app = Main(root)
#app.pack()
doors = ['dragon', 'water', 'empty']
lives = 3

def durvis1 ():
  choice = randint(1,2,3)
  if doors[choice - 1] == 'dragon':
    lives -= 1
  
trap1 = PhotoImage(file='fire.gif')
izo1 = Label(image=trap1)
izo1.place(x=150, y=40)

trap2 = PhotoImage(file='water.gif')
izo2 = Label(image=trap2)
izo2.place(x=150, y=40)


btn1 = Button(text="1.durvis",command=durvis1)
btn1.place(x=10, y=240, width=120, height=50)
btn2 = Button(text="2.durvis")
btn2.place(x=155, y=240, width=120, height=50)
btn3 = Button(text="3.durvis")
btn3.place(x=300, y=240, width=120, height=50)




'''
while True:
    choice = input ('Spelejam? y/n\n')
    if choice == 'y':
        players = input('Tavs vards:  ')
        doors = ['dragon', 'water', 'empty']
        lives = 3
        score = 0
        while True:
            choice = int(input('Ievādi durvu numuru (1, 2 vai 3, 10 lai iziet no spēles): '))
            shuffle(doors)
            score += 100
            if choice > 3:
                print('Nekas nav noticis.')
                print ('Meginiet velreiz!')
                continue
            if choice < 0:
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

    if choice == 10:
        print('Speles rezultati:')
        for key in rez:
                print(key,'nopelnija', rez[key], 'punktus')
        break
'''
root.mainloop()