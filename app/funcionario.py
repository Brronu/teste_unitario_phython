from datetime import date 
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def dados(self):
        return f"{self.nome} seu cargo e {self.cargo} e seu salario é {self.salario}"
    
    def registrarPonto(self):
        return f"Ponto registrada na data {date.today ()}"
        
    def descontarSalario(self, valor):
        
        if valor < 0:
            return "Operação Invalida"

        else: 
             self.salario = self.salario - valor

    def promover (self, novoCargo, novoSalario):
        self.cargo = novoCargo
        self.salario = novoSalario
        return f"promovido para {self.cargo} com salario de R$ {self.salario}"  

    def calcularBonus(self):
        bonus = self.salario * 0.1 #calculando 10% do salario
        return bonus       
        
