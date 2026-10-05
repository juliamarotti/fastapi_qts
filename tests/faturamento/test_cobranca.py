import time
import pytest
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
     "valor_base, plano, dias_atraso, retorno_esperado",
    [
        (0, "BASICO", 0, -1.0),
        (-100, "BASICO", 0, -1.0),
        (100, "BASICO", -1, -1.0),

        (100, "INVALIDO", 0, -2.0),
        (100, "", 0, -2.0),

        (100, "BASICO", 0, 100.00),
        (100, "PREMIUM", 0, 90.00),
        (100, "EMPRESARIAL", 0, 80.00),

        (100, " premium ", 0, 90.00),

        (100, "BASICO", 1, 105.50),
        (100, "PREMIUM", 1, 95.45),

        (100, "EMPRESARIAL", 30, 97.00),

        (100, "BASICO", 31, 156.00),
        (100, "PREMIUM", 31, 142.90),

        (200, "EMPRESARIAL", 40, 216.00),
    ],
)
def test_processar_cobranca(
    valor_base, plano, dias_atraso, retorno_esperado
):
    resultado = processar_cobranca(
        valor_base,
        plano,
        dias_atraso
    )

    assert resultado 

def test_processar_cobranca_desempenho():
    inicio = time.perf_counter()

    resultado = processar_cobranca(100, "PREMIUM", 10)

    fim = time.perf_counter()

    tempo_execucao = fim - inicio

    assert resultado == 99.50
    assert tempo_execucao < 0.1