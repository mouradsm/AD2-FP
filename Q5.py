import struct
#arquivo = input("Informe o nome do arquivo binário de números: ")

arquivo = "arquivo.bin"

def buscar(arq, num):




    try:
        with open(arquivo, "rb") as arq:
            byte = arq.read(4)
            achado = False
            while True:
                numero = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
                if numero == -1:
                    exit(0)

                while byte != b"":
                    if numero == struct.unpack('i',byte)[0]:
                        achado = True
                        break
                    else:
                        achado = False
                    byte = arq.read(4)

                if achado:
                    print("O número está na posição %d\n", arq.tell())
                else:
                    print("O número não foi encontrado.\n")


            arq.close()
    except IOError:
        print("Erro ao abrir ou manipular o arquivo.")