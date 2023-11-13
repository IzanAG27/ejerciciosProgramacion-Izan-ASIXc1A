PWD = "asdasd"
clave = input("Dime la clave: ")
intento = 0
while clave != PWD and intento < 2 and clave != "1234":
    intento = intento + 1
    print("Clave incorrecta")
    clave = input("Dime la clave")
    if intento == 2 and clave != PWD and clave != "1234":
        print("Límite de fallos superado")
if clave == PWD or clave == "1234":
    print("Bienvenido")
print("Programa terminado")