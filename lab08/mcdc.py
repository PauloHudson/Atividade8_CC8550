from itertools import combinations, product


def regra(cartao, documento, grupo_chamado, prioridade):
    return cartao and documento and (grupo_chamado or prioridade)


def pares_independentes(decisao, n):
    """Retorna pares de linhas que demonstram a independência de cada condição."""
    if len(decisao) != 2**n:
        raise ValueError("a tabela deve ter 2**n linhas")

    linhas = list(product((False, True), repeat=n))
    pares = {condicao: [] for condicao in range(n)}
    for primeira, segunda in combinations(range(len(linhas)), 2):
        diferentes = [
            indice
            for indice in range(n)
            if linhas[primeira][indice] != linhas[segunda][indice]
        ]
        if len(diferentes) == 1 and decisao[primeira] != decisao[segunda]:
            pares[diferentes[0]].append((primeira, segunda))
    return pares


def mcdc_sets():
    """Enumera os conjuntos MC/DC mínimos da regra de embarque."""
    linhas, decisoes = tabela_regra()
    pares = pares_independentes(decisoes, 4)
    conjuntos = []
    for indices in combinations(range(len(linhas)), 5):
        if all(
            any(primeira in indices and segunda in indices for primeira, segunda in pares[condicao])
            for condicao in range(4)
        ):
            conjuntos.append([linhas[indice] for indice in indices])
    return conjuntos


def tabela_regra():
    linhas = list(product((False, True), repeat=4))
    return linhas, [regra(*linha) for linha in linhas]
