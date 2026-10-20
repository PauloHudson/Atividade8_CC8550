import pytest

from preco import preco_final, preco_final_defeituosa


@pytest.mark.parametrize(
    ("preco", "vip", "esperado"),
    [
        (60, True, 50),
        (200, False, 200),
        (100, True, 80),
        (40, False, 50),
    ],
)
def test_preco_final(preco, vip, esperado):
    assert preco_final(preco, vip) == esperado


def test_suite_atual_mascarava_defeito():
    assert preco_final_defeituosa(60, True) == 50
    assert preco_final_defeituosa(200, False) == 200
    assert preco_final(100, True) == 80
