from Funcoes_matematicas import imc#importa a função imc o arquivo funcoes_matematicas


class Pessoa:#define a classe pessoa
    def __init__(self, nome, sobrenome, idade, peso, altura):#construtor que recebe parametros e passa os valores para os objetos
        self.nome = nome #define o valor do objeto nome como o parametro nome
        self.sobrenome = sobrenome #define o valor do objeto nome como o parametro nome
        self.idade = idade #define o valor do objeto idade como o parametro idade
        self.peso = peso #define o valor do objeto peso como o parametro peso
        self.altura = altura #define o valor do objeto altura como o parametro altura

    def printa_dados(self):#printa todos os objetos da classe
        for chave, valor in vars(self).items():#loopa para cada objeto na classe
             print(valor)
       
    def aniversario(self):#atualiza a idade da pessoa
        self.idade += 1 #adiciona um a idade

    def adicionar_peso(self, qtd: float):#atualiza o peso, o : float define que a variável é do tipo float
        self.peso += qtd #adiciona a variação no peso ao peso 
    
    def adicionar_altura(self, dif_altura):
        self.altura += dif_altura #adiciona dif_altura a altura

    def imc(self):
        print(str(imc(self.peso, self.altura)))#converte o valor retornado pela função imc em string e depois da print
    
    def retorna_dados_como_dicionario(self):#Retorna os dados da pessoa como dicionário
        return {'nome': self.nome, 'sobrenome': self.sobrenome, 'idade' : self.idade, 'peso': self.peso, 'altura' : self.altura}


gustavo = Pessoa('Gustavo', 'Marinho Tannenbaum', 25, 115.5, 1.73)
gustavo.imc()