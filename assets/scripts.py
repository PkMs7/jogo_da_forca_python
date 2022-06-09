

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

def jogarNovamente():
    return