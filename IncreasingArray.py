"""
You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.

On each move, you may increase the value of any element by one. What is the minimum number of moves required?

"""
x = int(input()) # Ingresar el tamaño del arreglo
n = input().split() #Ingresamos la lista de los elementos del arreglo, con el split creamos la lista si esta separada por algo.
assert len(n) == x # Verificamos que el tamaño del arreglo corresponda al tamaño ingresado.
movimientos = 0
for i in range(len(n)):
	n[i]=int(n[i])
for i in range(1,len(n)):
	if (n[i-1]) > (n[i]): #Si el elemento anterior es mayor al siguien significa que el arreglo no es creciente.
		movimientos+=(n[i-1] - n[i])
		n[i]=(n[i-1])
		
print(movimientos)
	
	
	


