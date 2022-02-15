n = int(input())
x = input().split()
assert len(x)==n-1
for i in range(len(x)):
	x[i]=int(x[i])
conjuntoTotal = set(i for i in range(1,n+1))
x= set(x)
numero=conjuntoTotal-x
print(list(numero)[0])
	
