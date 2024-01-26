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

    print('登入成功')


def grab():
    currentValue=0
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
        try:
            #WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_tbSubID"]')))
            
            browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_tbSubID"]').send_keys(classID[len(classID)-1])
        except:
            print('',end='')
        
        
            
    # 選課  
        if(1):#//*[@id="ctl00_MainContent_TabContainer1_tabSelected_CAPTCHA_imgCAPTCHA"]驗證碼
#//*[@id="ctl00_MainContent_TabContainer1_tabSelected_CAPTCHA_tbCAPTCHA"]驗證碼輸入框
            try:
                    
                    img_base64 = browser.execute_script("""
    var ele = arguments[0];
    var cnv = document.createElement('canvas');
    cnv.width = ele.width; cnv.height = ele.height;
    cnv.getContext('2d').drawImage(ele, 0, 0);
    return cnv.toDataURL('image/jpeg').substring(22);    
    """, browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_CAPTCHA_imgCAPTCHA"]'))


                    with open("captcha_login.png", 'wb') as image:
                    	image.write(base64.b64decode(img_base64))
                    with open('captcha_login.png', 'rb') as f:
                    	img_bytes = f.read()
                    res = ocr.classification(img_bytes)
                    browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_CAPTCHA_tbCAPTCHA"]').send_keys(res)
            except:
                    print('',end='')
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
                            login()
                            print('因為後來系統登入後面的驗證碼就算輸入正確也不會替你加選課程，所以我直接在下一行叫程式睡覺(你們也可以在其他地方叫程式睡覺，只是要注意縮排)，但我不確定10秒夠不夠，以及系統判定是否為機器人的地方在哪裡，這就要你們自己嘗試了')
                            time.sleep(10)
            except:
                print('',end='')      
        #print('browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock"]/span').text)        
        browser.get(browser.current_url)
    
if __name__ == "__main__":
    login()
    grab()
    browser.quit()
