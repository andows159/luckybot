from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

#mainclass
class XavierBot:
    def __init__(self,username,password,set,post,time):
        print(set[0],set[1],set[2])
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

    def write_as_human(self,single_input_field):
        for letter in self.set[self.count]:
            single_input_field.send_keys(letter)
            sleep(randint(1, 5) / 30)

    def comment_on_post(self, set):
        self.set = set
        sleep(3 * self.time)
        driver = self.driver
        
        
        try:
            self.count = 0
            for set[self.count] in range(len(set)):
                comment_box = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
                comment_box.click()
                comment_box = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
                self.write_as_human(comment_box)
                print(self.set[self.count])
                self.count += 1
        except:
            print("pagina não econtrada tentando novamente")
            self.driver.get(self.post)
            sleep(3 * self.time)
            self.count = 0
            for set[self.count] in range(len(set)):
                comment_box = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
                comment_box.click()
                comment_box = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
                self.write_as_human(comment_box)
                print(self.set[self.count])
                self.count += 1

            
            #comment_box.send_keys(self.comment)
        
        #for element in comment:
            
            




a = XavierBot("vlogueirosinsanosoficial@gmail.com","riacho2020",["@diegocunha9","@_laerton2","@tavares_r_"],'https://www.instagram.com/p/CF-R42TAlsW/',1)