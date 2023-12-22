####### imports

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from scrapy import Selector
import requests
import csv  



############ selenium part
driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in")
time.sleep(10)
username_input = driver.find_element(By.NAME, "session_key")
password_input = driver.find_element(By.NAME, "session_password")

# Input your LinkedIn credentials
username_input.send_keys("enter your login email")
password_input.send_keys("enter your password")
# breakpoint()
login_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
login_button.click()
time.sleep(10)
driver.get('enter the profile link that you want to scroll')
time.sleep(10)
str = "const origOpen=XMLHttpRequest.prototype.open;XMLHttpRequest.prototype.open=function(t,e){this.addEventListener(\"load\",function(){var t;4===this.readyState&&isVideoFetch(e)&&(pushVideoIDs(t=JSON.parse(this.responseText)),checkAutoScroller(t))}),origOpen.apply(this,arguments)};const autoScroller=setInterval(function(){window.scrollTo(0,document.body.scrollHeight)},1e3);function isVideoFetch(t){return/\/api\/post\/item_list\//.test(t)}function pushVideoIDs(t){t.itemList.forEach(t=>{})}function checkAutoScroller(t){t.hasMore||clearInterval(autoScroller)}"
driver.execute_script(str)
response = Selector(text=driver.page_source)
breakpoint()
like = response.css('.profile-creator-shared-feed-update__container .social-details-social-counts__reactions-count ::text').get()
comments = response.css('.profile-creator-shared-feed-update__container .social-details-social-counts__item--right-aligned ::attr(aria-label)').get()
reposts = response.css('.profile-creator-shared-feed-update__container span:contains(repost) ::text').get()
text = response.css('.profile-creator-shared-feed-update__container .break-words ::text').getall()
breakpoint()