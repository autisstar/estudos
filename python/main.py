# lista
salarios = []

#  repetir
for x in range(2):
    nome = input("Nome:")
    salario = input("Salario:")
    result = [nome, salario]
    salarios.append(result)

# resultados
for n in salarios:
    nome = n[0]
    salario = n[1]
    print("",nome,"tem o salario de ",salario)
