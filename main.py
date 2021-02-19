from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

#mainclass
class XavierBot:
    def __init__(self,username,password,set,post,time):
        self.time = time
        self.post = post
        self.username = username
        self.password = password
        #self.console_display()
        self.isvisible()
        self.login()
        sleep(3 * self.time)
        self.driver.get(post)
        self.comment_on_post(set)


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
            self.driver = webdriver.Chrome()
            self.driver.set_window_size(1280,720)
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

    def comment_on_post(self, set):
        self.set = set
        count = 0
        set = [f'test{count}',f'test{count}',f'test{count}']
        sleep(3 * self.time)
        driver = self.driver
        sleep(3 * self.time)

        comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh"]')
        comment_box.click()
        comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh focus-visible"]')
        #comment_box.send_keys(set)
        while True:
            
            
            for account in set:
                count += 1
                set = [f'test{count}',f'test{count}',f'test{count}']
                
                for letter in account:
                    comment_box.send_keys(letter)
                    sleep((randint(1,6) /30))

                button = driver.find_element_by_xpath('//button[@type="submit"]')
                button.click()
                sleep((randint(45,60)) * self.time)
                comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh"]')
                try:
                    comment_box.click()
                    
                except:
                    print("Elemento bloqueado")
                comment_box = driver.find_element_by_xpath('//textarea[@class="Ypffh focus-visible"]')
                
                
            




a = XavierBot("vlogueirosinsanosoficial@gmail.com","riacho2020",["teste1","teste2","teste3"],'https://www.instagram.com/p/CLagk0IB1C8/',1)