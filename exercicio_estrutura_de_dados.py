# import time

# altura = float(input("Digite a sua altura: "))
# peso = float(input("digite o seu peso: "))

# imc = peso / altura ** 2

# print("Calculando...")
# time.sleep(3)                      pra usar biblioteca importada time, 3 segundos pra responder
# print(f"Seu imc é {imc:.2f}")   :2f pra pegar decimal dessa forma format

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# nome = input("Boa noite, qual o seu nome? ")
# primeiro_nome = nome.split()[0]         divide o nome em lista pelos espaços e pega o index 0 com o colchete
# print(f"Ola {primeiro_nome}.")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------


# email = input("digite aqui seu email: ")
# dominio = email.split("@")[-1]                sepaga o email com o split no @ e com o colchete em -1 pega a ultima parte
# print(dominio)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# area = float(input("Informa a area quadrada que deseja pintar: "))

# volume_necessario = area / 3
# quantidade_latas = int(volume_necessario / 18)
# custo = quantidade_latas * 80

# print(f"Voce precisara de {quantidade_latas} latas e vai gastar {custo} reais.")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# valor_hora = float(input("Informe quanto ganha por hora: "))
# horas_trabalhadas = float(input("Informe horas trabalhadas por mes: "))

# salario = horas_trabalhadas * valor_hora
# ir = salario * 0.11
# inss = (salario - ir) * 0.08
# sindicato = (salario - ir - inss) * 0.05
# print(f"Salario Bruto: {salario}")
# print(f"taxa ir: {ir}")
# print(f"taxa inss: {inss}")
# print(f"taxa sindicato: {sindicato}")
# print(f"salario liquido: {salario - ir - inss - sindicato:.2f}")
