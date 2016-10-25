arquivoReferencia   = input("Arquivo de referência: ")
arquivoPesquisa     = input("Arquivo a ser pesquisado: ")

def separaPalavras(arquivo):
    return [palavra for line in open(arquivo, 'r') for palavra in line.split()]

def recuperaLinhas(arquivo):
    conteudo = open(arquivo)
    return conteudo.readlines()

def busca_referencia(palavrasReferencia, arquivo):
    linhas = recuperaLinhas(arquivo)

    for indexLinha, line in enumerate(linhas):
        for index, word in enumerate(line.strip('\n').split(" ")):
            if word in palavrasReferencia:
                print('('+ '"' + word + '"' + ', ' + str(indexLinha + 1) + ', ' + str(index + 1) + ')')

busca_referencia(separaPalavras(arquivoReferencia), arquivoPesquisa)