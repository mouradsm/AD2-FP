import struct
arquivo = input("Informe o nome do arquivo binário de números: ")

def buscar(arq, num):

    print("busquei")
    arq.seek(0)
    primeiro = struct.unpack("i",arq.read(4))[0]
    achado = False
    arq.seek(0, 2)
    ultimo = arq.tell()//4 #dividido por 4 bytes por número

    if num >= ultimo:
        return -1

    while primeiro <= ultimo and not achado:
        meiuca = (primeiro + ultimo)//2
        arq.seek(meiuca * 4) #multiplicado por 4 bytes por número

        numero = struct.unpack("i", arq.read(4))[0]
        if num == numero:
            achado = True
        else:
            if num < numero:
                ultimo = meiuca-1
            else:
                primeiro = meiuca+1

    if achado:
        return arq.tell()//4 #Multiplicado por 4 bytes por numero
    else:
        return -1

try:
    with open(arquivo, "rb") as arquivo:

        while True:
            numero = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
            if numero == -1:
                exit(0)

            posicao = buscar(arquivo, numero)

            if posicao != -1:
                print('O número está na posição %d\n' % posicao)
            else:
                print("O número não foi encontrado.\n")



    arquivo.close()
except IOError:
    print("Erro ao abrir ou manipular o arquivo.")