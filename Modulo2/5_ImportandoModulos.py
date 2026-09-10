### IMPORTANDO MÓDULOS
"""
Em Python, um módulo é um arquivo qie contém definiçoes de funçoes, classes e variáveis que pode ser utilizadas em outros programas. A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente. Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.
"""
### IMPORTAR MÓDULO
"""
Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. Podemos importar um módulo ou funçoes específicas de um módulo. 
"""

import math

resultado = math.sqrt(25)
print(resultado) # imprime 5.0


import random
import datetime

numero_aleatorio = random.randint(1,10)
print(numero_aleatorio) # Imprime um número inteiro aleatório entre 1 e 10

data_atual = datetime.datetime.now()
print(data_atual)# Imprime a data e a hora atual