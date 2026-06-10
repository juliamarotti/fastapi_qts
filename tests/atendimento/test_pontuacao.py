from app.atendimento.pontuacao import calcular_pontuacao_atendimento, classificar_atendimento

def test_tempo_zero():
    assert calcular_pontuacao_atendimento(0, True, False) == 0


def test_tempo_negativo():
    assert calcular_pontuacao_atendimento(-3, True, False) == 0


def test_resolvido_ate_10_sem_reincidencia():
    assert calcular_pontuacao_atendimento(10, True, False) == 10


def test_resolvido_11_sem_reincidencia():
    assert calcular_pontuacao_atendimento(11, True, False) == 8


def test_resolvido_21_com_reincidencia():
    assert calcular_pontuacao_atendimento(21, True, True) == 4


def test_nao_resolvido_10_sem_reincidencia():
    assert calcular_pontuacao_atendimento(10, False, False) == 5


def test_nao_resolvido_15_com_reincidencia():
    assert calcular_pontuacao_atendimento(15, False, True) == 1


def test_nao_resolvido_25_com_reincidencia():
    assert calcular_pontuacao_atendimento(25, False, True) == 0


def test_classificacao_excelente():
    pontuacao = calcular_pontuacao_atendimento(10, True, False)
    classificacao = classificar_atendimento(pontuacao)

    assert classificacao == "Excelente"


def test_classificacao_bom():
    pontuacao = calcular_pontuacao_atendimento(11, True, False)
    classificacao = classificar_atendimento(pontuacao)

    assert classificacao == "Bom"


def test_classificacao_regular():
    pontuacao = calcular_pontuacao_atendimento(21, True, True)
    classificacao = classificar_atendimento(pontuacao)

    assert classificacao == "Regular"


def test_classificacao_critico():
    pontuacao = calcular_pontuacao_atendimento(25, False, True)
    classificacao = classificar_atendimento(pontuacao)

    assert classificacao == "Crítico"