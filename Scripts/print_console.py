import sys

if len(sys.argv) == 3:
    text = sys.argv[1]
    repeat = int(sys.argv[2])

    for i in range(repeat):
        print(text)
else:
    print("Error introduce los argumentos correctamente!!")
    print("Ejemplo: python3 print_console.py 'Hola que tal!' 5")