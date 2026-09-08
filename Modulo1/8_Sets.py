### CONJUNTOS (SETS)
"""
Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criadps utilízando a função set().
"""

### CRIAÇÃO E OPERAÇÕES BÁSICAS

frutas = {"maça", "banana","laranja"}
numeros = set([1,2,3,4,5])

"""
Os conjuntos suportam operações matemáticas de conjuntos, como união(|), a interseção(&),a diferença (-), diferenção simétrica(^) 
"""
conjunto1 = {1,2,3}
conjunto2 = {3,4,5}
união = conjunto1|conjunto2
print(união) # Imprime {1,2,3,4,5}

interseção = conjunto1 & conjunto2
print(interseção) # Imprime {3}

diferença = conjunto1 - conjunto2
print(diferença) #  {1,2}

diferença_simetrica = conjunto1 ^ conjunto2
print(diferença_simetrica) # imprime os conjuntos somados, excluindo o elemento repetido

### MÉTODOS DE CONJUNTOS
"""
add(elemento): adiciona um elemento ao conjunto
remove(elemento) : remove um elemento do conjunto. Se o elemento não existir, gero um erro
discard(elemento): remove um elemento do conjunto se estiver presente. se o elemento não existir, não faz nada.
clear(): remove todos os elemtentos do conjunto

"""

frutas.add("pera")
print(frutas) # Imprime frutas com a pera
frutas.remove("banana")
print(frutas) # Imprime {"maça","laranja", "pera"}
frutas.discard("uva")
print(frutas) # não faz nada pois o elemento uva não existe

frutas.clear()
print(frutas) #imprime set()