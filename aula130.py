import threading
from time import sleep

def wait():
    sleep(2)
    print('Acabou')

class myThread(threading.Thread):
    
