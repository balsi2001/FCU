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
import random
from selenium.webdriver.support import expected_conditions as EC
config = configparser.ConfigParser()
config.read('config.ini')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
#chrome_options.add_argument('--headless')這行註解拿掉即可使程式在背景執行

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()

# 帳號及密碼
username = 'd0948511'
password = ''

# 選課代號
classID = []
line=''



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
    print("如果想要1234、2256兩門課就輸入1234 2256後enter，課別之間用空白分開\n")
    line=input('輸入想要的課程，用空白分開，enter結束讀取:')
    classID=line.split()
    print('以下是你選的課程代號')
    for i in classID:
        print(i)
    while len(classID):
        random.shuffle(classID)
        try:
            br=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_Label3"]')))
            br.click()
        except:
            print('連結找不到')
            
        try:
            br=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_tbSubID"]')))
            br.send_keys(classID[len(classID)-1])
        except:
            print('連結找不到')
            
        
        try:
            br=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[8]/input')))
            br.click()
            alert = browser.switch_to_alert()

            alertInfo = alert.text
            currentValue = int(alertInfo[10:13].strip())
            openValue = int(alertInfo[14:18].strip())
            alert.accept()

            print('剩餘名額:', currentValue)
            print('開放名額:', openValue)
            
        except :
            print('連結找不到')
            
        


    # 選課
        try:
            browser.find_element_by_xpath(
            '//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[1]/input').click()
            classID.remove(classID[len(classID)-1])
            print('選課成功')
            sleep(2)
        except:
            print('沒有搶到哦，再接再厲')
            



if __name__ == "__main__":
    login()
    grab()
    browser.quit()