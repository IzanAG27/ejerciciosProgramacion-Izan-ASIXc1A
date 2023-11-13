PWD = "asdasd"
clave = input("Dime la clave: ")
intento = 0
while clave != PWD and intento < 2 and clave != "1234":
    intento = intento + 1
    print("Clave incorrecta")
    clave = input("Dime la clave")
    while intento == 2:
        print("Límite de fallos superado")
        intento = 1

while intento < 2:
    print("Bienvenido")
    intento = 3
print("Programa terminado")