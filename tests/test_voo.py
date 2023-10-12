from app.voo import Voo

f1 = voo1(1,200,50,10)

def test_verificarconsultarDisponibilidade():
    assert f1.consultarDisponibilidade() == "O numero do voo e 1, capacidade do voo e de 200, assentos disponiveis 50, e assentos reservados e 10"