"""
Repete vogais

Faça um programa que pede ao usuario para que digite uma ou mais palavras e imprime cada uma das palavaras
com suas vogais duplicadas

ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra(ou enter para sair):' Bruno
'Digite uma palavra(ou enter para sair):' <Enter>
pythoon
bruunooo
"""
words = []
while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if not word:
        break

    final_word = ""
    for letter in word:
        # TODO: Remover acentuacao usando funcao
        """
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)
    """
        final_word += letter * 2 if letter.lower() in "aeiou" else letter

print(*words, sep="\n")
