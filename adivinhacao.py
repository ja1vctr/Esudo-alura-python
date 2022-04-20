import random as rd


def jogar():
    jogatina = 1
    while(jogatina == 1):
        print("---------------Jogo da adivinhação---------------\n\n")

        def jogo_da_adivinhacao():

            numero_secreto = rd.randrange(1, 100+1)
            tentativas = 0
            pontos = 1000

            print(f"O número secreto é: {numero_secreto}")
            print("Escolha a dificuldade:")
            print("(1) Fácil\n(2) Médio\n(3) Difícil")
            try:
                dificuldade = int(input())
            except ValueError:
                print("Digite um dos números correspondentes às dificuldades!")
                dificuldade = int(input())

            if dificuldade == 1:
                tentativas = 20
            if dificuldade == 2:
                tentativas = 10
            if dificuldade == 3:
                tentativas = 5
            elif(1 < dificuldade > 3):
                print("*****Você escolheu uma dificuldade inválida*****")
                print("Como castigo, a dificuldade escolhida será a difícil")

            for rodada in range(1, tentativas+1):
                print(f"tentativa {rodada} de {tentativas}")
                tentativa = int(input("Escolha um número entre 1 e 100: "))

                if (1 < tentativa > 100):
                    print("Digite um número válido!")
                    continue

                acertou = tentativa == numero_secreto
                maior = tentativa > numero_secreto
                menor = tentativa < numero_secreto

                if acertou:
                    print("***********VOCÊ GANHOUUUUU!!!!!***********")
                    print(f"Sua pontuação é:{pontos}")
                    break

                else:
                    if menor:
                        print("O número que você chutou é MENOR que o número secreto")
                        pontos = pontos - (numero_secreto - tentativa)
                        pass
                    elif maior:
                        print("O número que você chutou é MAIOR que o número secreto")
                        pontos = pontos - (tentativa - numero_secreto)
                        pass
        jogo_da_adivinhacao()

        print("Finde da Partida!")
        print("Você deseja jogar denovo?")
        print("(1) Sim\n(2) Não")
        jogatina = int(input())

    print("fim de jogo!")


if(__name__ == "__main__"):
    jogar()
