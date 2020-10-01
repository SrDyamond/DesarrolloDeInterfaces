#MetodoBurbuja
print("Ordenacion de numeros")
n1=int(input("Inserta o primeiro numero"))
n2=int(input("Inserta o segundo numero"))
n3=int(input("Inserta o terceiro numero"))
aux=0

if n1>n2:
    aux=n1
    n1=n2
    n2=aux
if n1>n3:
    aux=n1
    n1=n3
    n3=aux
if n2>n3:
    n2=aux
    n2=n3
    n3=aux

print(n1,n2,n3)
