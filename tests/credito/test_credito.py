import pytest
from app.credito.credito import classificar_credito


@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 500, False, "renda invalida"),
        (-1, -1, False, "renda invalida"),

        (1000, -1, True, "score invalido"),
        (1000, 0, False, "reprovado"),

        (1000, 500, True, "reprovado"),
        (1000, 300, True, "reprovado"),

        (1000, 1000, False, "aprovado premium"),

        (1000, 1001, False, "score invalido"),
    ],
)
def test_classificar_credito_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(
        renda_mensal,
        score_credito,
        restrito
    ) == retorno_esperado


@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 500, False, "renda invalida"),
        (0.01, 500, False, "aprovado padrao"),

        (1000, -1, False, "score invalido"),
        (1000, 0, False, "reprovado"),

        (1000, 399, False, "reprovado"),
        (1000, 400, False, "aprovado padrao"),

        (1000, 699, False, "aprovado padrao"),
        (1000, 700, False, "aprovado premium"),

        (1000, 1000, False, "aprovado premium"),
        (1000, 1001, False, "score invalido"),
    ],
)
def test_classificar_credito_fronteiras(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(
        renda_mensal,
        score_credito,
        restrito
    ) == retorno_esperado