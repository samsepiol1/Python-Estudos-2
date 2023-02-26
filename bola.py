class Bola():
    def __init__(self):
        self.cor=''
        self.circun=3.14
        self.material='Poligono'
    def troca_cor(self,cor):
        mudar_cor=self.cor=cor
    def mostra_cor(self):
        return print(self.cor)
b=Bola()
b.troca_cor('Azul')
b.mostra_cor()