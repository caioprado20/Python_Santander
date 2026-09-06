### Listas
frutas = ["maça", "banana", "laranja"]

print(frutas[0])
print(frutas[1])
print(frutas[2])

frutas.append("pera")
print(frutas)

frutas.insert(1,"uva")
print(frutas)

frutas.remove("banana")
print(frutas)

frutas_removida = frutas.pop(2)
print(frutas)
print(frutas_removida)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

numeros = [1,2,3,4,5]
quadrados = [x ** 2 for x in numeros if x % 2==0]
print (quadrados)