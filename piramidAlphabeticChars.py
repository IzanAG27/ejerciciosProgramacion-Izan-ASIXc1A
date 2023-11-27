"""
Imprimir de la A fins la Z.

A cada linia apareix un carcater i la seguent linia apareix un carcater més de forma progresiva. Fins aconseguir tenir una linia que mostri de la A fins la Z
Output
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H
"""
numero = int(input())
variable = chr(numero)
a = ord("A")
z = ord("Z")
for x in range(a, z + 1):
    print(chr(x))
    for i in range(a + 1):
        print(i)





