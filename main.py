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
from config_ import CHROME_PROFILE_PATH

# open codes
with open('numbers.txt', 'r', encoding='utf8') as f:
            numbers = [num.strip() for num in f.readlines()]

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
for n in numbers:
    # go to link to send message
    msg = msg.replace(' ', '%20')
    browser.get(f'https://api.whatsapp.com/send/?phone={n}&text={msg}&app_absent=0')
    time.sleep(2)

    # click in button "continue to chat"
    continue_chat = '//*[@id="action-button"]' 
    get_c_chat = browser.find_element_by_xpath(continue_chat)
    get_c_chat.click()
                
    time.sleep(5)

    # click in button 'use whatsapp web'
    use_wpp = '//*[@id="fallback_block"]/div/div/a'
    get_use_wpp = browser.find_element_by_xpath(use_wpp) 
    get_use_wpp.click()

    time.sleep(3)

    # click in input text place in chat
    input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
    input_box = browser.find_element_by_xpath(input_xpath)
    
    # send the message
    input_box.send_keys(Keys.ENTER)
    time.sleep(3)
    

'''    
    # click in input text place in chat            
    input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
    input_box = browser.find_element_by_xpath(input_xpath)
    time.sleep(1)

    # write the message
    pyperclip.copy(msg)

    # send the message  
    input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"'   

    # click in menu
    menu_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
    button_menu = browser.find_element_by_xpath(menu_xpath)
    button_menu.click()

    time.sleep(2)
    
    # click in 'Exit group'
    exit_xpath = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/ul/li[5]/div[1]'
    button_exit = browser.find_element_by_xpath(exit_xpath)
    button_exit.click()
    
    time.sleep(2)

    # confirm 'EXIT GROUP'
    confirmed_xpath = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div'
    button_confirm = browser.find_element_by_xpath(confirmed_xpath)
    button_confirm.click()

    time.sleep(2)

    # close the window
    browser.close()

'''
