from threading import Thread, Lock, Condition
import time
import random

armazem = []
trava = Lock()
dorme_produtor = Condition()
dorme_consumidor = Condition()
TAM_ARM = 10

class ProdutorThread(Thread):
    def __init__(self, threadID):
        Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global armazem
        while True:
            trava.acquire()
            dorme_produtor.acquire()
            dorme_consumidor.acquire()
            if len(armazem) < TAM_ARM:
                armazem.append(random.randrange(0, 9))
                print(f"Produtor {self.threadID} produziu {armazem[-1]}")
                print(f"Lista do produtor {armazem}\n")


                dorme_consumidor.release()
                dorme_produtor.release()
            else:
                print(f"Armazém cheio, Produtor {self.threadID} vai dormir")
                if trava.locked():
                    trava.release()
                dorme_consumidor.notify()
                dorme_consumidor.release()
                dorme_produtor.wait()
            if trava.locked():
                trava.release()
            time.sleep(random.random())

class ConsumidorThread(Thread):
    def __init__(self, threadID):
        Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global armazem
        while True:
            trava.acquire()
            dorme_produtor.acquire()
            dorme_consumidor.acquire()
            if len(armazem) > 0:
                num = armazem.pop(0)
                print(f"Consumidor {self.threadID} consumiu {num}")
                print(f"Lista do consumidor {armazem}\n")

                dorme_consumidor.release()
                dorme_produtor.release()
            else:
                print(f"Armazém vazio. Consumidor {self.threadID} irá dormir")
            if trava.locked():
                trava.release()
                dorme_produtor.notify()
                dorme_produtor.release()
                dorme_consumidor.wait()
            if trava.locked():
                trava.release()
            time.sleep(random.random())
if __name__ == '___main___':
    numprod = 2
    numcons = 2

    for i in range(numprod):
        t = ProdutorThread(i)
        t.start()

    for i in range(numcons):
        t = ConsumidorThread(i)
        t.start()
