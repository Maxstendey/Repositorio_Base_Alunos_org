import os

def limpa_tela():
    os.system("cls")

def adiciona_nome(lista_nomes, nome):
    lista_nomes.append(nome)

def remover_nome(lista_nomes, nome):
    print()

def mostrar_nomes(lista_nomes):
    for nome in lista_nomes:
        print(nome)

nomes = []
while True:
    limpa_tela()  
    menu = input("Escolha sua opção:\n[1] - Listar nomes\n[2] - Adicionar nomes\n[3] - Remover nomes\n[0] - Sair\nSua opção: ")
    if menu == "0":
        break


