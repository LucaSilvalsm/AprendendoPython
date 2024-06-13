#Essa Aula é o conceito basico do Python concatenar no python é "+"
nome = input("Informe o seu nome: ")
print("Seu nome é " + nome)
idade = input("Digite a sua idade: ")
print("Sua idade é " + idade)
print("Seu nome é " + nome + " e sua idade é " + idade + " anos")


nome = "Guilherme"
sobrenome = "Silva"

print(nome,sobrenome)
print(nome,sobrenome, end="...\n") # aqui ele vai adicionar 3 pontos no final 
print(nome,sobrenome, sep="#") # aqui ele adiciona um "#" no meio da palavra ele é um separador
print(nome,sobrenome, end="..........")