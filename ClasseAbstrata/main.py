## Em python nao tem o metodo interface, entao precisamos importa ele com ABC
##
##
from abc import ABC,abstractmethod


class UsuarioInterface(ABC):
    @abstractmethod
    def conhecerUsuario(self,nome,sobrenome,telefone):
        pass
    @abstractmethod
    def ola(self):
        pass    
    @property
    def fullName(self):
        return f"{self.nome} {self.sobrenome}"





class Usuario(UsuarioInterface):
    def conhecerUsuario(self,nome,sobrenome,telefone):        
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
    def ola(self):
        return print("Ola Mundo ")
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    

lucas = Usuario()
lucas.conhecerUsuario("Lucas","Moreira","21 99343-2153")
print(lucas)
print(lucas.fullName)
lucas.ola()