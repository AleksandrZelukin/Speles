#uzmini skaitli
import random
guesses_made = 0 # uzminēšanas mēģinājumu skaits
name = input('Hei! Kā tevi sauc?\n')
number = random.randint(1, 30)
print ('Super!, {0}, Es izdomāju skaitli starp 1 un 30. Jūs varat uzminēt?'.format(name))

# kamēr lietotājs nav pārsniedzis atļauto mēģinājumu skaitu - 6
while guesses_made < 6:
    guess = int(input('Ievadiet numuru: '))
    guesses_made += 1
    if guess < number:
        print ('Tavs skaitlis ir mazāks nekā es domāju.')
    if guess > number:
        print ('Jūsu skaits ir lielāks par to, kuru es iedomājos.')
    if guess == number:
        break
    if guess == number:
        print ('Oho, {0}! Jūs uzminējāt manu skaitli, izmantojot {1} mēģinājumi!'.format(name, guesses_made))
else:
    print ('Bet es neuzminēju! Es domāju, ka skaitlis {0}'.format(number))
