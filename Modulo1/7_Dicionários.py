## Dicionários
### Dicionários são uma extrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor. Cada elementeo em um dicionário consiste em uma chave única e seu valor corespondete. Os dicionários são delimitados por chaves{}, e os  pares chave-valor são separados por vírgula.

### INICIALIZAÇÂO
### para criar um dicionário, utilize chaves e separe as chaves e valores com dois pontos.

pessoa ={"nome": "joao", "idade": 25, "cidade": "Madri"}

### Acesso 

### Para acessar os valores de um dicionário, utilize a chave correspondete entre colchestes

print(pessoa["nome"]) # Imprime Joao
print(pessoa["idade"]) #25
print(pessoa["cidade"]) # madri

### MÉTODOS
"""
keys(): retorna uma visualização de toddas as chaves do dicionário.
values(): retorna uma visualização de todos os valores do dicionário.
items(): retorna uma visualização de todos os pares chave-valor do dicionário.
update(outro_dicionario): atualiza o dicionário com pares chave-valor de outro dicionário

"""
print(pessoa.keys()) # imprime dic_keys(["nome", "idade, "cidade])
print(pessoa.values()) # imprime dict_values (["joao",25,"Madri"])
print(pessoa.items()) # imprime dict_items (["nome"joao","idade",25,"cidade","Madri"])
pessoa.update({"profissão": "Engenheiro"})
print(pessoa)## imprime ["nome"joao","idade",25,"cidade","Madri" ""profissão": "Engenheiro""])