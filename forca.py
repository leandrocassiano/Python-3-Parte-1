# forca.py

import random # esse comando importa a biblioteca para podermos usar a funcionalidade random
def imprimi_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # o arquivo txt precisa estar no mesmo local que o código.
    palavras = []

    for linha in arquivo:
        linha = linha.strip()  # strip retirar os espaços das palavras.
        palavras.append(linha)  # append adiciona novamente as linhas a lista palavras.

    arquivo.close()  # Esse comando libera o canal de comunicação entre o pycharm e o processador.

    numero = random.randrange(0, len(palavras))  # nesse comando randrange
    # vai sortear os números de 0 até o tamanho da nossa lista de palavras
    # conforme o comando len(palavras) que devolve o tamanho da string.

    palavra_secreta = palavras[numero].upper()  # upper deixa toda a
    # palavra em maiúsculo assim facilitando nossa verificação dentro do laço.

    return palavra_secreta

def jogar():

    imprimi_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper() # aqui o professor usa strip e
        # upper já parece deixar o input do jogador no padrão da nossa
        # lista.

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
