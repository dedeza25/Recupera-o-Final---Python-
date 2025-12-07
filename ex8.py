qtd = int(input("Quantos números? "))
numeros = []

for i in range(qtd):
    n = int(input("Digite um número: "))
    numeros.append(n)

print("Maior:", max(numeros))
print("Menor:", min(numeros))
print("Quantidade:", len(numeros))
