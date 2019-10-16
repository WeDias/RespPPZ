# Wesley Dias (1º Semestre ADS-B), Lista II

# Exercício 1
lado1 = int(input('Digite o tamanho do lado 1: '))
lado2 = int(input('Digite o tamanho do lado 2: '))
lado3 = int(input('Digite o tamanho do lado 3: '))
if lado2-lado3 < lado1 < (lado2+lado3) and lado1-lado3 < lado2 < (lado1+lado3) and lado1-lado2 < lado3 < (lado1+lado2):
    if lado1 == lado2 == lado3:
        print('Pode formar um triângulo equilátero')
    elif lado1 != lado2 != lado3:
        print('Pode formar um triângulo escaleno')
    else:
        print('Pode formar um triângulo Isósceles')
else:
    print('Não pode formar um triângulo')

# Exercício 2
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 and ano != 0 or ano % 400 == 0 and ano != 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')

# Exercício 3
peso = int(input('Digite o peso total de peixes em KG: '))
if peso > 50:
    excesso = peso-50
    multa = excesso*4
    print(f'Com um excesso de {excesso}KG a multa será de R${multa:.2f}')
else:
    excesso = multa = 'ZERO'
    print(f'Excesso: {excesso}. Multa: {multa}.')

# Exercício 4
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n2 <= n1 >= n3:
    print(f'O maior número foi {n1}')
elif n1 <= n2 >= n3:
    print(f'O maior número foi {n2}')
else:
    print(f'O maior número foi {n3}')

# Exercício 5
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n2 <= n1 >= n3:
    print(f'O maior número foi: {n1}')
elif n1 <= n2 >= n3:
    print(f'O maior número foi: {n2}')
elif n1 <= n3 >= n2:
    print(f'O maior número foi: {n3}')
if n2 >= n1 <= n3:
    print(f'O menor número foi: {n1}')
elif n1 >= n2 <= n3:
    print(f'O menor número foi: {n2}')
elif n1 >= n3 <= n2:
    print(f'O menor número foi: {n3}')

# Exercício 6
ganho = float(input('Digite seu ganho R$ por hora: '))
horas = int(input('Digite quantas horas foram trabalhadas no mês: '))
salbruto = ganho * horas
ir = salbruto * 11/100
inss = salbruto * 8/100
sindicato = salbruto * 5/100
salliquido = salbruto - ir - inss - sindicato
print(f'Seu salário bruto neste neste mês foi de R${salbruto:.2f}')
print(f'Será descontado para o imposto de renda o valor de R${ir:.2f}')
print(f'Será descontado para o INSS o valor de R${inss:.2f}')
print(f'Será descontado para o sindicato o valor de R${sindicato:.2f}')
print(f'Seu salário líquido será de R${salliquido:.2f}')

# Exercício 7
m2 = int(input('Digite a quantidade de metros quadrados a ser pintados: '))
if m2 <= 54:
    print(f'Compre 1 lata de tinta, preço: R$80,00')
else:
    latas = m2 // 54
    if m2 % 54 > 0:
        latas += 1
    print(f'Compre {latas} latas de tinta, preço: R${latas*80:.2f}')
