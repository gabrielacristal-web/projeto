# Programa de consumo de energia
# Autor: Gabriela Cristal

# Entrada
print("\n--- CONSUMO DE ENERGIA ---")
nome = input("\nDigite o nome do eletrodoméstico: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
tempo = float(input("Qual o tempo médio de uso diário (em horas)? "))

# Processamento
consumoMensal = (potencia * tempo * 30) / 1000
custo = consumoMensal * 0.75  # dica valor fixo de R$ 0,75 por kWh

# Saída
print("\n--- RESULTADO ---")
print(f"\nAparelho: {nome}")
print(f"Consumo estimado: {consumoMensal} kWh/mês")
print(f"Custo estimado: R$ {custo}\n")