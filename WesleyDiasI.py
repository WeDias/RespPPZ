# Wesley Dias (1º Semestre ADS-B)

# Exercício 1
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print(f'A soma de {numero1} e {numero2} é: {numero1+numero2}')

# Exercício 2
metros = int(input('Digite uma medida em metros: '))
print(f'Convertendo {metros} metros para milímetros é: {metros*1000} mm')

# Exercício 3
dias = int(input('Quantos dias: '))
horas = int(input('Quantas horas: '))
minutos = int(input('Quantos minutos: '))
segundos = int(input('Quantos Segundos: '))
print(f'O total em segundos é: {dias*86400 + horas*3600 + minutos*60 + segundos} s')

# Exercício 4
salario = float(input('Digite o seu salário atual: R$'))
aumento = float(input('Digite a porcentagem de aumento: '))
print(f'Com um aumento de R${salario * aumento/100:.2f}, Seu novo salário é de: R${salario + salario * aumento/100:.2f}')

# Exercício 5
preco_produto = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite a porcentagem de desconto: '))
print(f'O desconto é de R${preco_produto*desconto/100:.2f}, Preço a pagar R${preco_produto-preco_produto*desconto/100:.2f}')

# Exercício 6
distancia = float(input('Digite a distância a percorrer em KM: '))
velocidade = float(input('Digite a velocidade média esperada (KM/H):  '))
print(f'O tempo até o fim do trajeto é de: {distancia/velocidade:.2f} horas')

# Exercício 7
celsius = float(input('Digite a temperatura em graus Celsius: '))
print(f'Convertendo {celsius:.2f}ºC para Fahrenheit é: {1.8*celsius+32:.2f}ºF')

# Exercício 8
fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
print(f'Convertendo {fahrenheit:.2f}ºF para Celsius é: {(fahrenheit-32)/1.8:.2f}ºC')

# Exercício 9
km = float(input('Digite a quantidade de KMs percorridos: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
print(f'Total a pagar: R${60*dias + 0.15*km:.2f}')

# Exercício 10
cigarros = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos = int(input('Em Quantos anos ?'))
print(f'Você perderá {(cigarros*1/6)*(365*anos)/24:.2f} dias !')

# Exercício 11
numero = 2 ** 1000000
print(f'Há {len(str(numero))} dígitos em 2 elevado a 1 milhão')
