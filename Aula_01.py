from Pessoa import Pessoa #importa a classe Pessoa
from Aluno import Aluno
from Funcoes_matematicas import juros_compostos #importa a função juros compostos
from Funcoes_matematicas import par_ou_impar

nome = 'Gustavo' #variável do tipo str que armazena o nome
sobrenome = 'Marinho Tannenbaum'#variável do tipo str que armazena o sobrenome
altura = 1.73 #variável do tipo float que armazena altura
peso = 114.5 #variável do tipo float que armazena o peso
idade = 25 #variável do tipo int que armazena a idade
variavel_booleana = False #é necessário colocar o F em maiusculo e o resto em minusculo, vale o mesmo para True



dicionario_dados = {'nome': 'Gustavo', 'sobrenome': 'Marinho Tannenbaum', 'altura': 1.73, 'peso' : 114.5, 'idade':25} #dicionario com os dados acima
#o dicionário acima armazena pares com uma chave e um valor

lista_idades = [28,25,13,27] #lista com dados do tipo int  que armazenam diversas idade, no python as listas são equivalentes aos arrays

tuple_idades = (31,74,17,52) #similar a lista, porém imutável

"""

Esse código faz o seguinte
1. importa a classe Pessoa
2. cria uma série de variáveis
3. cria um dicionário, uma lista e um tuple


"""

#print(juros_compostos( 1000.0 , 0.1075, 1))
#par_ou_impar(3)

def chama_a_classe_aluno():
    gustavo = Aluno(nome,sobrenome,idade,peso,altura,[8.5,5,7,5.5], 1)
    media = gustavo.media_nota()
    print(str(media))
    gustavo.adiciona_frequencia()
    frequencia = gustavo.frequencia
    print(str(frequencia))
    gustavo.printa_dados()

def chama_a_classe_pessoa():
    gustavo = Pessoa(nome,sobrenome,idade,peso,altura)#cria uma nova instância da classe Pessoa
    #gustavo.printa_dados()#chama função que printa os objetos da classe
    #gustavo.aniversario()#chama a função que atualiza a idade
    dif_peso = float(3.2)#cria a variável dif_peso e dá a ela o valor de 3.2
    #gustavo.adicionar_peso(dif_peso)#chama a função que atualiza peso e passa dif_peso para ela
    #gustavo.adicionar_altura(0.1)#chama a função que adiciona altura e passa 0.1 como paramêtro
    gustavo.printa_dados()#chama função que printa os objetos da classe
    gustavo.imc()

def printa_dados():#def é o comando para criar funções no python
    for x in dicionario_dados:#repete o ciclo para cada item no dicionário
        print(x) #mostra as chaves do dicionario_dados
        print(dicionario_dados[x]) #mostra os dados do dicionario_dados

    for x in lista_idades:#repete o ciclo para cada item na lista
        print(x)#mostra todos os dados da lista_idades

    for x in tuple_idades:
        print(x)#mostra todos os dados do tuple_idades


def verifica_maior_de_idade(lista_idades):#essa função recebe um parametro que é o array com as idades
    for y in lista_idades:#repete o ciclo para cada item na lista
        if y > 18:#condicional, se for maior de 18 executa aquilo que está espaçado com um tab a frente
            print(str(y) + " é maior de 18")
        else:#comando else para ser executado caso a condição acima não seja comprida
            print(str(y)+ " é menor e 18")


"""
O código acima inclui trê funções:

1.Função que cria uma instância de outra classe e começa a executar funções
2.Função que printa os dados de cima
3.Função que veirifca se a pessoa é maior de idade

"""

i = 0
while i < 5:
    print(i)
    i+=1

#executa a função verifica_maior_de_idade
#verifica_maior_de_idade(lista_idades) 
            

#chama_a_classe_pessoa()

#chama_a_classe_aluno()