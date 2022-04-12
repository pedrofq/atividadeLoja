from prettytable import PrettyTable


def imprimirMenu():
    print("Bem-vindo! Digite o número correspondente a operação: ")
    print("1 - Adicionar novos produtos")
    print("2 - Imprimir todos os produtos")
    print("3 - Sair!")

def imprimirTabela(mercadorias):
    
    x = PrettyTable()
    x.field_names = ["Nome do Produto", "Qnt. Mínima", "Qnt. Atual", "Valor Unitário", "Valor Total", "Precisa Repor?"]

    novaLinha = []

    for mercadoria in mercadorias: 
        if(len(novaLinha) > 0): #Se a lista estiver preenchida, deve ser colocada colocada em uma nova Row
            x.add_row(novaLinha)      
            novaLinha = []
        for key, value in mercadoria.items():
            if(not key == "qntMaxima"):
                novaLinha.append(value)
    x.add_row(novaLinha)

    print(x)