import random


arquivo = open("palavras.txt", "r")
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

arquivo.close()


def jogar():
    jogatina = 1
    while(jogatina == 1):
        print("---------------Jogo da forca---------------\n\n")

        posiçao = random.randrange(0, len(palavras))

        def jogo_da_forca():
            palavra_secreta = palavras[posiçao]
            enforcou = False
            acertou = False
            lista_letras = ["_" for i in palavra_secreta]

            print("{}\n\n".format(lista_letras))

            enforcou = False
            acertou = False
            erros = 0

            while(not enforcou and not acertou):
                chute = input("Qual a letra? ").strip()

                if(chute.lower() in palavra_secreta):

                    count = 0
                    for tentativa in palavra_secreta:
                        if (chute.lower() == tentativa.lower()):
                            lista_letras[count] = chute
                        count += 1
                else:
                    erros += 1

                enforcou = erros == 6
                acertou = "_" not in lista_letras

                print("Forca: {}\n\n".format(lista_letras))

            if(acertou):
                print("Você ganhou!!!!!")

            elif(enforcou):
                print("você perdeu :(")
                print(f"\nA palavras era: {palavra_secreta}\n")
        jogo_da_forca()

        print("Finde da Partida!")
        print("Você deseja jogar denovo?")
        print("(1) Sim\n(2) Não")

        posiçao = 0
        jogatina = int(input())

    print("fim de jogo!")


if (__name__ == "__main__"):
    jogar()
