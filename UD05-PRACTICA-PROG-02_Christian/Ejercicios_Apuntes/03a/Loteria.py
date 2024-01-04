numeros = input("Introduce 6 números separados por espacios: ")

lista = numeros.split(" ")
lista.sort()

print(lista)
contador = 0

repes = set(lista)
if(len(repes) < 6):
    print("La lista NO es válida \nHay números repetidos")
    contador+=1

for i in range(len(lista)):
    if(int(lista[i]) < 1 or int(lista[i])>49):
        print(f"La lista NO es válida \nHay un número menor que 1 o mayor que 49")
        contador+=1

if(contador == 0):
    print("La lista es válida")
