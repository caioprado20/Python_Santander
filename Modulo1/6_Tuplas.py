### Tuplas
### Uma tupla é uma estrutura de dados imutavel e ordenada que permite armazenar uma coleção de elementos . Os elementos de uma tupla são encerados entre parêtes() e separados por vírgulas.
# Acesso
ponto = (3,4)

print (ponto[0])
print (ponto[1])

### Ao contarios das listas, a tupla não pode ser modificados, ou seja, não podem serem adicionados o eliminados qualquer elementos depois de sua iniciação.

### Métodos tuplas

# count(elemento): Devolve o número de vezes que um elemento aparece na tupla.
# index(elemento): Devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca
#len(tupla) : embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla

minha_tupla = (1, 2, 3 ,2 ,4, 2)


print (minha_tupla.index(2))
print (minha_tupla.index (2, 2))
print (minha_tupla.index(2, 2, 4))