import sys

try:
    if(len(sys.argv)<3):
        print("No hay parametros para contar")

    else:
        for i in range(int(sys.argv[1]), int(sys.argv[2]) +1):
            print(i)

except:
    print("Datos Incorrectos")