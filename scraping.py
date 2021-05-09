from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep



print("Please enter Login Email or Phone Number")
#usernameStr = str(input())
usernameStr = str("4321lizhang@gmail.com")


print()
print("Password:")
# passwordStr = str(input())
passwordStr = str("ChyiChyi123")


print()
print("Please enter your usernmae exactly how it appears in your profile link (after '/in') :")
link_username = str("andypeh/")

print("Please enter the number of the last posts you want to analyse:")
number_of_posts = int(input())


browser = webdriver.Chrome(ChromeDriverManager().install())

#go to login page
browser.get('https://www.linkedin.com/login')

elementID = browser.find_element_by_id('username')
elementID.send_keys(usernameStr)
elementID = browser.find_element_by_id('password')
elementID.send_keys(passwordStr)
elementID.submit()

recent_activity_link = "https://www.linkedin.com/in/" + link_username + "/detail/recent-activity/shares/"
browser.get(recent_activity_link)


## Scrape post stats

#calculate number of scrolls depending on the input
number_of_scrolls = -(-number_of_posts // 5)  # 5 is LinkedIn's number of posts per scroll


