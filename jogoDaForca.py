import assets.scripts
import os

#listas de manipulação de dados
letrasChutadas = []
letrasCorretas = []
acumuladorDeLetrasCorretas = []



#cadastros aqui

nomeDesafiante = input("Digite o nome do desafiante: ")
nomeCompetidor = input("Digite o nome do competidor: ")

os.system("cls")


chances = int(input("Seu competidor terá quantas chances para adivinhar a palavra? "))

palavraChave = input("Digite a PALAVRA MÁGICA: ")
listaPalavraChave = assets.scripts.formarPalavraChave(palavraChave)

dicas = [input("\nDigite a dica 1: "), input("\nDigite a dica 2: "), input("\nDigite a dica 3: ")]

os.system("cls")

print(f"A PALAVRA MÁGICA possui {len(listaPalavraChave)} letras\n")

#jogo aqui

while(chances > 0):
    print(f"\nVocê possui ainda {chances} tentativas!\n")
    print("O que deseja fazer?\n")
    print("1 - Jogar")
    print("2 - Solicitar dica")
    print("0 - Sair do jogo\n")
    valorDigitado = int(input())
    if (valorDigitado == 1):
        chute = input("Qual seu chute: ")
        listaTemporaria = []
        for letra in listaPalavraChave:
            if letra == chute:
                print(chute)
                listaTemporaria.append(chute)
                acumuladorDeLetrasCorretas.append(chute)
            else:
                print("*")
        letrasChutadas.append(chute)
        verificadorDeChances = len(listaTemporaria)
        ganhaJogo = int(len(listaPalavraChave) - len(acumuladorDeLetrasCorretas))
        if ganhaJogo == 0:
            print(f"Parabéns, você ganhou o jogo, a PALAVRA MÁGICA era {listaPalavraChave}")
            break
        elif verificadorDeChances > 0:
            print(f"Letra(s) chutada(s) {letrasChutadas}")
            print(f"Letras acertadas {len(acumuladorDeLetrasCorretas)}")
            print(f"Letras da palavra chave {len(listaPalavraChave)}")
            del listaTemporaria
        elif verificadorDeChances == 0:
            print(f"Letra(s) chutada(s) {letrasChutadas}")
            print(f"Letras acertadas {len(acumuladorDeLetrasCorretas)}")
            print(f"Letras da palavra chave {len(listaPalavraChave)}")
            chances = chances - 1
            del listaTemporaria
    elif (valorDigitado == 2):
        assets.scripts.verificarDica(dicas)
    elif (valorDigitado == 0):
        print("Você perdeu!")
        break