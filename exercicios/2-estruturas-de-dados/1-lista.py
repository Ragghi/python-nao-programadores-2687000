# Crie uma lista apenas com elementos numéricos
lista_numerica = [2, 4, 6, 8, 10, 12]
print(lista_numerica)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista = [1, 3, "Gustavo", 8, {8 > 4}, {3 < 9 and 9 < 11}, {8 + 4}]
print(lista)

# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista[0:-1:2])

# Remova da lista o último item
print(lista.pop())
print(lista)

# Insira na lista um novo item
lista.append("novo item")
print(lista)

# Remova da lista um item específico
lista.remove('novo item')
print(lista)

#Trazer o valor da lista
print(lista[2])

#Adiciona uma lista dentro de outra lista
lista.extend(lista_numerica)
print(lista)

