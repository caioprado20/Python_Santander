### O manejo de exceçoes nos premite capturar e lidar com erros de maneira controlada utilizando as declarações try, except e opcionalmente finally

### TRY
"""
O bloco try contém o código que pode gerar uma exceção. Se ocorrer uma execeção dentro do bloco ty, o fluxo de execução é tranferido par o bloco except correspondente

"""
try:
    #Código que pode gerar uma exceção 
    resultado = 10/0 # DIvisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: divisão po zero")

### EXCEPT

"""
O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Voce pode ter Múltiplos blocos except para lidar com diferentes tipos de exeções.

"""
try:
    #Código que pode gerar uma exceção 
    resultado = 10/0 # DIvisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: divisão po zero")
except ValueError:
    print("Erro: Valor inválido ")   

### FINALLY 
"""
O bloco finally é opcional e é sempre, independente de ter ocorrido uma exceção ou não. É comemente utilizado para realizar tarefas de limpesa ou liberação de recursos.
"""
arquivo = None  # 1. Declara a variável previamente
try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt","r")
    conteudo = arquivo.read()
    # Realizar operações com arquivo
except FileNotFoundError:
    print("erro: Arquivo não encontrado") 
finally:
   if arquivo is not None:
        arquivo.close()
        print("Arquivo fechado com sucesso.")

