def validarQntMaxima(qntMaxima):
    if(qntMaxima > 0):
        return True
    else:
        print("Quantidade máxima deve ser maior que 0")
        return False

def validarQntMinima(qntMinima, qntMaxima):
    if(qntMinima <= qntMaxima and qntMinima >= 0):
        return True
    else:
        print("Digite valor maior que 0 e menor ou igual a quantidade máxima (%d)." %(qntMaxima))
        return False

def validarQntAtual(qntAtual, qntMaxima):
    if(qntAtual <= qntMaxima and qntAtual >= 0):
        return True
    else:
        print("Digite valor maior que 0 e menor ou igual a quantidade máxima (%d)." %(qntMaxima))
        return False

def validarValorUnitario(valorUnitario):
    if(valorUnitario > 0):
        return True
    else:
        print("Digite valor maior que 0.")
        return False