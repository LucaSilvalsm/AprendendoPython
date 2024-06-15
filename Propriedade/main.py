from datetime import datetime

class Pessoa:
    def __init__(self, nome, sobrenome, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento
        
    @property
    def fullName(self):
        return f"{self.nome} {self.sobrenome}"
    
    @property
    def idade(self):
        ano_atual = datetime.now().year
        return ano_atual - self.nascimento
    
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

lucas = Pessoa("Lucas", "Moreira", 1997)
print(f"Nome Completo: {lucas.fullName} \nIdade: vai fazer {lucas.idade}")
