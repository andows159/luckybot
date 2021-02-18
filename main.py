from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

#mainclass
class XavierBot:
    def __init__(self,username,password,accounts,url,time):
        print(accounts[1])
        self.time = time
        self.username = username
        self.password = password
        self.console_display()
        self.isvisible()
        self.login()


    def console_display(self):
#BUUG na escolha do modo, o modo oculto não está funcionando
        print('(Press "1" and "Enter" for YES\n or "2" and "Enter" for NOT) ' )
        visible_answer = input("Run program on visible mode ? (Show the browser when do actions)")
        if visible_answer == "1":
            self.visible = True
            print("Running on visible mode...")
            sleep(1)
        elif visible_answer == "2":
            self.visible = False
            print("Running on hidden mode...")

    #the browser is visible ?
    def isvisible(self):
        visible = self.visible
        if visible:
            self.driver = webdriver.Chrome()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            self.driver = webdriver.Chrome(chrome_options=options)

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        sleep(10 * self.time)
        login_box = driver.find_element_by_xpath('//input[@name="username"]')
        password_box = driver.find_element_by_xpath('//input[@name="password"]')
        login_box.click()
        login_box.clear()
        login_box.send_keys(self.username)
        password_box.click()
        password_box.clear
        password_box.send_keys(self.password)
        log_button = driver.find_element_by_xpath('//button[@type="submit"]')
        log_button.click()







instance = XavierBot("vlogueirosinsanosoficial@gmail.com","riacho2020",["@diegocunha9","@_laerton2","@tavares_r_"],'https://www.instagram.com/p/CF-R42TAlsW/',1)