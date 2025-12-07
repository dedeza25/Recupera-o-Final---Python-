frase = input("Digite uma frase: ")
vogais = 0

for letra in frase.lower():
    if letra in "aeiou":
        vogais += 1

print("Quantidade de vogais:", vogais)
