"""A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:
Your task is to find out the number in row y and column x.

Input

The first input line contains an integer t: the number of tests.

After this, there are t lines, each containing integers y and x.

Output

For each test, print the number in row y and column x.

"""

n = int(input())

lista = []

for i in range(n):
	coordenada = input().split(" ")
	coordenada[0] = int(coordenada[0])
	coordenada[1] = int(coordenada[1])
	coordenada = list(coordenada)
	lista.append(coordenada)
for i in range(len(lista)):
	x = lista[i][0]
	y = lista[i][1]
	if x < y:
		if y % 2 == 1:
			print(int(y*y-x+1))
		else:
			
			print(int((y-1)**2+1+x-1))
	else:
		if x % 2 == 0:
			print(int(x*x-y+1))
		else:
			print(int((x-1)**2+1+y-1))
		

	 	
