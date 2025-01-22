print ('Paspelesim')
def start():
    if i == 2:
        count = [0,0]
    elif i == 3:
        count = [0,0,0]
    elif i == 4:
        count = [0,0,0,0]
    koloda = [6,7,8,9,10,11] * 4
    import random
    random.shuffle(koloda)
    
    n = int('0')
    while n<i:
        print('Spelētajs nr. %d' %n)
        while True:
        	choice = input('Spēlejat? y/n\n')
        	if choice == 'y':
        	    current = koloda.pop()
        	    print('Jūs saņēma %d' %current)
        	    count[n] += current
        	    if count[n]>21:
        	        print('Jūms %d punktus \n Jūs nospēlēja' %count[n])
        	        break
        	    else:
        	        print('Jūms %d punktus' %count[n])
        	elif choice == 'n':
        		print('Jūms %d punktus' %count[n])
        		break
        n+=1
    res = int('0')
    chemp = int('0')
    n=0
    while n<i:
        if res<count[n] and count[n]<21:
        	res=count[n]
        	chemp=n
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
