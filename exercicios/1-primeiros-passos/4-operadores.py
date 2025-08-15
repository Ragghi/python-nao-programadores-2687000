ano_nascimento = 1989
ano_formatura = 2010
ano_atual = 2025

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
print(f'Gerlaine tinha {ano_formatura - ano_nascimento} anos na sua formatura')

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_nascimento >= ano_formatura)
print(ano_nascimento <= ano_formatura)
print(ano_nascimento == ano_formatura)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print((ano_formatura > ano_nascimento) and (ano_formatura < ano_atual)) #True
print((ano_formatura < ano_nascimento) and (ano_formatura < ano_atual)) #False
print((ano_formatura > ano_nascimento) or (ano_formatura > ano_atual))  #True
print(not(ano_formatura > ano_nascimento) and (ano_formatura < ano_atual)) #False