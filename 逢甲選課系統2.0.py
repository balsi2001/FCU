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
mainUrl = "https://course.fcu.edu.tw"
import configparser
from selenium.webdriver.support import expected_conditions as EC
config = configparser.ConfigParser()
config.read('config.ini')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()

# 帳號及密碼
username = 'd0948511'
password = ''

# 選課代號
classID = ''

# 確定要搶課嗎？
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
    while True:
        if browser.current_url != mainUrl:
            break
    while True:
        # select
        try:
            br=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_Label3"]')))
        except:
            print('連結找不到')
            browser.quit()
        browser.find_element_by_xpath(
            '//*[@id="ctl00_MainContent_TabContainer1_tabSelected_Label3"]').click()
        try:
            br=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_tbSubID"]')))
        except:
            print('連結找不到')
            browser.quit()
        # input class ID
        browser.find_element_by_xpath(
            '//*[@id="ctl00_MainContent_TabContainer1_tabSelected_tbSubID"]').send_keys(classID)
        try:
            br=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[8]/input')))
        except:
            print('連結找不到')
            browser.quit()
        browser.find_element_by_xpath(
            '//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[8]/input').click()

        # alert
        sleep(0.7)
        alert = browser.switch_to_alert()

        alertInfo = alert.text
        currentValue = int(alertInfo[10:13].strip())
        openValue = int(alertInfo[14:18].strip())
        alert.accept()

        print('剩餘名額:', currentValue)
        print('開放名額:', openValue)

        if(currentValue > 0 and grabbed):
            break

        browser.get(browser.current_url)

    # 選課
    if grabbed:
        try:
            br=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[1]/input')))
        except:
            print('連結找不到')
            browser.quit()
        browser.find_element_by_xpath(
            '//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[1]/input').click()
        print('選課成功')
    sleep(5)


if __name__ == "__main__":
    login()
    grab()
    browser.quit()