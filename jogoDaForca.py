import assets.scripts
import os

#listas de manipulação de dados
letrasChutadas = []
letrasCorretas = []
acumuladorDeLetrasCorretas = []

#cadastros aqui

nomeDesafiante = input("Digite o nome do desafiante: ").upper()
nomeCompetidor = input("Digite o nome do competidor: ").upper()

os.system("cls")

chances = int(input("Seu competidor terá quantas chances para adivinhar a palavra? "))
assets.scripts.verificarInteiros(chances)

palavraChave = input("Digite a PALAVRA MÁGICA (apenas letras): ").upper()
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
    if valorDigitado == 0 or valorDigitado == 1 or valorDigitado == 2:
        if (valorDigitado == 1):
            chute = input("Qual seu chute (digite apenas uma letra): ").upper()
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
                print(f"Parabéns, você ganhou o jogo, a PALAVRA MÁGICA era {listaPalavraChave}\n")
                print("Deseja jogar novamente?\n")
                print("1 - Sim")
                print("0 - Não")
                valorFimDeJogo = int(input())
                if valorFimDeJogo == 1:
                    os.system("python jogoDaForca.py")
                elif valorFimDeJogo == 0:
                    assets.scripts.escreverArquivoVencedor(listaPalavraChave, nomeDesafiante, nomeCompetidor)
                    break
            elif verificadorDeChances > 0:
                print(f"Letra(s) chutada(s) {letrasChutadas}")
                print(f"Letras acertadas {len(acumuladorDeLetrasCorretas)}")
                print(f"Letras da PALAVRA MÁGICA {len(listaPalavraChave)}")
                del listaTemporaria
            elif verificadorDeChances == 0:
                print(f"Letra(s) chutada(s) {letrasChutadas}")
                print(f"Letras acertadas {len(acumuladorDeLetrasCorretas)}")
                print(f"Letras da PALAVRA MÁGICA {len(listaPalavraChave)}")
                chances = chances - 1
                del listaTemporaria
        elif (valorDigitado == 2):
            assets.scripts.verificarDica(dicas)
        elif (valorDigitado == 0):
            print("Você perdeu!")
            assets.scripts.escreverArquivoPerdedor(listaPalavraChave, nomeDesafiante, nomeCompetidor)
            break
    else:
        print("Utilize apenas as opções abaixo:")