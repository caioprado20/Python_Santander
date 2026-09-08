# for
frutas = ["maçã","banana","laranja"]
for fruta in frutas:
    print (fruta)
# While

contador = 0
while contador <=5:
    print(contador)
    contador +=1
### Controle de Loops
# BREAK
contador =0
while True:
    print(contador)
    contador += 1
    if contador == 5:
     break
### CONTINUE

for i in range(10):
   if i % 2 == 0:
      continue
   print(i)   

### PASS

#não faz nada???

for i in range(5):
   pass

#As estruturas de controle são ferramentas poderosas que nos permitem controlar o fluxo de execução de nossos programas. Com as estruturas condicionais (if, if-else, if-elif-else) podemos tomar decisões baseadas em condições, enquanto que com os loops (for, while) podemos repetir blocos de código várias vezes. Além disso, as instruções break, continue e pass nos fornecem um controle adicional sobre o comportamento dos loops.