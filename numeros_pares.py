
"""Faça um programa que imprime os numeros pares de 1 a 200
ex
`python3 numeros_pares.py`
2
4
6
8
... 
"""

n = 0

while n < 201:
    if n % 2 != 0:
        n += 1
    print(n)
    n += 1

#for n in range(1, 201):
#    if n % 2 == 0:
#        print(n)