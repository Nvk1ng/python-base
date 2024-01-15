# PSEUDO CODIGO

# Algoritmos

"""Sequencia de instrucoes logicas que visam obter a solucao de um problema.

problema: Ir a padaria e comprar pão:
premissa: Padaria na esquina abre fds: ate 12h, semana ate 19h, feriado(exeto natal) nao abre.

1.A padaria esta aberta?
    1. SE e feriado E NAO e natal: nao
    2. Senao, se e sabado OU domingo E antes do meio dia: sim
    3. Senao, se e dia de semana E antes das 19h: sim
    4. Senao: nao
2.Se padaria esta aberta E:
    1. Se esta chovendo: pegar guarda-chuva
    2. Se esta chovendo E calor: Pegar guarda-chuva e agua
    3. Se esta chovendo E frio: pegar guarda-chuva, blusa e botas
3.Ir a padaria:
    1. Se tem pao integral E baguete: pedir 6 de cada
    2. Senao, se tem apenas pao integral OU baguete: pedir 12
    3. Senao,  pedir 6 de qualquer pao
4. Senao
    1. Ficar em casa comendo bolacha 
"""

import ir, pegar, pedir, tem, comer, ficar

# Premissas
today = "Segunda"
hora = 15
natal = False
frio = False
nevando = True
semana = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
feriado = ["quarta"]
horario_padaria = {
    "semana": 19,
    "fds":12
}

# Algoritmo
if today in feriado and not natal:
    padaria_aberta = False
elif today not in semana and hora < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and (frio or nevando):
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuva")
        pegar("agua")
    elif chovendo:
        pegar("guarda-chuva")

    ir("padaria")

    if tem("pao int") and tem("baguete"):
        pedir(6, "pao int")
        pedir(6, "baguete")
    elif tem("pao int") or tem("baguete"):
        pedir(12, "qualquer um dos dois")
    else:
        pedir(6, "qualquer pao")
    
else:
    ficar("Em casa comendo bolacha")








