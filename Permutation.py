"""A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.

Given n, construct a beautiful permutation if such a permutation exists."""
import random
n = int(input())



lista = []
if n <= 3 and n!=1 : 

	print("NO SOLUTION")
	
	
else:
	listapares = [i for i in range(1,n+1) if i % 2 == 0]
	listaimpares = [i for i in range(1,n+1) if i%2 != 0]
	lista = listapares + listaimpares

for i in lista:
	print(i, end = " ")
print("")


"""else:
	randomlist = [ i for i in range(1,n+1)]
	lista = []
	posicion = 0
	numero = random.choice(randomlist)
	randomlist.remove(numero)
	lista.append(numero)
	
	
	while len(randomlist) > 0:
	
		numero = random.choice(randomlist)
		
				
		if (numero not in lista) and (lista[posicion]-numero != 1 and numero - lista[posicion] != 1):
			randomlist.remove(numero)
			lista.append(numero)
			posicion +=1
	
	for i in lista:
	
		print(i,end=" ")
		
	print("")"""
	 
			 
		
			

	
	
	
	
