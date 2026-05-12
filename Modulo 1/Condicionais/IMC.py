nome = input("Digite o seu nome: ")
peso_usuario = float(input("Digite o seu peso: "))
altura_usuario = float(input("Digite a sua altura: "))

IMC = peso_usuario / (altura_usuario * altura_usuario)
print(IMC)

if  IMC < 18.5:
    print("Abaixo do peso")
elif IMC <= 24.9:
    print("peso normal")
elif IMC <= 29.9:
    print("Sobrepeso")
elif IMC <= 34.9:
    print("Obesidade Grau 1")
elif IMC <= 39.9:
    print("Obesidade Grau 2")
elif IMC < 40: 
    print("Obesidade Grau 3 (mórbida)") 

