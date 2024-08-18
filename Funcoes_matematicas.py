def juros_compostos(montante, juros, num_periodos):
    return montante*pow(1+juros, num_periodos)#retorna o valor futuro, pow é função utilizada pra calcular potência

def par_ou_impar(num):
    if num % 2 == 0:#verifica se o quociente de num é zero
        print("O número é par")
    else:#executa po código a seguir se a condição anterior for falsa
        print("O úmero é impar")

def imc(peso, altura):
    return peso / pow(altura, 2)#retorna o imc, pow é função utilizada pra calcular potência
