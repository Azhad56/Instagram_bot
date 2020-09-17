from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import random
import sys
import os

class InstagramBot:

    def __init__(self, username, password):
        #For heroku
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        #for localhost
        # opts = Options()
        # opts.set_headless()
        # assert opts.headless
        self.username = username
        self.password = password
        self.unfollowed = 0
        # self.driver = webdriver.Firefox(options=opts)

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(8)
        driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
        time.sleep(3)
    def find_username(self): # finds the username in the case of the program user is entered an e-mail adress instead of the username as a login info
        driver = self.driver
        self._username = driver.find_element_by_xpath("//a[@class='gmFkV']").text
        print(self._username)
    def like_photo(self):
        driver = self.driver
        print(driver)
        while True:
            follow_count=0
            like_count = 0
            driver.get("https://www.instagram.com/explore/")
            time.sleep(4)
            for i in range(1,3):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            pic_hrefs = [elem.get_attribute('href') for elem in hrefs_in_view]
            pic_hrefs = [elem for elem in pic_hrefs if 'com/p/' in elem]
            print("Total number of user to be Followed",len(pic_hrefs))
            for pic in pic_hrefs:
                driver.get(pic)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    driver.find_element_by_xpath("//*[@aria-label='Like']").click()
                    like_count +=1
                    print("Liked : ",like_count)
                    time.sleep(2)
                except Exception as e:
                    time.sleep(2)
                try:
                    driver.find_element_by_xpath("//button[text()='Follow']").click()
                    follow_count +=1
                    print("Followed : ",follow_count)
                    time.sleep(10)
                except Exception as e:
                    time.sleep(2)
    def unfollow_all(self):
        driver = self.driver
        driver.get("https://www.instagram.com/" + self.username + "/")
        time.sleep(2)

        following_number_str = driver.find_element_by_xpath( "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
        following_number_str = following_number_str.split(',')
        self.following_number = ''
        for nos in following_number_str:
            self.following_number = self.following_number + nos
        self.following_number = int(self.following_number)
        buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")

        following_button = [button for button in buttons if 'following' in button.get_attribute('href')]

        following_button[0].click()
        time.sleep(2)

        print(self.following_number//14 + 1)
        for i in range(7):
            time.sleep(2)
            WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))
            # now scroll
            driver.execute_script('''
                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                fDialog.scrollTop = fDialog.scrollHeight
            ''')
        unfollow_buttons = driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")
        print("Total number of followings to be unfollowed",len(unfollow_buttons))
        if len(unfollow_buttons) <=0:
            self.closeBrowser()
            print("closed Browser since there is no following")
        elif len(unfollow_buttons) <= 59:
            for unfollow_button in unfollow_buttons:
                unfollow_button.click()
                time.sleep(0.5)
                driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
                self.unfollowed += 1
                print("Number of user has unfollowed : ",self.unfollowed)
                time.sleep(5)
            self.closeBrowser()
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        else:
            for unfollow_button in unfollow_buttons:
                unfollow_button.click()
                time.sleep(0.5)
                driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
                self.unfollowed += 1
                print("Number of user has unfollowed : ",self.unfollowed)
                time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click() #window closed
            time.sleep(30)
            self.unfollow_all()
if __name__ == "__main__":

    username = "azhad.ghufran"
    password = "Dabkdi814126"

    ig = InstagramBot(username, password)
    ig.login()
    ig.find_username()
    ig.unfollow_all()
    ig.closeBrowser()
