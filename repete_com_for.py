#!/usr/bin/env python3

original = [1, 2, 3]

# for loops / laço for 

dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# funcional
# list comprehension

dobrada = [n * 2 for n in original]
print(dobrada)

# dict comprehension

dados = {}
for line in open("post.txt"):
    if ':' in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()
print(dados)
