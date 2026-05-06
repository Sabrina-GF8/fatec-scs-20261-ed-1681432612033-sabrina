'''
*---------------------------------------------------------*
* Fatec São Caetano do Sul                                *
* Atividade em conjunto                                   *
* Autor: 1681432612033 - Sabrina Franca Costa             *
* Grupo 9 - Sabrina, Henrique Oliveira e Luiza Lima       *
* Objetivo: Colocar em prática o conceito de filas em     *
* python                                                  *
*                  Data: 27/04/2026                       *
*---------------------------------------------------------*
'''

from datetime import datetime

class Paciente:
    def __init__(self, nome, sintoma_relatado, timestamp_chegada, idade, pcd, gestante):
        self.nome = nome
        self.sintoma_relatado = sintoma_relatado
        self.timestamp_chegada = timestamp_chegada
        self.idade = idade
        self.pcd = pcd
        self.gestante = gestante
        self.emergencia = False

    def __str__(self):
        return (
            f"Sintoma: {self.sintoma_relatado} | "
            f"Idade: {self.idade} | PcD: {self.pcd} | "
            f"Gestante: {self.gestante} | "
            f"Emergencia: {'Sim' if self.emergencia else 'Nao'} | "
            f"Chegada: {self.timestamp_chegada.strftime('%H:%M:%S')}"
        )

fila_bruta = []

while True:
    nome = input("Nome: ")
    sintoma = input("Sintoma: ")
    idade = int(input("Idade: "))
    pcd = input("PcD (s/n): ").strip().lower()
    gestante = input("Gestante (s/n): ").strip().lower()

    timestamp = datetime.now()

    paciente = Paciente(nome, sintoma, timestamp, idade, pcd, gestante)
    fila_bruta.append(paciente)

    print("Paciente enfileirado!\n")

    continuar = input("Adicionar outro paciente? (s/n): ")
    if continuar.lower() != "s":
        break