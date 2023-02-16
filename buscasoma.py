import openpyxl

def encontra_soma(n, arr):
    if n == 0:
        return []
    if not arr:
        return None
    if arr[0] > n:
        return encontra_soma(n, arr[1:])
    
    incluir = encontra_soma(n - arr[0], arr[1:])
    if incluir is not None:
        return [arr[0]] + incluir
    else:
        return encontra_soma(n, arr[1:])

# Abre o arquivo do Excel
workbook = openpyxl.load_workbook('planilha.xlsx')

# Seleciona a planilha e a coluna que deseja ler
worksheet = workbook['Planilha1']
column = worksheet['A']

# Armazena todos os valores da coluna em um Array
valores = []
print("Valores da coluna A:")
for cell in column:
    valores.append(cell.value)
print(valores)

# Lê um número N
n = int(input("Digite um número N: "))

# Chama a função encontra_soma para determinar quais valores somados do Array resultam no número N
resultado = encontra_soma(n, valores)

# Imprime o resultado
if resultado is None:
    print("Não foi possível encontrar uma soma que resulte em", n)
else:
    print("A soma de", " + ".join(str(x) for x in resultado), "é igual a", n)
