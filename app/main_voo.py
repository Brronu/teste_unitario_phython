from voo import Voo
voo1 = Voo(1, 100,50,10)
# voo2 = Voo(2,100,60,20)


disponibilidade = voo1.consultarDisponibilidade,()
print(f"Assentos disponíveis no voo 1: {disponibilidade}")


reserva_feita = voo1.fazerReserva(3)
if reserva_feita:
    print("Reserva feita com sucesso.")
else:
    print("Não há assentos suficientes para a reserva.")


cancelamento_feito = voo1.cancelarReserva(2)
if cancelamento_feito:
    print("Cancelamento feito com sucesso.")
else:
    print("Não há assentos reservados suficientes para o cancelamento.")


disponibilidade = voo1.consultarDisponibilidade()
print(f"Assentos disponíveis no voo 1: {disponibilidade}")
