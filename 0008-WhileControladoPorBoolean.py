valores=[1,6,8,2,90,56]
indice=0
longitud=len(valores)
encontrado= False
numero = int(input("Teclee el numero a buscar"))
while not encontrado and indice < longitud:
    valor=valores[indice]
    if valor==numero:
        encontrado=True
    else:
        indice += 1
if encontrado:
    print("Numero encontrado")
else:
    print("Numer no encontrado")
