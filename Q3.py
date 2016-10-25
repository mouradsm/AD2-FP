arquivoSinonimo =   input("Informe o nome do arquivo de sinônimos: ")
arquivoTexto    =   input("Informe o nome do arquivo com o texto: ")

def recuperaLinhas(arquivo, modo ='r'):
    conteudo = open(arquivo, modo)
    return conteudo.readlines()

def lerSinonimos(nomeArq):
    linhas = recuperaLinhas(nomeArq)

    dicionario = dict()

    for line in linhas:
        palavras = line.strip('\n').split()
        dicionario.update({palavras[0]: palavras[1]})
    return dicionario

def processarTexto(nomeArq, sinonimos):

    arquivo = open(nomeArq, 'r')
    arquivoTemp = open('arquivoTemp.txt','w')

    for line in arquivo:
        for word in line.strip('\n').split(" "):
           if word in sinonimos:
               line = line.replace(word,sinonimos[word])
        arquivoTemp.write(line)

    arquivoTemp.close()
    arquivo.close()

    arquivo = open(nomeArq, 'w')
    arquivoTemp = open('arquivoTemp.txt', 'r')

    for line in arquivoTemp:
        arquivo.write(line)

    arquivoTemp.close()
    arquivo.close()


dicionario = lerSinonimos(arquivoSinonimo)
processarTexto(arquivoTexto, dicionario)