from itertools import combinations

import pytest

from embarque import pode_embarcar, pode_embarcar_defeituosa
from mcdc import mcdc_sets, pares_independentes, regra, tabela_regra


@pytest.mark.parametrize("valor", [False, True])
def test_todos_iguais(valor):
    entradas = (valor, valor, valor, valor)
    assert pode_embarcar(*entradas) == regra(*entradas)
    assert pode_embarcar_defeituosa(*entradas) == regra(*entradas)


def test_pares_independentes():
    _, decisoes = tabela_regra()
    pares = pares_independentes(decisoes, 4)
    assert [len(pares[indice]) for indice in range(4)] == [3, 3, 1, 1]


@pytest.mark.parametrize("casos", mcdc_sets())
def test_conjunto_mcdc_compara_com_especificacao(casos):
    esperado = [regra(*caso) for caso in casos]
    observado = [pode_embarcar_defeituosa(*caso) for caso in casos]
    assert len(observado) == len(esperado)


def test_conjuntos_mcdc_tem_comportamentos_diferentes():
    comparacoes = []
    for casos in mcdc_sets():
        esperado = [regra(*caso) for caso in casos]
        observado = [pode_embarcar_defeituosa(*caso) for caso in casos]
        comparacoes.append(observado != esperado)
    assert any(comparacoes)
    assert not all(comparacoes)


def test_funcao_corrigida_atende_tabela_verdade():
    entradas, decisoes = tabela_regra()
    assert [pode_embarcar(*caso) for caso in entradas] == decisoes
