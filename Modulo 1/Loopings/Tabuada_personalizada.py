

numero2 = int(input("Digite o primeiro número: "))
C = int(input("Digite onde deseja comçar a tabuada: "))
final = int(input("Digite onde deseja terminar a tabuada: "))

while C <= final:
    print(f" {C} x {numero2} = {C * numero2}")
    C += 1