#!user/src/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotacao geral sobre carreira de tecnologia

$ notes.py read tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"you must specify subcommand {cmds}")
    print("CLIQUE EM SHELL ACIMA E EXECUTE `python notes.py new teste")
    sys.exit(1)

if arguments [0] not in cmds:
    print(f"invalid command {arguments[0]}")

if arguments [0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()


if arguments[0] == "new":
    title = arguments[1] # TODO: tratar execption
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n ").strip(),  
    ]

    with open (filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")