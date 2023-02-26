from selenium import webdriver
import time
class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "Bom dia pessoal, veja o video que acabou de sair https://www.youtube.com"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["Grupo"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver =webdriver.Chrome('C:/Users/Deus.DEUS.002/Documents/chromedriver.exe')

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()

