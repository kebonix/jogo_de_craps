''' 
Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" 
e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 
10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados 
até tirar este número novamente. Você perde, no entanto, se tirar um 7 
antes de tirar este Ponto novamente.
'''
from random import randint as r

jogada = 0
valor_acumulado = 0

def arremessar_dado():
    dado = r(1,6)
    return dado

def arremessar_dados():
    return [arremessar_dado(), arremessar_dado()]

def verificar_jogada(dado1,dado2):
    global jogada
    global valor_acumulado
    soma = dado1 + dado2
    if jogada == 1:   
        if soma == 7 or soma == 11:
            return "natural"
        elif soma == 2 or soma == 3 or soma == 12:
            return "craps"  
        else:
            valor_acumulado = soma
            return "continue"
    else:
        if soma == 7:
            return "perdeu"
        elif soma == valor_acumulado:
            return "ganhou"
        else:
            return "continue"

print(""" 
--------- CRAPS ----------- 
O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
Se, na primeira jogada, você tirar 7 ou 11, você um 'natural' e ganhou. 
se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de 'craps' e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu 'Ponto'. 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
""")

print("\nVamos começar o jogo!")

status = "continue"
while status == "continue":
    jogada += 1
    input("Digite 'enter' para jogar os dados!")
    dados = arremessar_dados()
    dado1 = dados[0]
    dado2 = dados[1]
    print("Os valores dos dados foram: " + str(dado1) + " e " + str(dado2) + ", a soma é: " + str(dado1+dado2))
    status = verificar_jogada(dado1, dado2)
    if status == "natural" or status == "ganhou":
        print("Parabéns, você ganhou!")
    elif status == "craps" or status == "perdeu":
        print("Me desculpe, você perdeu")
    print(status) 
