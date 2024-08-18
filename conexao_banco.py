import mysql.connector
from Pessoa import Pessoa

# Configurações da conexão
config = {
    'user': 'root',    # Usuário
    'host': 'localhost',  # Host
    'port': '3306',        # Porta
    'database': 'dados',  # Nome do banco
}

#Conecta ao banco de dados

conexao = mysql.connector.connect(**config)#O ** é usado para passar um dicionário como argumentos de palavra chave
if conexao.is_connected():
        print('Conectado ao servidor MySQL')#mensagem caso a conexão funcione


def apaga_todos():
     cursor = conexao.cursor()#cria um objeto que permite executar comandos sql
     
     query = 'DELETE FROM pessoas'#cria string com a query

     cursor.execute(query)


def inserir_pessoa(valores):#função para inserir dados no banco
    cursor = conexao.cursor()#cria um objeto que permite executar comandos sql
    
    # cria uma string com a query
    query = "INSERT INTO pessoas (nome, sobrenome, peso, altura, idade) VALUES (" +  "'" + valores['nome'] + "', '" + valores['sobrenome'] + "', " +   str(valores['peso']) + ", " + str(valores['altura']) + ", " +   str(valores['idade']) + ")"

    
    cursor.execute(query)# Insere dados no banco

    # Commit para efetivar a operação no banco de dados
    conexao.commit()
    
    cursor.close()

def buscar_todos():#busca no mysql todos os dados da tabela e printa
    
    cursor = conexao.cursor()#cria um objeto que permite executar comandos sql
    
    query = "SELECT * FROM pessoas" # cria string com a query
    
    cursor.execute(query) # Executa a busca no banco
    
    resultados = cursor.fetchall()# Armazenando os resultados na variável resultados
    
    for resultado in resultados:#loopa montrando todos os resultados
        print(resultado)#printa os resultados
        
#cria dicionários com os dados das pessoas
dicionario_pedro = {'nome': 'Pedro', 'sobrenome': 'silva', 'peso': 60.2, 'altura':1.65,'idade': 30}
dicionario_joao = {'nome': 'João', 'sobrenome': 'andrade', 'peso': 73.4, 'altura':1.70,'idade': 42}
dicionario_andre = {'nome': 'André', 'sobrenome': 'costa', 'peso': 85.2, 'altura':1.66,'idade': 19}

#inserir_pessoa(dicionario_pedro)
#inserir_pessoa(dicionario_joao)
#inserir_pessoa(dicionario_andre)

joao = Pessoa('João', 'da Silva', 31,90,1.72)
carlos = Pessoa('Carlos', 'dos Santos', 45, 82.4,  1.59)

joao_dicionario = joao.retorna_dados_como_dicionario()
carlos_dicionario = carlos.retorna_dados_como_dicionario()

#inserir_pessoa(joao_dicionario)
#inserir_pessoa(carlos_dicionario)

apaga_todos()

buscar_todos()

def inseri_numero(num):
    cursor = conexao.cursor()  # Cria um objeto que permite executar comandos SQL
    
    # Cria uma string com a query
    query = "INSERT INTO numeros (numero) VALUES ('" + num + "');"
    
    cursor.execute(query)  # Insere dados no banco

# Exemplo de chamada da função
#inseri_numero('3.2')
