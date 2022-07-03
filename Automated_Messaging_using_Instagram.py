from email import message
from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

user = ['user1', 'user2', 'user3']
message_ = ("Ignore this message")


class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()


    def login(self):
        self.bot.get(self.base_url)
        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME,'username')))
        
        print(enter_username)
        print("Hey")
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME,'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)


        self.bot.find_element(by = By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        #time.sleep(6)
        self.bot.implicitly_wait(6)
        self.bot.find_element(by = By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        time.sleep(4)
        print("Hey")
        

        self.bot.find_element(by = By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(3)

        self.bot.find_element(by = By.XPATH, value='//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
        time.sleep(6)


        for i in user:
            self.bot.find_element(by = By.XPATH, value='/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)

            time.sleep(2)

            self.bot.find_element(by = By.XPATH, value='/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div').click()
            time.sleep(2)

            self.bot.find_element(by = By.XPATH, value='/html/body/div[6]/div/div/div[1]/div/div[3]/div/button').click()
            time.sleep(2)

            send = self.bot.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
  
    # types message
            
            
            send.send_keys(self.message)
            time.sleep(1)

            send.send_keys(Keys.RETURN)
            time.sleep(2)


            self.bot.find_element(by = By.XPATH, value='/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(2)





def init():
    bot('username','password',user,message_)

    print("DOne")


init()

