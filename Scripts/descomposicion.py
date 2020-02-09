import sys

if len(sys.argv) == 2:
    entrada_1 = sys.argv[1]

    if entrada_1.isnumeric():
        for i in range(len(entrada_1)):
            salida = ""
            for j in range(len(entrada_1) - 1, -1, -1):
                if i == j:
                    salida += entrada_1[i]
                else:
                    salida += '0'
            print(salida)

    else:
        print("Error: no es un número correcto")
else:
    print("Error!!. Ejemplo de uso: python3 descomposicion.py 2157")