import random
from balde import Balde
#Definição de constantes
cap_min=10
cap_max=51
vol_min=1
vol_max=11
class Simulador:
    def __init__(self,semente):
        random.seed(semente)
        capacidade=random.randrange(cap_min,cap_max)
        self.rec=Balde(capacidade)
        self.vol=0
        self.avisou=False
    def sorteia(self):
        self.vol=random.randrange(vol_min,vol_max)
        print("Volume Atual :",self.rec.vol)
        print("Volume sorteado : ",self.vol)
        return self.vol
    def depoista(self):
        self.rec.deposita(self.vol)
        if self.rec.vol>=self.rec.cap/2 and not self.avisou:
            self.avisou=True
            print("O Volume do Balde Atingiu/Passou a metade")
            return self.rec.cheio
    def finaliza(self):
        print("\nFim da Simulação")
        print("Capacidade do balde: %d"%self.rec.cap)
        print("Volume Final: %d"%self.rec.vol)
        if self.rec.der>0:
            print("Balde está cheio e houve derramento de água")
            print("Volume derramado foi %d"%self.rec.der)
        else:
            if self.rec.cheio:
                print("O Balde está cheio e não houve derramamento de água")
            elif self.rec.cap-self.rec.vol>=self.vol:
                print("Balde não está cheio")
                print("Havia espaço para o ultimo volume sorteado: %d"%self.valor)
            else:
                 print("O balde não")
                 print("Não Havia espaço para o ultimo volume sorteado %d"%self.valor)
if __name__ == "__main__":
    s=Simulador(123)
    v1=s.sorteia()
    r1=s.depoista()
    print(v1,r1)
    v2=s.sorteia()
    r2=s.depoista()
    print(v2,r2)
    s.finaliza()

