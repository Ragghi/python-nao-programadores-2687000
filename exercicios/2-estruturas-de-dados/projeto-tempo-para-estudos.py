# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input("Qual é seu nome: ")
print(f"Olá, {nome}!")

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = int(input("Total de dias por semana, dedicados ao estudo: "))

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = int(input("Média de horas estudada por dia: ")) #posso manter a entrada como string e converter antes de apresentar o resultado na tela (passo 5).


# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input("Curso: ")

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f"{nome}, você arrasou com {total_dias} dias e {total_dias * total_horas} horas de estudo para o curso de {curso}!!!")
