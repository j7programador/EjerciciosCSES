"""You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character."""

n = input() #Definimos la variable n que nos va a almacenar nuestra cadena string
"""Definimos una varible contador que almacena el conteo de las secuencias
de caracteres que son repetidas consecutivamente. La inicializamos en 1,
porque la cadena de caracteres más pequeña es de 1 caracter."""
contador = 1 

"""
La variable mayor guardara la cadena de caracteres mas larga, inicializamos en uno,
porque al ingresar una cadena con un solo caracter, no se podría comparar con la varible contador
que también inicia en uno. 
"""
mayor = 1

"""
Establecemos un ciclo for que nos va a recorrer cada posicion de la cadena de caracteres.
"""
for i in range(1,len(n)): """Inicializamos el ciclo for en 1 para poder comparar el caracter de la primer 
posicion con el siguiente y así poder recorrer todo el arreglo"""
	if n[i-1] == n[i]: #Comparamos el caracter anterior con su siguiente.
		contador += 1 # Si son iguales le sumamos uno al contador.
	else:
		contador = 1 # Si no son iguales reiniciamos contador en 1
			
	if contador > mayor:
		mayor = contador # Si contador es mayor al mayor que equivale a la cadena mas larga de caracteres iguales, almacenamos ese valor en mayor
		
print(mayor)



	
