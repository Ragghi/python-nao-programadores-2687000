resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"
resumo="Gustavo é um homem de 38 anos que deseja mudar de profissão, por isso está estudando 'Python'."

print(resumo)

# Imprima na tela apenas a segunda letra da variável
print(resumo[1])

# Imprima na tela a idade de Paloma (resposta esperada: "46")
print(resumo[22:24])

# Imprima na tela o trecho final da variável
print(resumo[30:])

# Converta todos as letras para minúsculo e imprima na tela
print(resumo.lower())

# Converta todas as letras para maiúscula e imprima na tela
print(resumo.upper())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela
print(resumo.title())

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
print(resumo.capitalize())

# Imprima na tela uma string utilizando uma variável, usando o recurso string format
idade=38
print(f"Gustavo é um homem de {idade} anos que deseja mudar de profissão, por isso está estudando 'Python'.")
