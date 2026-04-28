'''
*---------------------------------------------------------*
* Fatec São Caetano do Sul                                *
* Filas                                                   *
* Autor: 1681432612033 - Sabrina Franca Costa             *
* Objetivo: Programar um sistema de impressão usando      *
* filas e prioridades em python                           *
*                  Data: 28/04/2026                       *
*---------------------------------------------------------*
'''


fila_aluno = []
fila_adm = []
fila_final = []

def adicionar():
    nome = input("Nome do arquivo: ")
    total_paginas = int(input("Total d paginas: "))
    tipo = input("Tipo (ADM ou ALUNO): ").upper()

    item = {"nome": nome, "paginas": total_paginas}

    if tipo == "ADM":
        fila_adm.append(item)
        print("Arquivo adicionado na fila(adm)")

    elif tipo == "ALUNO":
        fila_aluno.append(item)
        print("Arquivo adicionado na fila (aluno)")

    else:
        print("Digite um tipo válido. Ex: 'ADM' ou 'ALUNO'")

def reorganizar():
    global fila_final

    if fila_final:
        print("Já há uma fila final. Esvazie ela antes de reorganizar novamente.")
        return

    fila_final.extend(fila_adm)
    fila_final.extend(fila_aluno)

    fila_adm.clear()
    fila_aluno.clear()

    print("Filas reorganizadas.")

def listar():
    print("\n--- FILA - ADM ---")
    print(fila_adm if fila_adm else "Vazia")

    print("\n--- FILA - ALUNO ---")
    print(fila_aluno if fila_aluno else "Vazia")

    print("\n--- FILA FINAL ---")
    print(fila_final if fila_final else "vazia")

def consumir():
    if not fila_final:
        print("Fila final vazia. Você deve reorganizar primeiro.")
        return

    print("\nImprimindo...\n")

    while fila_final:
        atual = fila_final.pop(0)
        print(f"Imprimindo: {atual['nome']} ({atual['paginas']} paginas)")

    print("\nFila consumida.")

while True:
    print("\n----- MENU ------")
    print("1 - Adicionar arquivo")
    print("2 - Reorganizar")
    print("3 - Listar filas")
    print("4 - Consumir fila")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar()

    elif opcao == "2":
        reorganizar()

    elif opcao == "3":
        listar()

    elif opcao == "4":
        consumir()

    elif opcao == "0":
        print("Finalizando...")
        break

    else:
        print("Opçao invalida.")