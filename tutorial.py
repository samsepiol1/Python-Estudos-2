import schedule
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




def FazerTarefaImportante():
    print('Gerando')

def job():
    print('Estou rodando uma thread %s'%threading.current_thread())

def run_thread(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(10).seconds.do(run_thread,job)
schedule.every(10).seconds.do(run_thread,job)
schedule.every(10).seconds.do(run_thread,job)
schedule.every(10).seconds.do(run_thread,job)
schedule.every(10).seconds.do(run_thread,job)
while 1:
    schedule.run_pending()
    time.sleep(1)