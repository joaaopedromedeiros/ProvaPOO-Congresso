from datetime import datetime as dt
from datetime import timedelta as td

class Evento:
    def __init__(self, nome, data, local):
        self.__nome = nome
        self.__data = dt.strptime(data, '%d/%m/%Y')
        self.__local = local
    
    #gets

    def get_nome(self):
        return self.__nome
    
    def get_data(self):
        return self.__data
    
    def get_local(self):
        return self.__local
    
    #sets

    def set_nome(self,nome):
        if nome == '' or ' ':
            raise ValueError()
        else:
            self.__nome = nome
    
    def set_data(self, data):
        if data == '' or ' ':
            raise ValueError()
        else:
            self.__data = data
    
    def set_local(self, local):
        if local == '' or ' ':
            raise ValueError()
        else:
            self.__local = local
    
    def __str__(self):
        return f'Nome do evento: {self.__nome}, Data: {self.__data}, Local: {self.__local}'


class Congresso(Evento):
    def __init__(self, nome, data, local, numDias, inscricao): # add todos, dps add super().__init__(...)
        super().__init__(nome, data, local)
        if numDias < 1 or numDias > 30:
            raise NumDiasError(numDias)
        else:
            self.__numDias = int(numDias)
        self.__inscricao = float(inscricao) #double 

    
    #gets

    def get_numDias(self):
        return self.__numDias
    
    def get_inscricao(self):
        return self.__inscricao
    
    #sets
    def set_numDias(self, numDias):
        if numDias < 1 or numDias > 30:
            raise NumDiasError(numDias)
        else:
            self.__numDias = numDias
    
    def set_inscricao(self, valor):
        if valor == '' or ' ':
            raise ValueError()
        else:
            self.__inscricao = valor
    
    def dataFinal(self):
        inicio = self.get_data()
        diasTotais = self.get_numDias()
        datafinal = inicio + td(days=diasTotais - 1)
        print(datafinal)
        return datafinal
    
    def dias(self):
        dias_evento = []
        inicio = self.get_data()
        for i in range(self.get_numDias()):
            dias_evento.append(inicio + td(days=i))  # Adiciona cada dia ao evento
        for i in dias_evento:
            print(i.strftime('%d/%m/%Y'))
        return dias_evento

    
    def __str__(self):
        return f'Nome: {self.get_nome()}, data: {self.get_data()}, Local: {self.get_local()}, Dias de evento: {self.__numDias}, inscrição: {self.__inscricao}'
    

class NumDiasError(Exception):
    def __init__(self, numDias):
        self.__numDias = numDias
        self.__message = f'Quantidade invalida de dias: {self.__numDias}'
      
    
    def get_numDiaError(self):
        return self.__numDias
    
    def get_message(self):
        return self.__message
    
    def __str__(self):
        return self.__message

class ValueError(Exception):
    def __init__(self, nomeErrado, localErrado):
        self.nome = nome
        self.local = local
        

    
    




#testeError = 0
#teste = Congresso("teste", "05/03/2025","aaa",testeError,"60")
#teste.set_numDias(1)
#teste.dataFinal()
#print(teste)

class UI:
    @classmethod
    def MainUI(cls):
        try:
            nome = input("Digite o nome do evento: ")
            data = input("Digite a data de acontecimento (mm/dd/yyyy): ")
            local = input("Digite o local do evento: ")
            dias = int(input("Dias totais: "))
            valor = input("Valor de inscrição: ")
            novo = Congresso(nome, data, local, dias, valor)
            novo.dias()
        except NumDiasError:
            print(f'O número precisa está entre 1 e 30 dias, valor digitado: {dias}')

UI.MainUI()




