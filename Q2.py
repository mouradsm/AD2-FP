arquivoReferencia   = input("Arquivo de referência: ")
arquivoPesquisa     = input("Arquivo a ser pesquisado: ")

def separaPalavras(arquivo):
    return [palavra for line in open(arquivo, 'r') for palavra in line.split()]

def busca_referencia(palavrasReferencia, arquivo):

    conteudo = open(arquivo)

    for indexLinha, line in enumerate(conteudo):
        for index, word in enumerate(line.strip('\n').split(" ")):
            if word in palavrasReferencia:
                print('('+ '"' + word + '"' + ', ' + str(indexLinha + 1) + ', ' + str(index + 1) + ')')

busca_referencia(separaPalavras(arquivoReferencia), arquivoPesquisa)