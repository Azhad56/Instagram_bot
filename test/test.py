from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
username = "_instrick"
password = "Dabkdi814126"
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(2)
username_box = driver.find_element_by_xpath("//input[@name='username']")
username_box.clear()
username_box.send_keys(username)
password_box = driver.find_element_by_xpath("//input[@name='password']")
password_box.clear()
password_box.send_keys(password)
password_box.send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
time.sleep(3)
print("Logged In")

driver.get("https://www.instagram.com/" + username + "/")
time.sleep(2)

following_number_str = driver.find_element_by_xpath( "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
following_number_str = following_number_str.split(',')
following_number = ''
for nos in following_number_str:
    following_number = following_number + nos
following_number = int(following_number)
print(following_number)
buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")

following_button = [button for button in buttons if 'following' in button.get_attribute('href')]

following_button[0].click()
time.sleep(2)

# following_window = driver.find_element_by_xpath("//div[@class='_1XyCr']//a")
# print(following_window)
# for i in range(7):
#     time.sleep(4)
#     following_window.send_keys(Keys.PAGE_DOWN)

# print(test_followings)
# driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
print(following_number//14 + 1)
for i in range(following_number//14+1):
    time.sleep(4)
    WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))
    # now scroll
    driver.execute_script('''
        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        fDialog.scrollTop = fDialog.scrollHeight
    ''')
target_followings = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
target_followings = [account.get_attribute('title') for account in target_followings]
followings = set(target_followings)
_blacklist = []
for acc in followings:
    _blacklist.append(acc)
print(target_followings)
print(_blacklist)
# driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click() #window closed
#
#
# driver.get("https://www.instagram.com/" + username + "/")
# time.sleep(2)
#
# buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
#
# following_button = [button for button in buttons if 'following' in button.get_attribute('href')]
#
# following_button[0].click()
# time.sleep(2)
unfollow_buttons = driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")
print(len(unfollow_buttons))
# for account in _blacklist:
#     unfollow_buttons[target_followings.index(str(account))].click()
#     time.sleep(0.5)
#     driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
#     time.sleep(8)
for unfollow_button in unfollow_buttons:
    unfollow_button.click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
    time.sleep(10)
# for i in range(10):
#     unfollow_buttons[i].click()
#     time.sleep(0.5)
#     driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
#     time.sleep(8)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click() #window closed
