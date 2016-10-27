import random, struct

try:
    with open("arquivo.bin", "wb") as arq:
        for i in range(10):
            numero = struct.pack("i", random.randint(0, 3))
            arq.write(numero)
    arq.close()
except IOError:
    print("Erro ao abrir ou ao manipular arquivo.")

