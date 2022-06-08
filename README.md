# Jogo da Forca

Descrição e demo aqui.


##REGRAS DE NEGÓCIO

- [x] O sistema deve pedir o nome do Desafiante e do Competidor ao abrir o programa.
- [x] Após o processo de identificação, a tela deve ser limpada, e solicitado ao desafiante algumas informações como: Palavra Chave, Dica 1, ica2 e Dica3.
- [ ] A tela novamente é limpa, e ao competidor, é apresentado algumas informações como: número de letras da palavra chave, ex: ******** e duas opções (Jogar ou Solicitar Dica).
- [ ] Se a opção solicitar dica for escolhida, deve ser apresentado a dica1 e o jogador obrigatóriamente deve arriscar uma letra no jogo. O máximo de dicas são 3, portanto o competidor pode solicitar apenas 3 dicas durante o game.
- [ ]  Quando a opção for de jogar, o competidor deve informar uma letra. O sistema deve verificar se letra exite na palavra e apresentar uma resposta, que no caso de correta deve ser algo tipo: ***A**A**, no caso de erro deve ser mostrado o número de erros do jogador, ex: Erro: 1.
- [ ]  Se o jogador errar 5 vezes ele perde e o desafiante ganha. Se ele acertar todas as letras da palavra, o competidor ganha e o desafiante  perde.
- [ ]   É necessário armazenar em um arquivo txt o histórico dos jogos. A cada partida é incluida uma linha, que indica quem venceu e quem perdeu. Ex.: Palavra: Bola – Vencedor: Desafiante Marcos , Perdedor: Competidor Pedro ou Palavra: inconstitucionalissimamente – Vencedor: Competidor Pedro, Desafiante:Marcos
- [ ]   Ao final de cada partida o sistema deve apresentar na tela o histórico de partidas jogadas e oferece uma opção de sair ou jogar novamente, recomeçando tudo de novo.
- [ ]   Utilização de try e except é extremamente necessário, para evitar que o usuário informe um número ou deixe em branco alguma informação necessária do sistema.
- [ ]    É obrigatório neste desenvolvimento, a utilização de funções que retornem valores de conferencia, indicando que o código foi bem desenvolvido e permite evoluções futuras.
