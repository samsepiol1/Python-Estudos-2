from threading import Thread, Lock
import time
import random

armazem = []
trava = Lock()

class ProdutorThread(Thread):
    def run(self):
        global armazem
    while True:
        trava.acquire()
        armazem.append(random.randrange(0, 9))
        print(f"Produzido {armazem[-1]}")
        print(f"Lista do produtor {armazem}\n")
        trava.release()
        time.sleep(random.random())

class consumidor(Thread):
    def run(self):
        global armazem
        while True:
            trava.acquire()
            if not armazem:
                print("Armazém Vazio, o consumidor tentará consumir")
                num = armazem.pop(0)
                print(f"Consumiu {num}")
                print(f"Lista do consumidor {armazem}\n")
                trava.release()
                time.sleep(random.random())
                if __name__ == '__main__':
                  ProdutorThread().start()
                  ConsumidorThread().start()
