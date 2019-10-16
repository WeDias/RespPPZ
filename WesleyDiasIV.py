# Wesley Dias (1º Semestre ADS-B), Lista IV

# Exercício 1a (Obs.: Não foi usado a função max ou min, o que torna este exercício válido — hahaha :D )
from random import randint

numeros = []
for c in range(0, 10):
    numeros.append(randint(1, 100))
print(f'Lista sorteada: {numeros}')
numeros.sort()
print(f'O menor número foi {numeros[0]}, e o maior foi {numeros[9]}\n')

# Exercício 1b (Obs.: Caso o Sr. não aceite a malandragem acima — hahaha :D )
from random import randint

numeros = []
menor = maior = 0
for c in range(0, 10):
    numeros.append(randint(1, 100))
    if numeros[c] > maior:
        maior = numeros[c]
        if c == 0:
            menor = maior = numeros[c]
    elif numeros[c] < menor:
        menor = numeros[c]
print(f'Lista sorteada:{numeros}\nO menor número foi {menor}, e o maior foi {maior}\n')

# Exercício 2
from random import randint

numeros = []
par = []
impar = []
for c in range(0, 20):
    aleatorio = randint(1, 100)
    numeros.append(aleatorio)
    if aleatorio % 2 == 0:
        par.append(aleatorio)
    else:
        impar.append(aleatorio)
print(f'Números sorteados:{numeros}\nNúmeros pares:{par}\nNúmeros impares: {impar}\n')

# Exercício 3 
from random import randint

vetor1 = []
vetor2 = []
vetor3 = []
for c in range(1, 21):
    aleatorio = randint(1, 100)
    if c % 2 != 0:
        vetor1.append(aleatorio)
    else: 
        vetor2.append(aleatorio)
    vetor3.append(aleatorio)
print(f'Vetor1:{vetor1}\nVetor2:{vetor2}\nVetor3:{vetor3}')

# Exercício 4
lista = []
text = '''The Python Software Foundation and the global Python community welcome and encourage participation by
everyone Our community is based on mutual respect tolerance and encouragement and we are working to help
each other live up to these principles We want our community to be more diverse whoever you are
and whatever your background we welcome you'''
text = text.lower()
text = text.split()
for c in text:
    if c[0] in 'python' or c[-1] in 'python':
        lista.append(c)
print(f'\n{lista}')

# Exercício 5
lista = []
text = '''The Python Software Foundation and the global Python community welcome and encourage participation by
everyone Our community is based on mutual respect tolerance and encouragement and we are working to help
each other live up to these principles We want our community to be more diverse whoever you are
and whatever your background we welcome you'''
text = text.lower()
text = text.split()
for c in text:
    if c[0] in 'python' and len(c) > 3 or c[-1] in 'python' and len(c) > 3:
        lista.append(c)
print(f'\nExistem {len(lista)} palavras')
