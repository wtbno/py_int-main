import random
aleatorio = random.randint(0, 10)
escolha = int(input('Pense em um número de 0 a 10: '))
if aleatorio == escolha:
    print('Parabéns, você acertou')
else:
    print('Número incorreto!')
print('O número escolhido foi: {}' .format(aleatorio))
