def pode_embarcar_defeituosa(cartao, documento, grupo_chamado, prioridade):
    if cartao and documento and grupo_chamado or prioridade:
        return True
    return False


def pode_embarcar(cartao, documento, grupo_chamado, prioridade):
    if cartao and documento and (grupo_chamado or prioridade):
        return True
    return False
