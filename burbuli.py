from tkinter import *
garums = 500
platums = 800
logs = Tk()
logs.title('Burbuļu spridzinātājs')
a = Canvas(logs,width=platums, height=garums, bg='darkblue')
a.pack()
kuģa_id = a.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
kuģa_id2 = a.create_oval(0, 0, 30, 30, outline='red')
kuģa_r = 15
vid_x = platums/2
vid_y = garums/2
a.move (kuģa_id, vid_x, vid_y)
a.move (kuģa_id2, vid_x, vid_y)

'''
Programmas nākamais posms ir uzrakstīt programmu, kas liek
zmūdenei kustēties, kas tiek piespiesti bulttaustiņi.
Izveidosim funkciju - notikumu darinātāju. Šī funkcija pārbauda, kurš
taustiņā ticis piespiests,un pārvieto zemūdeni.
'''
kuģa_ātr = 10

def pārvietot_ķuģi(notikums):
    if notikums.keysym == 'Up':
        a.move(kuģa_id, 0, -kuģa_ātr)
        a.move(kuģa_id2, 0, -kuģa_ātr)

    elif notikums.keysym == 'Down':
        a.move(kuģa_id, 0, kuģa_ātr)
        a.move(kuģa_id2, 0, kuģa_ātr)

    elif notikums.keysym == 'Left':
        a.move(kuģa_id, -kuģa_ātr, 0)
        a.move(kuģa_id2, -kuģa_ātr, 0)

    elif notikums.keysym == 'Right':
        a.move(kuģa_id, kuģa_ātr, 0)
        a.move(kuģa_id2, kuģa_ātr, 0)

a.bind_all('<KeyRelease>', pārvietot_ķuģi)
    

'''
Nākamais solis ir izveidot burbuļus, ko spēlētājam spridzināt.
Burbuļim būs atšļiriga lielums un pārvīetošanās ātrums.
'''

from random import randint
burb_id = list()
burb_r = list()
burb_ātrums = list()

min_burb_r = 10
max_burb_r = 30
max_burb_ātr = 10
atstarpe = 100

def izveidot_burbuli():
    x = platums + atstarpe
    y = randint(0, garums)
    r = randint(min_burb_r, max_burb_r)
    id1 = a.create_oval(x - r, y - r, x + r, y + r,outline="white")
    burb_id.append(id1) 
    burb_r.append(r)
    burb_ātrums.append(randint(1, max_burb_ātr))


'''
Liec burbuļiem kustēcies

'''
def pārvietot_burbuļus():
    for i in range(len(burb_id)):
        a.move(burb_id[i], - burb_ātrums[i], 0)

from time import sleep, time
burb_nejauši = 10


def iegūt_koord(id_skaitlis):
    poz = a.coords(id_skaitlis)
    x = (poz[0] + poz[2])/2
    y = (poz[1] + poz[3])/2

    return x, y    

def dzēst_burbuli(i):
    del burb_r[i]
    del burb_ātrums[i]
    a.delete(burb_id[i])
    del burb_id[i]

def notīrīt_burbuļus():
    for i in range(len(burb_id) -1, -1, -1):
        x, y = iegūt_koord(burb_id[i])
        if x < -atstarpe:
            dzēst_burbuli(i)
            

from math import sqrt
def attālums(id1, id2):
    x1, y1 = iegūt_koord(id1)
    x2, y2 = iegūt_koord(id2)
    return sqrt((x2-x1)**2 + (y2 - y1)**2)

def sadursme():
    punkti = 0
    for burb in range(len(burb_id)-1, -1, -1):
        if attālums(kuģa_id2, burb_id[burb]) < (kuģa_r + burb_r[burb]):
            punkti += (burb_r[burb] + burb_ātrums[burb])
            dzēst_burbuli(burb)
    return punkti

a.create_text(50, 30, text="LAIKS", fill="white")
a.create_text(150, 30, text="REZULTĀTS", fill="white")
laiks_teksts = a.create_text(50, 50, fill="white")
rezultāts_teksts = a.create_text(150, 50, fill="white")
def parādīt_rezultātu(rezultāts):
    a.itemconfig(rezultāts_teksts, text=str(rezultāts))
def parādīt_laiku(laiks_palicis):
    a.itemconfig(laiks_teksts, text=str(laiks_palicis))


from time import sleep, time
burb_nejauši = 10
laika_ierobežojums = 30
papildlaika_rez = 1000
rezultāts = 0
papildu = 0
beigas = time() + laika_ierobežojums

rezultāts = 0

# Spēles galvenais cikls

while time() < beigas:
    if randint(1, burb_nejauši) ==1:
        izveidot_burbuli()
        pārvietot_burbuļus()
        notīrīt_burbuļus()
        rezultāts += sadursme()
        if (int(rezultāts/papildlaika_rez)) > papildu:
            papildu += 1
            beigas += laika_ierobežojums
        parādīt_rezultātu(rezultāts)
        parādīt_laiku(int(beigas - time()))
        #print(rezultāts)
        logs.update()
        sleep(0.01)
    

a.create_text(vid_x, vid_y,text="SPĒLES BEIGAS", fill="red", font=("Helvetica", 60))
a.create_text(vid_x, vid_y +45, text="REZULTĀTS: "+ str(rezultāts), fill="yellow", font=("Helvetica", 30))
a.create_text(vid_x, vid_y + 70, text="Papildu laiks:  " + str(papildu*laika_ierobežojums), fill="yellow")


