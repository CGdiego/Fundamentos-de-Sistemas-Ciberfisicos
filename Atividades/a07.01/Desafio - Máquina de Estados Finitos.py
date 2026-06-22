estado = "inicio"

while estado != "fim":
    if estado == "inicio":
        valor1 = 0
        valor2 = 0
        resultado = 0
        solicitacao = 0

        print("Estou pronto.")
        estado = "esperando_entrada"

    elif estado == "esperando_entrada":
        valor1 = input("Insira o 1º valor: ")
        while not valor1.isdigit():
            print("Input inválido, insira novamente.")
            valor1 = input("Insira o 1º valor: ")
        valor1 = int(valor1)

        valor2 = input("Insira o 2º valor: ")
        while not valor2.isdigit():
            print("Input inválido, insira novamente.")
            valor2 = input("Insira o 2º valor: ")
        valor2 = int(valor2)

        estado = "calculando"

    elif estado == "calculando":
        print(f"O 1º valor é {valor1}.")
        print(f"O 2º valor é {valor2}.")
        print(f"O resultado é a soma de {valor1} com {valor2}.")
        resultado = valor1 + valor2
        estado = "imprimindo_resultado"

    elif estado == "imprimindo_resultado":
        print(f"O resultado é {resultado}.")
        estado = "aguardando_solicitacao"

    elif estado == "aguardando_solicitacao":
        solicitacao = input("Digite o número correspondente à sua escolha:\n[1] - Realizar um nova operação.\n[2] - Encerrar o programa.\n")
        while not solicitacao.isdigit() or (int(solicitacao) != 1 and int(solicitacao) != 2):
            print("Input inválido, insira novamente.")
            solicitacao = input("Digite o número correspondente à sua escolha:\n[1] - Realizar um nova operação.\n[2] - Encerrar o programa.\n")
        solicitacao = int(solicitacao)

        if solicitacao == 1:
            estado = "esperando_entrada"
        else:
            estado = "fim"

if estado == "fim":
    print("Programa encerrado.")