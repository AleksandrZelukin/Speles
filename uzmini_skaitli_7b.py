import random
live = 3
skaitlis = random.randint(1,3)

print("Dators uzminēja skaitli!")
print("Tev ir trīs meģinājumi")

while live >0:
    players = int(input("ievadi savu variāntu: "))
    if skaitlis != players:
        print("Nē, vēl viens meģinājums!")
        live = live-1
        print(f"Tev palika {live} meģinājumi")
        
    else:
        print("Uraa! Pareizi!")
        break
