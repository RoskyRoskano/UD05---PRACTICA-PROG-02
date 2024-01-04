# Le pasamos dos numeros y uno se va incrementando y sacando cual es el mayor numero por el que se pueden dividir los dos
def mcd(a, b):
    aux = 0
    while b != 0:
        aux = b
        b = a % b
    return  aux

# Si hay algun numero que el resto es 0 entre el rango de 2 y el numero que le pasamos, no es primo
# porque ya hay otro numero que se pueda dividir entre el nuestro y el resto de 0
def esPrimo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True

print("El maximo comun divisor de 20 y de 12 es:",mcd(20, 12))

#Recorremos del 1 a 50 y le vamos pasando cada número a la función. Si la función devuelve True, ese número es primo
for i in range(1,51):
    if esPrimo(i)==True:
        print("El numero",i,"es primo")