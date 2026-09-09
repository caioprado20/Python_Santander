### FUNÇOES
"""
funçoes são blocos de código reutilizáveis que nos permitem encapsular tarefas específicas e executá-las quando necessário. As funçoes nos ajudam a organizar nosso código, evitar a repetição e fazer com que nossos programas sejam mais modulares e fácies de manter.

"""
### DEFINIÇÃO E CHAMADAS DE FUNÇÕES
def saudacao():
    print("Olar, mundo!")

saudacao()# Imprime "Olar mundo"

### PARÂMETROS E ARGUMENTOS

# Funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. OS parâmetros são especifícados dentro de parênteses na definição da função.

def saudacao2 (nome):
    print (f"Olar,{nome}!")

saudacao2("joao") # Imprime "olá joao"
saudacao2("maria") # Imprime "olá maria"

### VALORES RETORNO

# as funçoes podem retornar valores usando a palavra-chave return. O valor de retorno pode ser usado pelo código que chama a função.

def soma (a,b):
    return a+b
resultado = soma(3,4)
print (resultado) # Imprime 7

### FUNÇOES ANÔNIMAS (LAMBDA)

# Python permite criar funçoes anônimas ou funçoes lambda, que são funçoes sem nome definidas em uma única linha. são comumente usadas para funçoes pequenas e concisas.

quadrado = lambda x: x**2
print(quadrado(5)) # Imprime 25

### ESCOPO DAS VARIÁVEIS (LOCAL VS GLOBAL)

# As variáveis definidas detro de uma função têm um escopo local, o que significa que só são acessiveis dentro da função. Por outro lado, as variáveis definidas fora de qualque função têm um escoppo global

def funcao():
    variavel_local = 10
    print(variavel_local) # Acessível dentro da função

variavel_global = 20
def funcao2 ():
    print(variavel_global) # Acessível de qualquer lugar 

funcao() # Imprime 10
funcao2 () # imprime 20
print(variavel_global) # Imprime 20
#print(variavel_local) # gera um erro, a variável não está definida neste escopo

### DOCUMENTAÇÃO DE FUNÇOES(DOCSTRINGS)

"""
É uma boa pratica documentar nossas funçoes utilizando docstrings. As docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. São colocadas imediatamente após a definição da função e são encerrados entre pasas duplastriplas(tipo essa daqui)



"""
def area_retangulo (base, altura):
    """
    calcula a área de um retangulo

    Args: 
        base (float): A base do retangulo.
        altura(float): A autura do retÂngulo
    returns:
        float : A area do retângulo.
    """
    return base *altura        

### FUNÇOES COM NÚMERO VARIÁVEL DE ARGUMENTOS

"""
O Python permite definir funçoes que aceitem um número variável de argumentos. Isso é feito ultilizando o operador * antes do nome do parâmetro
"""

def soma_variavel(*numeros):
    total = 0 
    for numero in numeros:
        total += numero
    return total

print (soma_variavel(1,2,3))  # Imprime 6   
print (soma_variavel(4,5,6,7)) # Imprime 22