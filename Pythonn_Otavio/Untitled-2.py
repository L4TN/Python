
'''Escreva um programa onde o usuário digite um valor inteiro e o programa escreva a
música do “Elefante incomoda” correspondente ao valor digitado:
Exemplo: Usuário digitou o nº 3
Saída: Incomoda Incomoda Incomoda muito mais'''

# elefante incomoda incomoda muito mais

a = int(input("Digite um número: "))
texto = ""

for i in range(a):
    texto += "Incomoda "


print(texto + "muito mais")
