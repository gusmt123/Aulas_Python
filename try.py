try:
    print('Digite a operação:\n')
    print('1. Soma\n')
    print('2. Subtração\n')
    print('3. Multiplicação\n')
    print('4. Divisão')
    operacao = int(input(''))
    num1 = float(input('Digite o primeiro número\n'))
    num2 = float(input('Digite o segundo número:\n'))
    resultado = 0
    match operacao:
        case 1:
            resultado = num1 + num2
        case 2:
            resultado = num1 - num2
        case 3:
            resultado = num1 * num2
        case 4: 
            resultado = num1 / num2
    print(f"O resultado é: {resultado}")
except:
    print('erro ao processar')
finally:
    pass
