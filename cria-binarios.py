import random, struct

try:
    with open("arquivo.bin", "wb") as arq:
        for i in range(11):
            numero = struct.pack("i", i)
            arq.write(numero)
    arq.close()
except IOError:
    print("Erro ao abrir ou ao manipular arquivo.")

