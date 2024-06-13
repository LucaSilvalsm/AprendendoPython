# Para iniciar uma classe em python precisamos do def __init__(seft)
# self é uma referencia ao objeto  a instancia do objeto


class Carros:
    def __init__(self, cor, marca, modelo, ano):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f"Cor: {self.cor}, Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

    # def __str__(self):
    #    return f"{self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave,valor in self.# __dict__.items()])}"
    
    def velocidade(seft): #metodos do objeto
        print("Velocidade de 120 km/h ")
    def consumo(seft): #metodos do objeto
        print("Faz 6 km/litro")
Fusion = Carros("Preto", "Ford", "Fusion", 2022)

print(Fusion)
Fusion.consumo() #acessando os methodos
Fusion.velocidade() #acessando os methodos