import random, struct

try:
    with open("arquivo-seq.bin", "wb") as arq:
        for i in range(21):
            numero = struct.pack("i", random.randint(0,100))
            arq.write(numero)
            numero = struct.pack("d", random.randrange(0,100))
            arq.write(numero)
            numero = struct.pack("d", random.randrange(0, 100))
            arq.write(numero)
    arq.close()
except IOError:
    print("Erro ao abrir ou ao manipular arquivo.")

