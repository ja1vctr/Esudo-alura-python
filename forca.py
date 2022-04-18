import pandas as pd


def jogar():
    print("---------------Jogo da forca---------------\n\n")

    df_palavras = pd.read_csv()
    palavra_secreta = "banana"
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

    print("Fim de jogo!")


if (__name__ == "__main__"):
    jogar()
