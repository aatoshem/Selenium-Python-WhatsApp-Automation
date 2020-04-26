#/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

f = open("c:/Users/12027/Downloads/names.txt", "r")
k = open("c:/Users/12027/Downloads/message.txt", "r")

msg = ""
for line in k:
    msg = msg + str(line)
name = ""
print(msg)

driver = webdriver.Chrome(executable_path='C:/webdriver/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

time.sleep(15)


# print(name)
for line in f:
    # name = f.strip()
    print("Inside loop: ", line)
    name = line.strip()
    cust_msg = "Hello " + name + msg
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_xpath(
        '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]')
    time.sleep(3)
    msg_box.send_keys(cust_msg + Keys.ENTER)

