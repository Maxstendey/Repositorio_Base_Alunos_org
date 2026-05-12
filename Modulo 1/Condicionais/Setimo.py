nome = input("Qual é seu nome? ")
ano = int(input("Digite o ano que você nasceu: "))

if 2026 - ano >= 18:
    print("Maior de idade")
    print("Já pode beber")
    print("Ja pode dirigir")
else:
    print("Menor de idade")
    print("n pode nada")

