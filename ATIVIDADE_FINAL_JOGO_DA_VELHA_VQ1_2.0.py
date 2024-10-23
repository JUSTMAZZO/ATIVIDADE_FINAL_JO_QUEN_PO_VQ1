import os
import random

jogarDeNovo = "s"
jogadas = 0
quemJoga = 2
# 1 = CPU ; 2 = JOGADOR
maxJogadas = 9
vit = "n"
tabuleiro =[
    [" "," "," "], #l0c0 l0c1 l0c2
    [" "," "," "], #l1c0 l1c1 l1c2
    [" "," "," "]  #l2c0 l2c1 l2c2
]


def tela():
    global tabuleiro
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2])
    print("   -----------")
    print("1:  " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2])
    print("   -----------")
    print("2:  " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2])
    print("Jogadas: " + str(jogadas))

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas    
    if quemJoga ==2 and jogadas<maxJogadas:
        try:
            l = int(input("linha..: "))
            c = int(input("coluna.: "))
            while tabuleiro[l][c]!= " ":
                l = int(input("linha..: "))
                c = int(input("coluna.: "))
            tabuleiro[l][c] ="X"
            quemJoga = 1
            jogadas+= 1
        except:
            print("Jogada Invalida")
            os.system("pause")
            # vit="n"

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)

        while tabuleiro[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        tabuleiro[l][c] = "O"       
        jogadas += 1
        quemJoga = 2

def verificarVitoria():
    global tabuleiro
    vitoria = "n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria = "n"
        
        #verificar linhas
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(tabuleiro[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            il += 1
        if(vitoria != "n"):
            break

        #verificar colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (tabuleiro[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic+=1

        if (vitoria != "n"):
            break
        #verifica diagonal1
        soma=0
        idiag=0

        while idiag<3:
            if (tabuleiro[idiag][idiag] == s):
                soma += 1
            idiag+=1
        if(soma==3):
            vitoria=s
            break
        #verifica diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 2

        while idiagc >= 0:
            if (tabuleiro[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria

def redefinir():
    global tabuleiro
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2  # 1 = CPU ; 2 = JOGADOR
    maxJogadas = 9
    vit = "n"
    tabuleiro = [
        [" ", " ", " "],  # l0c0 l0c1 l0c2
        [" ", " ", " "],  # l1c0 l1c1 l1c2
        [" ", " ", " "]  # l2c0 l2c1 l2c2
    ]
while(jogarDeNovo=="s"):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit=verificarVitoria()
        if(vit!="n")or(jogadas>=maxJogadas):
            break

    print("FIM DE JOGO")
    if(vit=="x" or vit=="O"):
        print("Resultado: AEEE Parabens Jogador" +  vit  + "voce venceu")
    else:
        print("Resultado: Opaaa Parece que Tivemos um Empate")
    jogarDeNovo=input("Eae? jogar Novamente? [s/n]: ")
    redefinir()

