from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep


# options = webdriver.ChromeOptions()
# options.add_argument('headless')

browser = webdriver.Chrome(ChromeDriverManager().install())
r = browser.get("http://www.linkedin.com")

inputID = browser.find_element_by_name("session_key")
inputPass = browser.find_element_by_name("session_password")
buttonSignIn = browser.find_element_by_class_name("sign-in-form__submit-button")


inputID.send_keys("4321lizhang@gmail.com")
inputPass.send_keys("ChyiChyi123")

buttonSignIn.click()


sleep(3)
browser.close()
#balaaadadsd
print("Hello")
#input.send_keys(Keys.ENTER)
# soup = BeautifulSoup(browser.page_source, features='html.parser')

# print(soup.prettify())

#browser.close()

#
#text = browser.find_element_by_tag_name("body")
#print(text)


