class Estudante:
    escola = "UVA"
    def __init__(self,nome,matricua):
        self.nome = nome
        self.matricula = matricua
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
aluno1 =  Estudante("Lucas",2)
aluno2 = Estudante("Pedro",3)

print(aluno1)
print(aluno2)