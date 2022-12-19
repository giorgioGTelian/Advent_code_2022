# cubetti 1x1x1. Trovare facce libere (non adiacenti). Forse è meglio trovarle tutte (n*6) e togliere 2 per ogni adiacente?
cubes=[]
with open("18.data","r") as f:
	for line in f:
		l=line.rstrip()
		l=list(map(int,l.split(',')))
		cubes.append(l)
f.close()

length=(len(cubes))
tot=length*6
adj=tot
for i in range(length):
	if i==length:
		break
	else:
		for j in range(length-i):
			same=0
			cont=False
			for k in range(3):
				if cubes[i][k]==cubes[i+j][k]:
					same+=1
				else:
					if abs(cubes[i][k]-cubes[i+j][k])==1:
						cont=True
			if same==2 and cont:
				adj-=2
print(adj)
