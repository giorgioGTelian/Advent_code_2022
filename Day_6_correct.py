with open("input.txt", "r") as f:
 input = f.read()


# A ogni colonna far corrispondere il numero di quella colonna. Associamo a una chiave numerica un valore stringa
# Dall'input prendere la lista di chiavi
lookup = '1'
lineWithKeysIndex = 0

with open("input.txt") as f:
 for num, line in enumerate(f, 1):
  if lookup in line:
   lineWithKeysIndex = num
   break

input = input.splitlines()
highestKey = max(input[lineWithKeysIndex-1].split(' '))
dictionary = dict.fromkeys(range(1, int(highestKey) + 1))

# Associare colonna di valori a chiavi
def getCrateColumn(dictKey):
 diff = 0
 if dictKey == 1:
  diff = 1
 else:
  return 

print(getCrateColumn(1))
print(getCrateColumn(2))
print(getCrateColumn(3))
print(getCrateColumn(4))


 #esempio:
 # dictKey = 1 -> colonna 2
 # dictKey = 2 -> colonna 6
 # dictKey = 3 -> colonna 10
 # dictKey = 4 -> colonna 14
 # dictKey = 5 -> colonna 18

 # la distanza tra dictKey e colonna aumenta sempre di 3
#print(input)
# Data model
# * Per ogni cassa ci sono 3 char (quadra, lettera, quadra oppure tre spazi in caso di assenza della cassa)
# * Tra una cassa l'altra c'e' sempre uno spazio
# Creazione di un dizionario/struttura dati dove salvari questi accoppiamenti
# Inizio movimento
