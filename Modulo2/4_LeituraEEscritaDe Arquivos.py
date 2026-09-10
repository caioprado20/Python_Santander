### LEITURA DE ARQUIVOS

"""
Para ler o conteúdo de um arquivo, primeiro devemos abri-lo utilizando a funçãoopen() em modo de leitura ("r"). depois, podemos ler o conteúdo do arquivo utilizando métodos como read() e readlines().
"""
"""
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
"""

### ESCRITA DE ARQUIVOS

"""
Para escrever dados em um arquivo, abrimos em modo de escrita("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, sei conteúdo será sobrescrito. 

"""

arquivo1 = open("dados.txt", "w")
arquivo1.write("Olar, mundo!")
with open("dados.txt", "r") as arquivo1:
    conteudo = arquivo1.read()
    print(conteudo)

arquivo1.close()



