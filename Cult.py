from selenium import webdriver
class Cult12:
    def __init__(self,driver):
        self.driver=driver
        self.url="http://cultcampinas.com.br"
        self.box='eventBox' #class
        self.title_box='titleEventBox' #clas
        self.date='dateEvent' #class
        self.place='placeEvent' #class
        self.hour='hourEvent' #class
        self.desc='descEventBox' #class
        self.type='typeEventBox' #class



    def navigate(self):
        self.driver.get(self.url)
    def __get__boxes(self):
        return self.driver.find_elements_by_class_name(self.box)
    def get_all_data(self):
        boxes=self.__get__boxes()
        for box in boxes:
            print(box)
gg=webdriver.Chrome('C:/Users/Deus/Downloads/chromedriver.exe')
c=Cult12(gg)
c.navigate()
c.get_all_data()