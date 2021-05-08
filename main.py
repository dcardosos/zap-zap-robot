# librarys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip
import time
import sys
from config import CHROME_PROFILE_PATH

# open codes
with open('codes.txt', 'r', encoding='utf8') as f:
            codes = [code.strip() for code in f.readlines()]

# open messages
with open('message.txt', 'r', encoding='utf8') as f:
    msg = f.read()

# instanciate option
options = Options()
options.add_argument(CHROME_PROFILE_PATH)

# creating a browser with options
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

# open and maximize window
browser.maximize_window()

# read each code in codes.txt
for c in codes:
    # come in group link
    browser.get(f'https://web.whatsapp.com/accept?code={c}')
    time.sleep(10)

    # click in button "Join group"
    join = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]' 
    get_join = browser.find_element_by_xpath(join)
    get_join.click()
                
    time.sleep(5)
    
    # click in input text place in chat            
    input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
    input_box = browser.find_element_by_xpath(input_xpath)
    time.sleep(2)

    # write the message
    pyperclip.copy(msg)
   
    # send the message  
    input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"'   
    input_box.send_keys(Keys.ENTER)
    time.sleep(5)
    
    # close the window
    browser.close()
