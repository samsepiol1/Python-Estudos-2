from selenium import webdriver
driver = webdriver.Chrome('C:/Users/Deus.DEUS.002/Documents/chromedriver.exe')
driver.implicitly_wait(30)
base_url = "https://m.facebook.com/friends/center/requests/outgoing/"
driver.get(base_url)
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys('steve.jkl5@gmail.com')
driver.find_element_by_id("m_login_password").send_keys('imac88246948')
login=driver.find_element_by_name('login')
login.click()

while True:
    cancelReq = driver.find_element_by_link_text("Cancelar")
    cancelReq.click()

