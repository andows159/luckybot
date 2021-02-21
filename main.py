from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
from PyQt5 import uic, QtWidgets
import platform

#mainclass
class BackEnd:

    def start(self,username,password,kit,post,time):
        #move back to constructor when learn about method super
        self.time = time
        self.post = post
        self.kit = kit
        self.username = username
        self.password = password
        self.isvisible()
        self.login()
        try:
            self.comment_on_post(self.kit)
        except:
            self.comment_on_post(self.kit)

   
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
        self.time = int(input('how is your internet today? (press "1" for normal, "2,3,4" if is slow'))

    #the browser is visible ?
    def isvisible(self):
        
        if platform.system() == "Windows":
            
            
            visible = True
            #visible = self.visible
            if visible:
                
                #options = webdriver.ChromeOptions()
                #options.add_argument("--start-maximized")
                #options.add_argument("--headless")
                self.driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe',)
                
            else:
                options = webdriver.ChromeOptions()
                options.add_argument("--headless")
                self.driver = webdriver.Chrome(chrome_options=options)
        elif platform.system() == "Linux":
                 
            visible = True
            #visible = self.visible
            if visible:
                
                #options = webdriver.ChromeOptions()
                #options.add_argument("--start-maximized")
                #options.add_argument("--headless")
                self.driver = webdriver.Chrome()
                
            else:
                options = webdriver.ChromeOptions()
                options.add_argument("--headless")
                self.driver = webdriver.Chrome(chrome_options=options)







    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        sleep(4 * self.time)
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
    def browse_to_post(self,post,verification):
        sleep(3 * self.time)
        driver = self.driver
        driver.get(post)
        sleep(2 * self.time )
        try:
            driver.find_element_by_xpath(verification)
        except:
            print("elementos não econtrados, recarregando...")
            driver.get(post)
    def comment_on_post(self, kit):
        self.browse_to_post(self.post,'//button[@type="submit"]')
        self.kit = kit
        sleep(3 * self.time)
        driver = self.driver
        sleep(3 * self.time)

        comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh"]')
        comment_box.click()
        comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh focus-visible"]')
        #comment_box.send_keys(kit)
        while True:
            
            for account in kit:
                
                
                for letter in account:
                    comment_box.send_keys(letter)
                    sleep((randint(3,30) /30)) 

                button = driver.find_element_by_xpath('//button[@type="submit"]')
                button.click()
                print(f"account {account} commented on post {self.post}")
               
                sleep((randint(45,60)) * self.time)
                comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh"]')
                try:
                    comment_box.click()
                    
                    
                except:
                    print("Elemento bloqueado")
                comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh focus-visible"]')
                
                
            



class FrontEnd(BackEnd):
    def __init__(self):
        #QT instances
        app = QtWidgets.QApplication([])
        self.main_screen()
        app.exec()
        
    def main_screen(self):
        self.main_screen = uic.loadUi(r".\screens\main.ui")
        self.main_screen.show()
        self.main_screen.start_button.clicked.connect(self.start_button)
        

    def start_button(self):
        username = self.main_screen.login_box.text()
        password = self.main_screen.password_box.text()
        kit = list()
        comment1 = self.main_screen.comment_1.text()
        comment2 = self.main_screen.comment_2.text()
        comment3 = self.main_screen.comment_3.text()
        comment4 = self.main_screen.comment_4.text()
        comments = comment1,comment2,comment3,comment4
        for comment in comments: kit.append(comment)
        print(kit)
        post = self.main_screen.post_box.text()
        timebefore = self.main_screen.time_box.text()
        time = timebefore.replace('X','')
        time = int(time)
        self.start(username,password,kit,post,time)
        


b = FrontEnd()
#a = XavierBot("vlogueirosinsanosoficial@gmail.com","riacho2020",["@_laerton2","@tavares_r_","tavares boi"],'https://www.instagram.com/p/CLagk0IB1C8/',1)