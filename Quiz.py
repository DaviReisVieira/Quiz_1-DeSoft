########################################################################################################################
########################################----Autor: Davi Reis Vieira de Souza----########################################
################################################----Quiz nº1 DeSoft----#################################################
########################################################################################################################

###################################################----QUESTÃO 1-----###################################################

import math

def calcula_elongacao(A,Fi,w,t):
    Fi = math.radians(Fi)
    w = math.radians(w)
    return A*math.cos(Fi + w*t)

print(calcula_elongacao(2,90,45,2))

###################################################----QUESTÃO 2-----###################################################

p1 = input("Está se movendo? (n/s)")
if p1=='n':
    p1 = input("Deveria estar parado? (n/s)")
    if p1=='n':
        print('WD-40')
    elif p1=='s':
        print('Sem problemas!')
elif p1 =='s':
    p1 = input("Deveria se mover? (n/s)")
    if p1=='n':
        print('Silver tape')
    elif p1=='s':
        print('Sem problemas!')

###################################################----QUESTÃO 3-----###################################################

lista1 = [10, 12, 5, 1]
lista2 = [10, 12, 1, 5]
lista3 = [1, 17, 3]
lista4 = [1, 16, 3, 5]

def monta_mala(lista):
    i=0
    somavalores=0
    listanova=[]
    while i<len(lista):
        somavalores+=lista[i]
        if somavalores <= 23:
            listanova.append(lista[i])
            i+=1
        else:
            break
    return listanova

print(monta_mala(lista1))

###################################################----QUESTÃO 4-----###################################################

def verifica_quadrado_perfeito(n):
    ni=1
    while True:
        n=n-ni
        ni+=2
        if n == 0:
            return True
        elif n <= 0:
            return False

print(verifica_quadrado_perfeito(16))

###################################################----QUESTÃO 5-----###################################################

from random import randint

Dado1 = randint(1, 10)
Dado2 = randint(1, 10)
SomaDados = Dado1+Dado2
Dinheiro=10
Chutes=0

fase_inicial_n1 = int(input("Escolha um número:"))
fase_inicial_n2 = int(input("Escolha um número maior ou igual ao anterior:"))

if SomaDados < fase_inicial_n1:
    print('Soma menor')
elif SomaDados > fase_inicial_n2:
    print('Soma maior')
else:
    print('Soma no meio')

print(Dinheiro)

fase_chutes_n1 = int(input("Qte de chutes para comprar(1 chute/1 dinheiro):"))

Dinheiro-=fase_chutes_n1
Chutes=fase_chutes_n1

while Chutes > 0:
    fase_chutes_chute = int(input("Chute um número:"))
    if fase_chutes_chute == SomaDados:
        Dinheiro+=5*Dinheiro
        break
    else:
        Chutes-=1

print("Você terminou o jogo com {0} dinheiros" .format(Dinheiro))
