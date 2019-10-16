# Wesley Dias (1º Semestre ADS-B), Lista III

# Exercício 1
while True:
    nota = input('Digite uma nota: ')
    if not nota.isnumeric():
        print('APENAS NÚMEROS ENTRE 0 E 10 !')
    else:
        if 10 >= int(nota) >= 0:
            print('OK!')
            break
        print('APENAS NOTAS ENTRE 0 E 10 ! ')

# Exercício 2
while True:
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    if usuario == senha:
        print('ERRO! Usuário e senha iguais. Digite novamente.')
    else:
        print('OK!')
        break

# Exercício 3
pais_a = 80000
pais_b = 200000
cont = 0
while True:
    if pais_a >= pais_b:
        print(f'Em {cont} anos o paísA passará o paisB (PaísA= {int(pais_a)} pessoas) (PaísB= {int(pais_b)} pessoas)')
        break
    else:
        pais_a += pais_a*3/100
        pais_b += pais_b*1.5/100
        cont += 1

# Exercício 4
num = int(input('Digite um número: '))
f1 = f2 = fn = 1
if 3 > num > 0:
    fn = 1
else:
    for contador in range(2, num):
        fn = f1 + f2
        f1 = f2
        f2 = fn
print(f'Na sequência de fibonacci f{num} corresponde: {fn}')

# Exercício 5
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num2 > num1:
    maior = num2
    menor = num1
else:
    maior = num1
    menor = num2
while maior % menor != 0:
    resto = maior % menor
    maior = menor
    menor = resto
print(f'O MDC de {num1} e {num2} é: {menor}')
