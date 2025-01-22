import PySimpleGUI as sg
import random
import sqlite3

def pret_izveele():
  defizveeles = ['A','S','P']
  pretIzveele = random.choice(defizveeles)
  if pretIzveele == 'P':
    window['-IZVELE-'].update("Papīrs")
  if pretIzveele == 'S':
    window['-IZVELE-'].update("Šķēres")
  if pretIzveele == 'A':
    window['-IZVELE-'].update("Akmens")
  return pretIzveele

def rezultats(pretIzveele,izveele):
  if pretIzveele == str.upper(izveele):
    rezultats = "Neizšķirts!"
  elif pretIzveele == "A" and izveele.upper() == "S":
    rezultats = "Tu zaudēji"
  elif pretIzveele == "S" and izveele.upper() == "P":
    rezultats = "Tu zaudēji"
  elif pretIzveele == "P" and izveele.upper() == "A":
    rezultats = "Tu zaudēji"
  else:
    rezultats = "Tu uzvarēji"
  return rezultats

def datu_saglabasana(vards,vecums):
  db = sqlite3.connect('dati.db')
  db.execute(
  """
  CREATE TABLE IF NOT EXISTS rezultati
  (id   INTEGER   PRIMARY KEY AUTOINCREMENT   NOT NULL,
  vards   TEXT,
  vecums   INTEGER
  )
  """
  )
  db.execute("""
           INSERT INTO rezultati
           (vards,vecums)
           VALUES(:vards,:vecums)
           """,{'vards':vards,'vecums':vecums})

  db.commit()

def datu_izvadisana():
  db = sqlite3.connect('dati.db')
  dati = db.execute("""SELECT * FROM rezultati
                  """)
  rezultats = dati.fetchall()
  return rezultats

sg.theme('DarkAmber')   
layout = [  [sg.Text('Spēle: Akmens, Šķēres, Papīrīts')],
            [sg.Text('Izvēlies darbību')],
            [sg.Button('Akmens'), sg.Button('Šķēres'),sg.Button('Papīrs')],
            [sg.Text('Pretinieka izvēle: '),sg.Text('', key='-IZVELE-')],
            [sg.Text('Rezultāts: '),sg.Text('', key='-REZ-')],
            [sg.Text('Ievadi savu vārdu:'), sg.InputText()],
            [sg.Text('Ievadi savu vecumu:'), sg.InputText()],
            [sg.Text('Vai vēlies saglabāt rezultātu? '),sg.Button('Saglabāt')]]

layout2 = [[sg.Text('',key = '-JA-')]]

tabgrp = [
  [
    sg.TabGroup([[
      sg.Tab('Spēle',layout ), 
      sg.Tab('Spēlētāju dati',layout2)
    ]]),
    sg.Button('Aizvērt')
  ]
]
 
window = sg.Window('Spēle', tabgrp)
while True:             
    event, values = window.read()
    if event == "Akmens":
      izveele = 'A'
      pretIzvele = pret_izveele()
      window['-REZ-'].update(rezultats(pretIzvele,izveele))
    elif event == "Šķēres":
      izveele = 'S'
      pretIzvele = pret_izveele()
      window['-REZ-'].update(rezultats(pretIzvele,izveele))
    elif event == "Papīrs":
      izveele = 'P'
      pretIzvele = pret_izveele()
      window['-REZ-'].update(rezultats(pretIzvele,izveele))
    elif event == "Saglabāt":
      vards = values[0]
      vecums = values[1]
      datu_saglabasana(vards,vecums)
      window['-JA-'].update(datu_izvadisana())
    if event in (sg.WIN_CLOSED, 'Aizvērt'):
        break

window.close()