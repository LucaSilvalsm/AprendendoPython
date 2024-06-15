class Animal:
    def __init__(self, numeroPatas, especie, **kwargs):
        self.numeroPatas = numeroPatas
        self.especie = especie
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
         return f"{self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"    


class Manifero(Animal):
    def __init__(self, corPelo, **kwargs):
        self.corPelo = corPelo
        super().__init__(**kwargs)


class Ave(Animal):
    def __init__(self, caracteristica, **kwargs):
        self.caracteristica = caracteristica
        super().__init__(**kwargs)


class Gato(Manifero):
    pass


class Ornitorrinco(Manifero, Ave):
    def __init__(self, numeroPatas, especie, corPelo, caracteristica):
        Manifero.__init__(self, corPelo=corPelo, numeroPatas=numeroPatas, especie=especie)
        Ave.__init__(self, caracteristica=caracteristica, numeroPatas=numeroPatas, especie=especie)


gato = Gato(4, "Gato", corPelo="Cinza")
print(gato)

ornitorrinco = Ornitorrinco(4, "Ornitorrinco", "Marrom", "Bico")
print(ornitorrinco)
