from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import ddddocr
from datetime import datetime
import base64
mainUrl = "https://course.fcu.edu.tw"
import configparser
import random
from selenium.webdriver.support import expected_conditions as EC
config = configparser.RawConfigParser()
config.read('config.ini')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
#chrome_options.add_argument('--headless')這行註解拿掉即可使程式在背景執行

browser = webdriver.Chrome(options=chrome_options)
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
    """, browser.find_element(By.XPATH,"//*[@id='ctl00_Login1_Image1']"))

    with open("captcha_login.png", 'wb') as image:
        image.write(base64.b64decode(img_base64))
    with open('captcha_login.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)

    browser.find_element(By.XPATH,
        '//*[@id="ctl00_Login1_UserName"]').send_keys(config['data']['user'])
    browser.find_element(By.XPATH,
        '//*[@id="ctl00_Login1_Password"]').send_keys(config["data"]["pass"])
    browser.find_element(By.XPATH,
        '//*[@id="ctl00_Login1_vcode"]').send_keys(res)
    browser.find_element(By.XPATH,
        '//*[@id="ctl00_Login1_LoginButton"]').click()
    
    if '登出' in browser.page_source:
    	print('登入成功')
    else:
    	login()

def grab():
    currentValue=0
    t=0.1
    print("如果想要1234、2256兩門課就輸入1234 2256後enter，課別之間用空白分開\n")
    line=input('輸入想要的課程，用空白分開，enter結束讀取:')
    classID=line.split()
    print('以下是你選的課程代號')
    for i in classID:
        print(i)
    
    while len(classID):
        currentValue=0
        

        random.shuffle(classID)
        try:
            #WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_Label3"]')))
            browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_Label3"]').click()
            
        except:
            print('',end='')
        sleep(t)
        try:
            #WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_tbSubID"]')))
            
            browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_tbSubID"]').send_keys(classID[len(classID)-1])
            
        except:
            print('',end='')
        sleep(t)        
            
    # 選課  
        if(1):#//*[@id="ctl00_MainContent_TabContainer1_tabSelected_CAPTCHA_imgCAPTCHA"]驗證碼
#//*[@id="ctl00_MainContent_TabContainer1_tabSelected_CAPTCHA_tbCAPTCHA"]驗證碼輸入框
            
            try:
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[1]/input')))
                    browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[1]/input').click()
                    
                    #//*[@id="ctl00_MainContent_TabContainer1_tabSelected_gvToAdd"]/tbody/tr[2]/td[1]/input
                    if browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock"]/span').text.find('加選成功')!=-1:
                        print(browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock"]/span').text)
                        classID.remove(classID[len(classID)-1])
                    else:
                        
                        print(browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock"]/span').text)
                        if '驗証碼' in browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock"]/span').text:
                            print(f'增加待機時間為{t}秒')
                            t=t+0.1
                            login()

                            
            except:
                print('',end='')      
        #print('browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock"]/span').text)        
        browser.get(browser.current_url)
        sleep(t)
        with open('t_to_wait','w')as ff:
        	ff.write(str(t))
    
if __name__ == "__main__":
    login()
    grab()
    browser.quit()
