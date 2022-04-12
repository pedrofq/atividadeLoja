from Modulos.Validacoes import *

def receberNomeMercadoria():
    nomeMercadoria = input("Digite o nome da mercadoria: ")
    return nomeMercadoria

def receberQntMaxima():
    validador = False
    while (validador == False):
        qntMaxima = int(input("Digite a quantidade MÁXIMA dessa mercadoria: "))
        validador = validarQntMaxima(qntMaxima)
    return qntMaxima

def receberQntMinima(qntMaxima):
    validador = False
    while(validador == False):
        qntMinima = int(input("Digite a quantidade mínima dessa mercadoria: "))
        validador = validarQntMinima(qntMinima, qntMaxima)
    return qntMinima

def receberQntAtual(qntMaxima):
    validador = False
    while(validador == False):
        qntAtual = int(input("Digite a quantidade atual dessa mercadoria: "))
        validador = validarQntAtual(qntAtual, qntMaxima)
    return qntAtual

def receberValorUnitario():
    validador = False
    while(validador == False):
        valorUnitario = float(input("Digite o valor unitário dessa mercadoria: "))
        validador = validarValorUnitario(valorUnitario)
    return valorUnitario