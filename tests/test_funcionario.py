from app.funcionario import Funcionario

colaborador = Funcionario("Sofia", "Gerente",3000)

def test_vericarDados():
    assert colaborador.dados() == "Sofia seu cargo e Gerente e seu salario é 3000"
    
def test_calcularBonus():
    assert colaborador.calcularBonus() >= 300

def test_registrarPonto():
    assert colaborador.registrarPonto() >= "Ponto registrada na data 08 de outumbro de 2023"