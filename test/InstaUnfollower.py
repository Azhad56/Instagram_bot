from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramUnfollower:

    _username = None
    _blacklist = []

    def __init__(self, username, password, unfollowing_speed):
        self.username = username # the username of your instagram account
        self.password = password # the password of your instagram account
        self.unfollowing_speed = unfollowing_speed
        self.driver = webdriver.Chrome()
    def login(self): # method to login into your account
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        username_box = driver.find_element_by_xpath("//input[@name='username']")
        username_box.clear()
        username_box.send_keys(self.username)
        password_box = driver.find_element_by_xpath("//input[@name='password']")
        password_box.clear()
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
        time.sleep(3)

    def find_username(self): # finds the username in the case of the program user is entered an e-mail adress instead of the username as a login info
        driver = self.driver
        self._username = driver.find_element_by_xpath("//a[@class='gmFkV']").text
        print(self._username)

    def find_followings(self): # this functions finds the accounts who are followed by us
        driver = self.driver
        driver.get("https://www.instagram.com/" + self._username + "/")
        time.sleep(2)
        buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
        # who do we follow
        self.following_button = [button for button in buttons if 'following' in button.get_attribute('href')]
        print(self.following_button)
        self.following_button[0].click()
        print("Clicked on Following Button")
        time.sleep(10)
        self.following_window = driver.find_element_by_xpath("//div[@role='dialog']//a")
        print(self.following_window)
        print("check1")
        self.following_number = driver.find_element_by_xpath( "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
        print(self.following_number)
        print("check2")
        counter = 0
        while counter < int( self.following_number) / 4:  # scrolls 5 account each time approximately, if in your browser it differs, change the value with the passed account per scrolling
            self.test_followings = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
            self.test_followings = [account.get_attribute('title') for account in self.test_followings]
            print(self.test_followings)
            self.following_window.send_keys(Keys.PAGE_DOWN)
            counter = counter + 1
            time.sleep(3)
        print(counter)
        print("chech3")
        self.following_accounts = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
        print(self.following_accounts)
        self.following_accounts = [account.get_attribute('title') for account in self.following_accounts]  # the array of the accounts who we follow
        print(self.following_accounts)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click() #closes the following window
        print("Window closed down")



    def find_followers(self): # this functions finds the accounts who are following us
        driver = self.driver
        driver.get("https://www.instagram.com/" + self._username + "/")
        time.sleep(2)
        buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
        # who follows us
        follower_button = [button for button in buttons if 'followers' in button.get_attribute('href')]
        follower_button[0].click()
        time.sleep(2)
        follower_window = driver.find_element_by_xpath("//div[@role='dialog']//a")
        follower_number = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
        print(follower_number)
        counter = 0
        while counter < int( follower_number) / 2:  # scrolls 5 account each time approximately, if in your browser it differs, change the value with the passed account per scrolling
            self.test_followings = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
            self.test_followings = [account.get_attribute('title') for account in self.test_followings]
            follower_window.send_keys(Keys.PAGE_DOWN)
            counter = counter + 1
            time.sleep(3)
        self.follower_accounts = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
        self.follower_accounts = [account.get_attribute('title') for account in  self.follower_accounts]  # the array of the accounts who follows us
        print(self.follower_accounts)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click() #closes the follower window

    def compare_following_and_followers(self, followers, followings): # this function compare the list of followers and followings, and create a blacklist which will include the list of users who we want to unfollow.
        followers = set(self.follower_accounts)
        followings = set(self.following_accounts)
        targetusers = followings - followers
        for acc in targetusers:
            self._blacklist.append(acc)

    def find_target_users(self): #method to find users who we follow but they don't follow us back
        print("Including followers and following buttons")
        time.sleep(2)
        # who do we follow
        # self.find_followings()

        time.sleep(2)

        # who follows us
        self.find_followers()

        time.sleep(2)
        self.compare_following_and_followers(self.follower_accounts,self.following_accounts)
        time.sleep(2)




    def unfollow_target_users(self, unfollowing_speed):
        driver = self.driver
        driver.get("https://www.instagram.com/" + self._username + "/")
        time.sleep(2)
        buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
        # who do we follow
        self.following_button = [button for button in buttons if 'following' in button.get_attribute('href')]
        self.following_button[0].click()
        self.following_window = driver.find_element_by_xpath("//div[@role='dialog']//a")
        self.following_window = driver.find_element_by_xpath("//div[@role='dialog']//a")
        self.following_number = driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
        counter = 0
        while counter < int( self.following_number) / 5:  # scrolls 5 account each time approximately, if in your browser it differs, change the value with the passed account per scrolling
            self.following_window.send_keys(Keys.PAGE_DOWN)
            counter = counter + 1
            time.sleep(0.2)
        self.unfollow_buttons = driver.find_elements_by_xpath("//button[@class='oF4XW sqdOP  L3NKy   _8A5w5   ']")
        for account in self._blacklist:
            self.unfollow_buttons[self.following_accounts.index(str(account))].click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
            time.sleep(unfollowing_speed)
        self.following_window.find_element_by_xpath("//span[@class='glyphsSpriteX__outline__24__grey_9 u-__7']").click()
