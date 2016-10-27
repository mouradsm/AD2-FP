import math

# arquivoTurmas = input("Informe o arquivo de turmas: ")
# matriculaAluno = input("Informe a matricula do aluno: ")

arquivoTurmas = "TecnologiaEmSistemasDeComputacao.txt"
matriculaAluno = "216031013"

def recuperaLinhas(arquivo):
    conteudo = open(arquivo)
    return conteudo.readlines()

def lerTurmas(nomeArq):

    linhas = recuperaLinhas(nomeArq)
    quantidadeTurmas = int(linhas[0].strip('\n'))

    turmas = []
    listaTurmasNotas = []

    for i in range(quantidadeTurmas):
       turmas.append(linhas[i + 1].strip('\n'))

    for index, turma in enumerate(turmas):
        linhas = recuperaLinhas(turma)
        quantidadeAlunos = int(linhas[0].strip('\n'))

        listaTurmasNotas.insert(index, [])

        for i in range(quantidadeAlunos):
            notas = (linhas [i + 1].strip('\n').split(" "))

            listaTurmasNotas[index].append((notas[0],float(notas[1])))

    return listaTurmasNotas

def calcularMedia(listaDeListas, mat):

    notasAluno = []

    for lista in listaDeListas:
       for tupla in lista:
           if mat in tupla:
               notasAluno.append(tupla[1])

    return (math.fsum(notasAluno)/len(notasAluno))

listaDeListas = lerTurmas(arquivoTurmas)

media = calcularMedia(listaDeListas, matriculaAluno)

print(matriculaAluno + " " + "obteve média " + str(media))