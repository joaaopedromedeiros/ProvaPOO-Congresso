from datetime import datetime, timedelta

class Evento:
    def __init__(self, nome, data, local):
        self.__nome = nome
        self.__data = data
        self.__local = local
    
    def get_nome(self):
        return self.__nome
    
    def get_data(self):
        return self.__data
    
    def get_local(self):
        return self.__local
    
    #sets
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_data(self, data):
        self.__data = data
    
    def set_local(self, local):
        self.__local = local
    
    def __str__(self):
        return f'{self.__nome} - {self.__data} - {self.__local}'


class Congresso(Evento):
    def __init__(self, nome, data, local, numDias, inscricao): #esqueci
        super().__init__(nome, data, local) # esqueci
        self.__numDias = numDias
        if self.__numDias < 1 or self.__numDias > 30:
            raise NumDiasError(self.__numDias)
        self.__inscricao = inscricao
    
    def set_numDias(self, numDias):
        self.__numDias = numDias
    
    def set_inscricao(self, inscricao):
        self.__inscricao = inscricao
    
    def get_numDias(self):
        return self.__numDias
    
    def get_inscricao(self):
        return self.__inscricao
    
    def DataFinal(self):
        dias_totais = self.get_numDias()
        data_str = self.get_data()
        data_datetime = datetime.strptime(data_str, "%d/%m/%Y")
        adicionando_dias = data_datetime + timedelta(days=dias_totais - 1) 
        print("Ultimo dia de evento")
        print(adicionando_dias.strftime("%d/%m/%Y"))
    
    def Dias(self):
        dias_totais = self.get_numDias()
        data_str = self.get_data()
        data_datetime = datetime.strptime(data_str, "%d/%m/%Y")
        dias = []
        for i in range(dias_totais): #[0,1]
            dias.append(data_datetime + timedelta(days=i))
        print("Lista de dias do evento:")
        for i in dias:
            print(i.strftime("%d/%m/%Y")) # ele já é datetime, não precisa de >>datetime<<.strftime("formato")
        

    
    def __str__(self):
        return f' Nome: {self.get_nome()} - Data: {self.get_data()} - Local: {self.get_local()} - Dias de evento: {self.__numDias} - Valor da inscrição: {self.get_inscricao()}'



class NumDiasError(Exception):
    def __init__(self, dias):
        self.__dias = dias
    
    def get_dias(self):
        return self.__dias
    
    def __str__(self):
        return f'O valor {self.__dias} é menor que 1 dia ou maior que 30 dias'


class UI:
    @classmethod
    def Main(cls):
        nome = input("Nome do evento: ")
        data = input("Data de ínicio do evento no formato (dd/mm/yyyy): ")
        local = input("Local do evento: ")
        dias = int(input("Dias total de evento: "))
        inscricao = int(input("Valor da inscrição para o evento: "))
        try:
            evento = Congresso(nome, data, local, dias, inscricao)
            print("-----------------------------------------------------------")
            print("Criando evento...")
            print("Evento criado com sucesso! Dados abaixo:")
            evento.DataFinal()
            evento.Dias()
        except NumDiasError as e:
            print(f'Erro ao criar o evento: {e}')

UI.Main()



#datafinal, dias
#codir = Congresso("CODIR","09/03/2025","REITORIA IFRN",2, 0)

#codir.DataFinal()
#codir.Dias()




