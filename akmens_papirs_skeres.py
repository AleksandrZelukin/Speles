import random
print("""
      ==========
      Akmens - 1
      Šķēres - 2
      Papīrs - 3
      ==========
      """)

vardi = {1:"Akmens",2:"Šķēres",3:"Papīrs",4:"Stop, Spēles beigas!"}
counter = 0
spele = 1
while True:
    print("Spēles numurs: ",spele)
    speletajs = int(input("Jūsu izvēlē: "))
    dators = random.randint(1,3)
    print("Jūsu izvēļe: ",vardi[speletajs])
    print("Datora izvēlē:",vardi[dators])
 
    if speletajs == dators:
        print("spēles izloze") 
        spele += 1  
    if speletajs == 1 and dators == 2 or speletajs == 2 and dators == 3 or speletajs == 3 and dators == 1:
        counter += 1
        spele += 1
        print("Jūs uzvāreja!, kopējais konts: ",counter) 
    if speletajs == 4:
        break
    else:
        spele += 1
        counter -= 1
        print("Dators uzvāreja, kopējais konts: ",counter)
        

    
    