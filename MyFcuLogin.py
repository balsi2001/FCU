from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import ddddocr
import base64
mainUrl = "https://myfcu.fcu.edu.tw/main/InfoMyFcuLogin.aspx"
import configparser
from selenium.webdriver.support import expected_conditions as EC
config = configparser.ConfigParser()
config.read('config.ini')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()
def login():
    browser.get(mainUrl)
    sleep(1)
    browser.find_element_by_xpath(
        '//*[@id="txtUserName"]').send_keys(config['data']['user'])
    sleep(1)
    browser.find_element_by_xpath(
        '//*[@id="txtPassword"]').send_keys(config['data']['pass'])
    sleep(1)
    browser.find_element_by_xpath(
        '//*[@id="OKButton"]').click()
   
    browser.execute_script("document.getElementsByClassName('barbtn')[0].click();")
    sleep(1)
    browser.execute_script("document.getElementsByClassName('icon-block text ng-binding')[4].click();")
    sleep(1)
    browser.execute_script("document.getElementsByClassName('ng-scope')[69].click();")
    sleep(1)
    strScript = 'window.open("'+mainUrl+'");'
    browser.execute_script(strScript)
    sleep(1)
    windows=browser.window_handles

    browser.switch_to.window(windows[-1])
    sleep(1)
    browser.find_element_by_xpath(
        '//*[@id="txtPassword"]').send_keys(config['data']['pass'])
    sleep(1)
    browser.find_element_by_xpath(
        '//*[@id="OKButton"]').click()
    sleep(1)
    browser.execute_script("document.getElementsByClassName('barbtn')[0].click();")
    sleep(1)
    browser.execute_script("document.getElementsByClassName('icon-block text ng-binding')[3].click();")
    sleep(1)
    browser.execute_script("document.getElementsByClassName('ng-scope')[76].click();")
    
   
    #browser.find_element_by_xpath('/html/body/div/div[3]/div/ul/li[10]').click()
    #browser.execute_script("document.getElementsByClassName('nav-item ng-scope active')[0].click();")
    #browser.find_element_by_xpath('').click()
    #browser.execute_script("document.getElementsByClassName('nav-link ng-binding')[9].click();")
if __name__ == "__main__":
    login()