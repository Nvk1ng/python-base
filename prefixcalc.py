#!/usr/bin/ env pthon3

"""Calculadora prefix.

Funciomaneto:

[operacao] [n1] [n2]

operacoes:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2 
7

$ prefixcalc.py mul 10 5 
50

$prefixcalc.py 
opercao: sum
n1: 5
n2: 4 
9
""" 
__version__ = "0.1.0"

import sys
from wsgiref import validate
arguments = sys.argv[1:]

if not arguments:
    operation = input("Opercao:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Numero de argumentos invalidos")
    print("ex: `sum 5 5 `") 
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum","sub", "mul", "div")
if operation not in valid_operations:
    print("Operacao Invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero invalido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

# TODO: Usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2 
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2  
print(f"O resultado é {result}")













