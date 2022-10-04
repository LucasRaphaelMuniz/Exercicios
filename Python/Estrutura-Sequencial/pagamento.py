nome = input("Nome: ")
valor = float(input("Valor por hora: "))
horasTrab = float(input("Horas Trabalhadas: "))

pagamento = valor * horasTrab

print(f"O pagamento para {nome} deve ser R$ {pagamento:.2f} ")