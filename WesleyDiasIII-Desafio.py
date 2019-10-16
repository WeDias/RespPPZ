# Wesley Dias (1º Semestre ADS-B), Lista IIIb—Desafios!
# Quero nota a mais por ter feito isso !

# Exercício 1
num = int(input('Digite um número: '))
cont = verificador = 0
while True:
    cont += 1
    resultado = cont * (cont + 1) * (cont + 2)
    if resultado == num:
        verificador = 1
        print(f'{num} é triangular')
        break
    elif resultado > num:
        break
if verificador == 0:
    print(f'{num} não é triangular')

# Exercício 2
notas = 50, 20, 10, 5, 2, 1
conta = int(input('Valor da conta a pagar: R$'))
pagamento = int(input('Valor do pagamento: R$'))
troco = pagamento - conta
print(f'Troco: R${troco}\n')
for cedulas in notas:
    if troco // cedulas > 0:
        print(f'{troco//cedulas} Notas de R${cedulas}')
    troco = troco % cedulas

# Exercício 3
verificador = 0
n = int(input('Digite um número interio positivo: '))
for c in range(1, n+1):
    if n % c == 0:
        verificador += 1
if verificador == 2:
    print(f'{n} É um número primo !')
else:
    print(f'{n} Não é um número primo !')

# Exercício 4
num = int(input('Digite um número inteiro positivo: '))
div = 2
mult = []
while num != 1:
    if num % div == 0:
        num = num//div
        mult.append(div)
    else:
        div += 1
print(f'O número fatorado é: ', end='')
for c, n in enumerate(mult):
    if c == len(mult)-1:
        print(n)
    else:
        print(n, end='x')

# Exercício 5a
inverso = []
num = int(input('Digite um número inteiro positivo: '))
for digitos in str(num):
    inverso.insert(0, digitos)
print(f'O inverso desse número é: ', end='')
for digitos in inverso:
    print(digitos, end='')
print()

# Exercício 5b — EU NÃO FAÇO IDEIA DO POR QUE NÃO FIZ ESSE ANTES... ERA MAIS FÁCIL!
num = int(input('Digite um número inteiro positivo: '))
print(f'O inverso desse número é: ', end='')
for digitos in range(len(str(num)), 0, -1):
    print(str(num)[digitos-1], end='')
