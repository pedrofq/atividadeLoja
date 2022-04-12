from Modulos.Impressao import *
from Modulos.Funcionalidades import *
from Modulos.UserInputs import *

mercadorias = []

while(True):
    imprimirMenu()
    userCheck = True
    escolhaUsuario = int(input())
    if(escolhaUsuario == 1):
        clearScreen()
        while(userCheck == True):

            nomeMercadoria = receberNomeMercadoria()
            qntMaxima = receberQntMaxima()
            qntMinima = receberQntMinima(qntMaxima)
            qntAtual = receberQntAtual(qntMaxima)
            valorUnitario = receberValorUnitario()
            
            reposicao = verificarReposicao(qntAtual, qntMinima)


            mercadorias = registroMercadoria(nomeMercadoria, qntMaxima, qntMinima, qntAtual, valorUnitario, reposicao, mercadorias)

            userCheckStr = input("Deseja incluir novas mercadorias (S/N): ")
            if(userCheckStr == "n" or userCheckStr == "N"):
                userCheck = False
            else:
                clearScreen()
    
    elif(escolhaUsuario == 2):
        clearScreen()
        mercadorias = calculoValorTotal(mercadorias)
        imprimirTabela(mercadorias)
    
    elif(escolhaUsuario == 3):
        break
    
    else:
        clearScreen()
        print("Número inválido!")




    

        
        
 

    
    


