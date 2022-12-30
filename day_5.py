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
crates = dict.fromkeys(range(1, int(highestKey) + 1))

# Associare colonna di valori a chiavi
#esempio:
# x = 1 -> return 2
# x = 2 -> return 6 => 2*3
# x = 3 -> return 10 => 3*3 + 1
# x = 4 -> return 14 => 4*3 + 2
# x = 5 -> return 18 => 5*3 + 3

# x = x*3 + (x-2)

def getCrateColumn(dictKey):
	if dictKey == 1:
		return 2
	else:
		return dictKey*3+(dictKey-2)

for key in crates:
	# Inizializziamo valore dizionario
	crates[key] = []
	# Iterare tutte le righe delle casse
	for index, line in enumerate(input, start=1):
		if index < lineWithKeysIndex:
			# per ogni riga se c'e' una cassa aggiungere la lettera al dizionario, se non c'e' una cassa mettiamo %
			crateIndex = getCrateColumn(key)
			if line[crateIndex-1] != ' ':
				crates[key].append(line[crateIndex-1])
	crates[key].reverse()

commandList = input[lineWithKeysIndex+1:]

for index, line in enumerate(commandList):
	commandList[index] = [int(s) for s in line.split() if s.isdigit()]

# Commandlist
# primo numero = quante casse devo spostare
# secondo numero = chiave di partenza
# terzo numero = chiave di arrivo
def executeCommandCrateMover9000(cratesNumber, fromKey, toKey):
	for i in range(cratesNumber):
		moving = crates[fromKey].pop()
		crates[toKey].append(moving)

def executeCommandCrateMover9001(cratesToMove, fromKey, toKey):
	# debug = False
	# if cratesToMove == 1 and fromKey == 3 and toKey == 9:
	# 	debug = True
	# if debug:
	# 	print("Executing command %s %s %s" % (cratesToMove, fromKey, toKey))
	# 	print(crates)
	moving = []
	for i in range(cratesToMove):
		moving.append(crates[fromKey].pop())
	moving.reverse()
	crates[toKey].extend(moving)
	# if debug:
	# 	print(crates)


for command in commandList:
	executeCommandCrateMover9001(command[0], command[1], command[2])

for column in crates:
	print(crates[column][-1])




