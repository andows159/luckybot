from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

#mainclass
class XavierBot:
    def __init__(self,username,password,set,post,time):
        self.time = time
        self.post = post
        self.set = set
        self.username = username
        self.password = password
        #self.console_display()
        self.start()
       

    def start(self):

        self.isvisible()
        self.login()
        try:
            self.comment_on_post(self.set)
        except:
            self.comment_on_post(self.set)



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
        visible = True
        #visible = self.visible
        if visible:
            
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            #options.add_argument("--headless")
            self.driver = webdriver.Chrome(chrome_options=options)
            
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
    def comment_on_post(self, set):
        self.browse_to_post(self.post,'//button[@type="submit"]')
        self.set = set
        sleep(3 * self.time)
        driver = self.driver
        sleep(3 * self.time)

        comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh"]')
        comment_box.click()
        comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh focus-visible"]')
        #comment_box.send_keys(set)
        while True:
            
            for account in set:
                
                
                for letter in account:
                    comment_box.send_keys(letter)
                    sleep((randint(3,30) /30)) 

                button = driver.find_element_by_xpath('//button[@type="submit"]')
                button.click()
                print(f"account {account} commented on post {self.post}")
               
                sleep((randint(10,20)) * self.time)
                comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh"]')
                try:
                    comment_box.click()
                    
                    
                except:
                    print("Elemento bloqueado")
                comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh focus-visible"]')
                
                
            



class Console(XavierBot):
    pass

a = XavierBot("vlogueirosinsanosoficial@gmail.com","riacho2020",["@_laerton2","@tavares_r_","tavares boi"],'https://www.instagram.com/p/CLagk0IB1C8/',1)