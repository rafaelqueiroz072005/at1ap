from aprovado2 import aprovado 

def test1():
    assert aprovado(10, 80, 0) == "Aprovado"

def test2():
    assert aprovado(7, 80, 80) == "Reprovado por faltas"

def test3():
    assert aprovado(10, 80, 20 ) == "Aprovado" 

def test4():
    assert aprovado(5, 80, 20) == "Precisa fazer a prova final" 

def test5():
    assert aprovado(6, 80, 20) == "Aprovado"

def test6():
    assert aprovado(6.1, 80, 0) == "Aprovado"

def test7():
    assert aprovado(5.9, 80, 0) == "Precisa fazer a prova final"





