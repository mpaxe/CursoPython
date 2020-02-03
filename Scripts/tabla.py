import sys

if len(sys.argv) == 3:
    entrada_1 = sys.argv[1]
    entrada_2 = sys.argv[2]

    if entrada_1.isnumeric() and int(entrada_1) >= 1 and int(entrada_1) <= 9 and entrada_2.isnumeric() and int(entrada_2) >= 1 and int(entrada_2) <= 9:
        for i in range(int(entrada_1)): 
            for j in range(int(entrada_2)):
                print(" * ", end='')
            print()
    else:
        print("Error: no es un número correcto")
else:
    print("Error!!. Ejemplo de uso: python3 tabla.py 2 7")

