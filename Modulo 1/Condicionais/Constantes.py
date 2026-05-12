TAXA_SERVICO = 0.004
PERCENTUAL_IMPOSTO_RENDA_4 = 0.25
PERCENTUAL_IMPOSTO_RENDA_3 = 0.2
PERCENTUAL_IMPOSTO_RENDA_2 = 0.15
PERCENTUAL_IMPOSTO_RENDA_1 = 0.1
FAIXA_SALARIAL_4 = 10000
FAIXA_SALARIAL_3 = 7500
FAIXA_SALARIAL_2 = 5000
FAIXA_SALARIAL_1 = 2500

print("calculadora de impostos")

salario_base = float(input("Digite o quanto vc ganha: "))

if salario_base > 10000:
    imposto = salario_base * (FAIXA_SALARIAL_4 + PERCENTUAL_IMPOSTO_RENDA_4)

elif salario_base > 7500:
    imposto = salario_base * (FAIXA_SALARIAL_3 + PERCENTUAL_IMPOSTO_RENDA_3)
 
elif salario_base > 5000:
    imposto = salario_base * (FAIXA_SALARIAL_2 + PERCENTUAL_IMPOSTO_RENDA_2)

elif salario_base > 2500:
    imposto = salario_base * (FAIXA_SALARIAL_1 + PERCENTUAL_IMPOSTO_RENDA_1)
else:
    imposto = 0
    taxa_conveniencia = 0

print(f"para a sua faixa salarial o imposto é: {imposto}")