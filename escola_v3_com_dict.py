__version__ = "0.1.1"
__author__ = "Matheus Calmon"

import pprint

# Dados
escola = {
    "sala1": ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana'],
    "sala2": ['Joao', 'Antonio', 'Carlos', 'Maria', 'Isolda'],
}

aulas = {
    "ingles": ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio'],
    "musica": ['Erik', 'Carlos', 'Maria'],
    "danca": ['Gustavo', 'Sofia', 'Joana', 'Antonio'],
}

# Cria um dicionario para armazenar as criancas por sala e atividade
relatorio = {}

# Iterar sobre as atividades
for atividade, criancas_atividade in aulas.items():
  #Somente as atividades  
    relatorio[atividade] = {}
    
    # Iterar sobre as salas
    for sala, criancas_sala in escola.items():
        # Encontrar as criancas que estao na sala e tambem na atividade
        criancas_presentes = set(criancas_sala) & set(criancas_atividade)
        
        # Adicionar ao relatorio se houver criancas presentes
        if criancas_presentes:
            relatorio[atividade][sala] = list(criancas_presentes)

# Exibir o relatorio
pprint.pprint(relatorio)
