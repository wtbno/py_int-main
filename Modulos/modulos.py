#Importando bliotecas
# import math
import emoji
from math import sqrt, ceil
# import bebida => generalista
# from math import ceil
# from bebida import cafe => especifico


numero = int(input('Insira um número: '))
raiz = sqrt(numero)
print('A raiz de {} é igual a {}' .format(numero, ceil(raiz)))
print(emoji.emojize('Olá mundo :sunglasses'))