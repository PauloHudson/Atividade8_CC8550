import pytest

from senha import forca


@pytest.mark.parametrize(
    ("senha", "esperada"),
    [
        ("curta", "fraca"),
        ("abcdefgh", "media"),
        ("12345678", "forte"),
        ("!!!!aaaa", "forte"),
        ("a1b2c3d4!", "forte"),
    ],
)
def test_caminhos_e_lacos(senha, esperada):
    assert forca(senha) == esperada
