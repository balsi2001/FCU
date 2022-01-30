from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import os
from time import sleep
import ddddocr
import base64
mainUrl = "https://course.fcu.edu.tw"
import configparser
from ast import literal_eval
config = configparser.ConfigParser()
config.read('config.ini')

options = webdriver.ChromeOptions()
options.add_argument('–log-level=3')
options.use_chromium = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

browser=webdriver.Chrome(chrome_options=options)
browser.maximize_window()


username = '帳號'
password = '密碼'


classID = []


grabbed = True


def login():
    
    browser.get(mainUrl)
    ocr = ddddocr.DdddOcr()
    checkCode = 0
    cookies = browser.get_cookies()
    
    img_base64 = browser.execute_script("""
    var ele = arguments[0];
    var cnv = document.createElement('canvas');
    cnv.width = ele.width; cnv.height = ele.height;
    cnv.getContext('2d').drawImage(ele, 0, 0);
    return cnv.toDataURL('image/jpeg').substring(22);    
    """, browser.find_element_by_xpath("//*[@id='ctl00_Login1_Image1']"))

    with open("captcha_login.png", 'wb') as image:
        image.write(base64.b64decode(img_base64))
    with open('captcha_login.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)

    browser.find_element_by_xpath(
        '//*[@id="ctl00_Login1_UserName"]').send_keys(config['data']['user'])
    browser.find_element_by_xpath(
        '//*[@id="ctl00_Login1_Password"]').send_keys(config['data']['pass'])
    browser.find_element_by_xpath(
        '//*[@id="ctl00_Login1_vcode"]').send_keys(res)
    browser.find_element_by_xpath(
        '//*[@id="ctl00_Login1_LoginButton"]').click()

    print('登入成功')


def grab():
    size=0
    while True:
        if browser.current_url != mainUrl:
            break
        
    prompt = "請依照喜好程度由大到小輸入-> "
    #line = input(prompt)
    #line="1234"
    #while line!='\n':
     #   n=literal_eval(input(line))
      #  classID.append(n)
       # size+=1
        #line = input(prompt)
    #for i in classID:
     #   print(i)
    
    while True:
        # select
        
        browser.find_element_by_xpath(
            '//*[@id="ctl00_MainContent_TabContainer1_tabSelected_Label3"]').click()

        # input class ID
        browser.find_element_by_xpath(
            '//*[@id="ctl00_MainContent_TabContainer1_tabSelected_tbSubID"]').send_keys(classID[size])
        browser.find_element_by_xpath(
            '//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[8]/input').click()
        size-=1
        # alert
        sleep(0.7)
        alert = browser.switch_to_alert()

        alertInfo = alert.text
        currentValue = int(alertInfo[10:13].strip())
        openValue = int(alertInfo[14:18].strip())
        alert.accept()

        print('剩餘名額:', currentValue)
        print('開放名額:', openValue)
        
        if(currentValue > 0 and grabbed and size==0 ):
            break
        
        browser.get(browser.current_url)

    # 選課
    if grabbed:
        browser.find_element_by_xpath(
            '//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[1]/input').click()
        print('選課成功')
    sleep(20)


if __name__ == "__main__":
    login()
    grab()
    browser.close()