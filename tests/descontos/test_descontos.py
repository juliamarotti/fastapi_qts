from app.descontos.descontos import calcular_desconto

def test_valor_negativo():
    assert calcular_desconto(-50, False) == 0


def test_cliente_vip():
    assert calcular_desconto(250, True) == 200


def test_cliente_nao_vip():
    assert calcular_desconto(300, False) == 270


def test_valor_pequeno():
    assert round(calcular_desconto(0.05, False), 3) == 0.045


def test_valor_maior():
    assert calcular_desconto(500, True) == 400