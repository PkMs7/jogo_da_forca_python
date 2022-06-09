import assets.scripts
import os

nomeDesafiante = input("Digite o nome do desafiante: ")
nomeCompetidor = input("Digite o nome do competidor: ")

os.system("cls")


chances = int(input("Seu competidor terá quantas chances para adivinhar a palavra? "))

palavraChave = input("Digite a PALAVRA MÁGICA: ")
listaPalavraChave = assets.scripts.formarPalavraChave(palavraChave)

dicas = [input("\nDigite a dica 1: "), input("\nDigite a dica 2: "), input("\nDigite a dica 3: ")]

os.system("cls")

quantidadeLetras = assets.scripts.contarLetras(listaPalavraChave)

letrasChutadas = []
letrasAcertadas = []
acumuladorDeLetrasAcertadas = []

ganhaJogo = len(listaPalavraChave) - len(acumuladorDeLetrasAcertadas)

print(f"A PALAVRA MÁGICA possui {quantidadeLetras} letras\n")

#jogo no while

#chances = 5

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
                acumuladorDeLetrasAcertadas.append(chute)
            else:
                print("*")
        letrasChutadas.append(chute)
        verificadorDeChances = len(listaTemporaria)
        if ganhaJogo == 0:
            print(f"Parabéns, você ganhou o jogo, a PALAVRA MÁGICA era{listaPalavraChave.join('')}")
            break
        elif verificadorDeChances > 0:
            print(f"Letra(s) chutada(s) {letrasChutadas}")
            del listaTemporaria
        elif verificadorDeChances == 0:
            print(f"Letra(s) chutada(s) {letrasChutadas}")
            chances = chances - 1
            del listaTemporaria
    elif (valorDigitado == 2):
        assets.scripts.solicitarDica(dicas)
    elif (valorDigitado == 0):
        break
print("Você perdeu!")
# número de letras da palavra chave, ex: ******** e duas opções (Jogar ou Solicitar Dica).