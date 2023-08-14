import os

while True:
    print("0 - Soma")
    print("1 - Subtracao")
    print("2 - Multiplicacao")
    print("3 - Divisao")
    print("4 - Exponenciacao")
    operacao = input("Qual operacao voce deseja fazer? ")
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    if operacao == "0":
        print(f"A soma de {n1} e {n2} = {n1 + n2}")
    elif operacao == "1":
        print(f"A subracao de {n1} por {n2} = {n1 - n2}")
    elif operacao == "2":
        print(f"A multiplicacao de {n1} por {n2} = {n1 * n2}")
    elif operacao == "3":
        print(f"A divisao de {n1} por {n2} = {n1 / n2}")
    elif operacao == "4":
        print(f"A potencia de {n1} elevado a {n2} = {n1 ** n2}")
    else:
        print("Operacao nao encontrada.")
    questao = input("Deseja continuar usando a calculadora? 0 para SIM, 1 para NAO: ")
    if questao == "0":
        os.system("clear")
        continue
    else:
        break
    
# -----------------------------------------------------------------------------------------------------------------