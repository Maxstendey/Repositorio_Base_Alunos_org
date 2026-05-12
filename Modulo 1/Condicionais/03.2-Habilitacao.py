nome = input("Qual o seu nome? ")
idade = int(input("Qual é a sua idade?"))
possui_carteira = input("Possui carteira de motorista? \n (1-Sim / 2-Não) ")

if idade >= 18:
    if possui_carteira == "1":
        print("Pode dirigir")
    else:
        print("Não pode dirigir")
else:
    print("Menor de idade")
    