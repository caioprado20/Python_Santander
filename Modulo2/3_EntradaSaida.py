### ENTRADAS/SAÍDAS
"""
Em python, a entrada e saída nos permite interagir com o usauário e manipular arquivos . Podemos solicirar informação ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos externos. 
"""
### ENTRADA DE DADOS DO USUÁRIO
### Para obter informações do usuário durante a execução do programa, podemos utilizar a função input(). Esta função mostra uma mensagem na tela e espera que o usuário insira um valor.

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

print (" Olar," + nome  + "!")
print ("Você tem " + idade + "anos. ")

### Importante

"""
A função input() sempre retorna uma cadeia de texto. Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, deve realizar uma conversão explícita ultilizando funçoes int() ou float()
"""

idade2 = int(input(" Insira a sua idade"))

if idade2 >=18:
    print("Você é maior de idade.")
else:
    print(" Você é menor de idade.")    

### SAÍDA DE DADOS

"""
Para mostrar na tela, utilizamos a função print(). Esta função receve um oi mais argumentos e os mostra no console
Podemos utilizar a f-string(formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia de texto.
"""
nome2 = "Juan"
idade3 = 25


print(f"OLAR, meu nome é {nome2} e tenho {idade3} anos")