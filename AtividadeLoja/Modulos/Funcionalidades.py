import os

def registroMercadoria(nomeMercadoria, qntMaxima, qntMinima, qntAtual, valorUnitario, reposicao, mercadorias):
    novaMercadoria = {
        "Nome":nomeMercadoria,
        "qntMaxima":qntMaxima,
        "qntMinima":qntMinima,
        "qntAtual":qntAtual,
        "valorUnitario":valorUnitario,
        "valorTotal":0.00,
        "precisaReposicao":reposicao
    }
    mercadorias.append(novaMercadoria)

    return mercadorias

def calculoValorTotal(mercadorias):
    for mercadoria in mercadorias:
        qntAtual = mercadoria.get("qntAtual")
        valorUnitario = mercadoria.get("valorUnitario")
        valorTotal = qntAtual*valorUnitario
        mercadoria["valorTotal"] = valorTotal
    return mercadorias

def verificarReposicao(qntAtual, qntMinima):
    if(qntMinima > qntAtual):
        return "Sim"
    else:
        return "Não"

def clearScreen():
    os.system('cls')