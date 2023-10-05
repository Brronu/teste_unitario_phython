from funcionario import Funcionario
import os
f1 = Funcionario("pedro", "Cafetão", 50000)

# print(f1.dados())
# print(f1.registrarPonto())

# f1.descontarSalario(50)
# print(f1.dados())

print(f1.promover("Pastor",305000))

os.system("cls")
print(f1.calcularBonus())