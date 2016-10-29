#PRIMEIRO ELEMENTO DA LISTA
def car(dados):
    return dados[0]
#TODOS ELEMENTO EXCETO O PRIMEIRO
def cdr(dados):
    return dados[1:len(dados)]

#RETORNA UMA LISTA COM O PRIMEIRO ELEMENTO SEGUIDO PELA LISTA DE DADOS
def cons(item, dados):
    return [item] + dados

def obterSetor(lista, inicio, fim):

    if fim > len(lista) or inicio > fim:
      return []

    setores = []

    def recusividade(lista, inicio, fim):
        if not(len(lista) == 0 or fim < 1):
            if inicio > 1:
                recusividade(cdr(lista), inicio - 1, fim - 1)
            elif fim > 1 or inicio <= 1:
                setores.append(car(lista))
                recusividade(cdr(lista), inicio, fim - 1)

    recusividade(lista, inicio, fim)

    return setores

print(obterSetor(["ana","maria", "chico", "igor", "juca"], 2, 4))

print(obterSetor(["ana","maria", "chico", "igor", "juca"],4, 1))

print(obterSetor([10, 2, 5, 13, 26, 4, 2, 9, 33, 18, 6, 99, 12, 17], 5, 9))

print(obterSetor([10, 2, 5, 13, 26, 4, 2, 9, 33, 18, 6, 99, 12, 17], 5, 19))
