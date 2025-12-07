qtd = int(input("Quantos alunos? "))

nomes = []
notas = []

for i in range(qtd):
    nomes.append(input("Nome: "))
    notas.append(float(input("Nota: ")))

print("\nAlunos e notas:")
for i in range(qtd):
    print(nomes[i], "-", notas[i])

print("\nAprovados:")
for i in range(qtd):
    if notas[i] >= 6:
        print(nomes[i])
