class Pessoa:
    def __init__(self,nome):
        self.nome=nome
    def __str__(self):
        return self.nome
regis=Pessoa('Regis')
print(regis)
fabio=Pessoa('Fabio')
print(fabio)
