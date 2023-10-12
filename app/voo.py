class Voo:
    def __init__(self,numeroVoo, capacidade, assentosDisponiveis, assentosReservados):
        self.numeroVoo = numeroVoo
        self.capacidade = capacidade
        self.assentosDisponiveis = assentosDisponiveis
        self.assentosReservados =assentosReservados
        self.assentosReservados = 0

    def consultarDisponibilidade(self):
        return self.assentosDisponiveis

    def fazerReserva(self, quantidade):
        if quantidade <= self.assentosDisponiveis:
            self.assentosDisponiveis -= quantidade
            self.assentosReservados += quantidade
            return True
        else:
            return False

    def cancelarReserva(self, quantidade):
        if quantidade <= self.assentosReservados:
            self.assentosDisponiveis += quantidade
            self.assentosReservados -= quantidade
            return True
        else:
            return False
