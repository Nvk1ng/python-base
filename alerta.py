""" 
Alarme de temperatura

faça um script que pergunta ao usuario qual a temperatura atual e o indice de umidade 
do ar sendo que caso sera exibida uma mensagem de alerta dependendo das condicoes:

temp maior que 45: ALERTA!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: Frio extremo
"""
import sys
import logging
log = logging.Logger("Alerta")

info = {
    "temperatura": None,
    "umidade": None
}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"qual a {key} :").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("ALERTA!!! Perigo de calor extremo")
elif temp * 3 >= umidade:
    print("ALERTA!!! Perigo de calor umido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp <= 10:
    print("Frio")
elif temp < 0:
    print("Frio extremo !!!")

