import Pessoa #importa o arquivo pessoa
class Aluno(Pessoa.Pessoa):#cria a classe Aluno que herda a classe Pessoa
    def __init__(self,nome, sobrenome, idade, peso, altura, notas, frequencia):#construtor da classe passa os valores 
        super().__init__(nome, sobrenome, idade, peso, altura)#chama construtor da classe pai
        self.notas = notas #define o valor do objeto notas como o parametro notas
        self.frequencia = frequencia #define o valor do objeto frequencia como o parametro frequencia

    def media_nota(self):#calcula média aritimética
        somatorias_notas = 0#cria variável somatoria_notas e iguala ela a zero
        for nota in self.notas:#loopa para cada nota
            somatorias_notas += nota#faz a somatoria das notas
        media_notas = somatorias_notas / len(self.notas)#divive a somastória das notas pelo número de notas, função len() retorna comprimento de algo lista, tuple, etc...
        return media_notas#retorna o resultado

    def adiciona_frequencia(self):#adiciona um a frequencia
        self.frequencia += 1#adiciona um a frequencia 