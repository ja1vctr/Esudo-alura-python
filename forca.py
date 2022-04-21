import random


def jogar():

    jogatina = 1
    while(jogatina == 1):
        print("---------------Jogo da forca---------------\n\n")

        def carregar_palvra_secreta():
            arquivo = open("palavras.txt", "r")
            palavras = []

            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)
            arquivo.close()

            posiçao = random.randrange(0, len(palavras))
            palavra_secreta = palavras[posiçao]

            return palavra_secreta

        def lista_das_letras():
            lista_letras = ["_" for i in palavra_secreta]
            print("{}\n\n".format(lista_letras))

            return lista_letras

        palavra_secreta = carregar_palvra_secreta()
        lista_letras = lista_das_letras()

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

        print("Finde da Partida!")
        print("Você deseja jogar denovo?")
        print("(1) Sim\n(2) Não")

        jogatina = int(input())

    print("fim de jogo!")


if (__name__ == "__main__"):
    jogar()
