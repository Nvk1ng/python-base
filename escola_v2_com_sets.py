#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividade.
imprimir a lista de criancas agrupadas por sala que 
frequentam cada uma das atividades.    
"""
__version__ = "0.1.1"
__author__ = "Matheus Calmon"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos","Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("ingles", aula_ingles),
    ("musica", aula_musica),
    ("danca", aula_danca),
]

# Listar alunos em cada atividade por sala
 
for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    
    #sala1 que tem intersecao com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print(f"{nome_atividade} sala1 ", atividade_sala1)
    print(f"{nome_atividade} sala2 ", atividade_sala2 )
    print()
    print("#" * 40)
