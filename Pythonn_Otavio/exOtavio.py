# Faça um programa que peça ao usuário para digitar um número int informe se este número é par ou Impar.
#
# Caso o usuário não digite um Inteiro, informe que não é um número Inteiro.

def Int_e_Par_ou_Impar():

    a = float(input("Digite um número: "))

    # Verifica se o número é inteiro
    # if a. a.is_integer():
    if a % 1 == 0:
        # Verifica se o número é par
        if a % 2 == 0:
            print("O número é par.")
        else:
            print("O número é impar.")
    else:
        print("Não é um número inteiro.")


# Faça um programe que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex. Bom dia 6-11, Boa tarde 12-17 e Boa noite 16-23.

def CumprimentoHora():
    hora = int(input("Digite a hora: "))
    if hora >= 0 and hora <= 11:
        print("Bom dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
    else:
        print("Hora inválida")


# Faça a programa que peça o primeiro nave do usuário. Se o nome tiver 4 letras ou signos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome e muito grande

def Nome():
    nome = input("Digite seu nome: ")
    if len(nome) <= 4:
        print("Seu nome é curto")
    elif len(nome) <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")


def menu():
    print("""
    1 - Int_e_Par_ou_Impar
    2 - CumprimentoHora
    3 - Nome
    4 - Sair
    """)

    option = int(input("Digite a opção desejada: "))

    while option != 4:
        if option == 1:
            Int_e_Par_ou_Impar()
        elif option == 2:
            CumprimentoHora()
        elif option == 3:
            Nome()
        else:
            print("Opção inválida")

#


meuVetor = [15, 232, 32, 1323, 1]

# printar array
for i in range(0, len(meuVetor)):
    print(meuVetor[i])

maior = meuVetor[0]
menor = meuVetor[0]
for i in range(0, len(meuVetor)):
    if meuVetor[i] > maior:
        maior = meuVetor[i]
    if meuVetor[i] < menor:
        menor = meuVetor[i]
# se os 5 numeros forem iguais
if meuVetor[0] == meuVetor[1] == meuVetor[2] == meuVetor[3] == meuVetor[4]:
    print("Os 5 números são iguais")

    # interpoalção de string
print("O maior número é: %d" % maior)
print("O menor número é: %d" % menor)
