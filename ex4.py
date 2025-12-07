soma = 0

while True:
    n = int(input("Digite um número (0 para parar): "))
    if n == 0:
        break
    if n > 0:
        soma += n

print("Soma:", soma)
