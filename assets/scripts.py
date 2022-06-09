import os

def verificarInteiros(caracter):
    try:
        if caracter == int:
            return 1
    except:
        return 0

def formarPalavraChave(string):
    listaPalavraChave = []
    listaPalavraChave.extend(string)
    return listaPalavraChave

def verificarDica(array):
    if len(array) > 0:
        print(array[0])
        del(array[0])
    else:
        print("Você não tem mais dicas!")

def escreverArquivoVencedor(listaPalavraChave, nomeDesafiante, nomeCompetidor):
    arquivo = open('assets/historico.txt','a')
    arquivo.write("\n------------------------------------------------------------------\n")
    arquivo.write(f"A PALAVRA MÁGICA era: {listaPalavraChave}\n")
    arquivo.write(f"O vencedor foi o Competidor {nomeCompetidor}\n")
    arquivo.write(f"O perdedor foi o Desafiante {nomeDesafiante}\n")
    arquivo.write("\n------------------------------------------------------------------\n")
    arquivo.close()

def escreverArquivoPerdedor(listaPalavraChave, nomeDesafiante, nomeCompetidor):
    arquivo = open('assets/historico.txt','a')
    arquivo.write("\n------------------------------------------------------------------\n")
    arquivo.write(f"A PALAVRA MÁGICA era: {listaPalavraChave}\n")
    arquivo.write(f"O vencedor foi o Desafiante {nomeDesafiante}\n")
    arquivo.write(f"O perdedor foi o Competidor {nomeCompetidor}\n")
    arquivo.write("\n------------------------------------------------------------------\n")
    arquivo.close()