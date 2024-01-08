#!/usr/bin/env python3
""" Imprime a tabuada do 1 ao 10

    ---Tabuada do 1---
    1X1 = 1
    2X1 = 2
    3X1 = 3
    ...
##############################
    ---Tabuada do 2---
    2X1 = 2
    2X2 = 4
    2X3 = 6
    ...
##############################
 """
__version__ = "0.1.1"
__author__ = "Matheus"


#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Iterable (percorrivel)
numeros = list(range(1, 11))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2  in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} X {n2} = {resultado}"))
    
    print("#" * 18)
