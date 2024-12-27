# Calculadora Simples

while True:
    print("\nBem-vindo à calculadora!")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    # Receber a escolha do usuário
    escolha = input("Digite o número da operação desejada: ")

    if escolha == '5':
        print("Obrigado por usar a calculadora! Até mais.")
        break

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida. Tente novamente.")
        continue

    # Receber os números de entrada
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números.")
        continue

    # Realizar a operação escolhida
    if escolha == '1':
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} é {resultado}.")
    elif escolha == '2':
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} é {resultado}.")
    elif escolha == '3':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} é {resultado}.")
    elif escolha == '4':
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} é {resultado}.")


