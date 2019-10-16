# Wesley Dias (1º Semestre ADS-B), Lista XIV
# Também conhecida como a última lista. Não sei se isso é bom ou ruim, mas cheguei até aqui !

# !/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras para listas

# D. Dada uma lista de números retorna uma lista sem os elementos repetidos


def remove_iguais(nums):
    res = []
    for c in range(len(nums)):
        if res.count(nums[c]) == 0:
            res.append(nums[c])
    res.sort()
    return res


# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar


def cripto(frase):
    frase = frase.split()
    crip = []
    txt = ''
    for palavra in frase:
        palavracrip = ''
        for letra in palavra:
            if palavracrip.count(letra) == 0:
                palavracrip += letra
        palavracrip = sorted(palavracrip)
        crip.append(palavracrip)
    for palavra in crip:
        for letra in palavra:
            txt += letra
        txt += ' '
    return txt.rstrip()


# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2


def derivada(coef):
    res = []
    for n in range(len(coef)):
        if n > 0:
            res.append(coef[n] * n)
    return res


# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# Não vale converter a lista em número para somar diretamente


def soma(n1, n2):
    u = 0
    res = []
    for c in range(len(n1)):
        if (n1[c] + n2[c]) > 9:
            res.append((n1[c] + n2[c] + u) % 10)
            u = ((n1[c] + n2[c] + u) // 10)
        else:
            res.append(n1[c] + n2[c] + u)
            u = 0
    if u != 0:
        res.append(u)
    return res


# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é são uma é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False


def anagrama(s1, s2):
    situ = False
    s1, s2 = sorted(s1), sorted(s2)
    if s1 == s2:
        situ = True
    return situ


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))


def main():
    print('remove_iguais')
    test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
    test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
    test(remove_iguais([]), [])

    print()
    print('cripto')
    test(cripto('ana e mariana gostam de banana'),
         'an e aimnr agmost de abn')
    test(cripto('Batatinha quando nasce esparrama pelo chão'),
         'Bahint adnoqu acens aemprs elop choã')

    print()
    print('derivada de polinômio')
    test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
    test(derivada([4, 16, 1]), [16, 2])

    print()
    print('soma em listas invertidas')
    test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
    test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])

    print()
    print('anagrama')
    test(anagrama('aberto', 'rebato'), True)
    test(anagrama('amor', 'roma'), True)
    test(anagrama('ramo', 'amor'), True)
    test(anagrama('baba', 'aba'), False)
    test(anagrama('casa', 'cassa'), False)


if __name__ == '__main__':
    main()
