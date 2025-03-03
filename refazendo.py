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
        if nome == '':
            raise ValueError("O nome do evento não foi definido")
        else:
            self.__nome = nome
    
    def set_data(self, data):
        if data == '':
            raise ValueError("A data não foi definido")
        else:
            self.__data = data
    
    def set_local(self, local):
        if local == '':
            raise ValueError("O local não foi definido")
        else:
            self.__local = local
    
    def __str__(self):
        return f'{self.__nome} - {self.__evento} - {self.__local}'
    
class NumDiasError(Exception):
    def __init__(self, dias):
        self.__dias = dias
    
    def get_dias(self):
        return self.__dias

class Congresso(Evento):
    def __init__(self, nome, data, local, numDias, inscricao):
        super().__init__(nome,data,local)
        self.__numDias = numDias
        self.set_numDias(numDias) # assim que definir e passar o numDias vai conferir, na hora
        self.__inscricao = inscricao
    
    #gets

    def get_numDias(self):
        return self.__numDias
    
    def get_inscricao(self):
        return self.__inscricao
    
    #sets

    def set_numDias(self, numDias):
        if numDias < 1 or numDias > 30:
            raise NumDiasError(numDias)
    
    def set_inscricao(self, valor):
        if valor == '':
            raise ValueError("O valor precisa ser diferente de vazio")
    
    def DataFinal(self):
        pass

    def Dias(self):
        pass

    def __str__(self):
        return f'Nome do evento: {self.get_nome()}, Data de inicio: {self.get_data()}, local: {self.get_local()}, Período de execução: {self.__numDias}, Valor: {self.__inscricao}'


class UI:
    @classmethod
    def Main(cls):
        nome = input("Digite o nome do evento: ")
        local = input("Digite o local do evento: ")
        data = datetime.strptime(input("Qual a data do evento: "),'%d/%m/%Y') #show papae
        dias = int(input("Período de execução: "))
        inscricao = int(input("Qual o valor da inscrição: "))
        try:
            c = Congresso(nome,data,local,dias,inscricao)
            print(c)
        except NumDiasError as error:
            print("Números de dias invalidos")
            print(f'Quantidade invalida: {error.get_dias()}')

UI.Main()

            
        
    


    

        