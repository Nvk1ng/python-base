#!/usr/bin/env python3

# while - enquanto

n = 0 
while n < 101:
    if n % 2 != 0:
        n += 1
        continue
    print(n)
    n += 1
