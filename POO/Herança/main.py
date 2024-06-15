#Herança Simples
# Eu consigo criar metodos unicos na classe filha sem alterar a classe pai 
# E consigo tbm criar atributos unicos na classe filha sem alterar a classe pai


class Veiculo: #classe pai 
    def __init__(self,cor,placa,marca,modelo):
        self.cor = cor 
        self.placa = placa 
        self.marca = marca
        self.modelo = modelo 
    def ligarMoto(self):
        print("Ligando Motor")
    def __str__(self):
         return f"{self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave,valor in self. __dict__.items()])}"
    
class Motocicleta(Veiculo):#classe filha
    def __init__(self, cor, placa, marca, modelo, cilindradas):
        super().__init__(cor, placa, marca, modelo) # chamando o construdor da classe pai,para assim herdar os atributos 
        self.cilindradas = cilindradas
class Carro(Veiculo):
    pass
class Caminhao(Veiculo):
    def carregar(self):
        print("Carregando para Viagem")


moto = Motocicleta("Vermelha","75H3U","HONDA","Fazer","150")
print(moto)
moto.ligarMoto()

fussion = Carro("Preto Fosco","BR346A1","FORD","Fusion")
scanner = Caminhao("Branco","BR316AE","WOSK","Scanner")
scanner.ligarMoto()
scanner.carregar()