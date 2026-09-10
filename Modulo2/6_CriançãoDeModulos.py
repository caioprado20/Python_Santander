### CRIAR E UTILIZAR MÓDULOS PERSONALIZADOS
"""
Para criar módulos personalizados, simplesmente criamos um novo arquivo Python com o nome desejado e fefinimos as funçoes, classes e variáveis que queremos incluir no módulo. Por exemplo, criamos um arquivo(no mesmo diretoório on estamos executnado Pytohn) Chamado meu_modulo.py co o seguinte conteudo
"""

import meu_modulo
meu_modulo.saudar("Caio") # imprime "OLAR , Caio"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado) # Imprime 8

import operacoes
import utilidades

resultado = operacoes.somar(5 ,3)
utilidades.imprimir_mesagem (F"O resultado da soma é :{resultado}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mesagem(f"Olar, {nome}!")