from datetime import date
from email import header
import imp
from wsgiref import headers

import requests
import bs4
import re
import ddddocr
import urllib3
import base64
import urllib.request

from PIL import Image
import http.cookiejar as cookielib

from selenium.webdriver.chrome.options import Options
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    browser.get('https://course.fcu.edu.tw')
    ocr = ddddocr.DdddOcr()
url = 'https://course.fcu.edu.tw'
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
print(res)
user = browser.find_element_by_id('ctl00_Login1_UserName')
passwd = browser.find_element_by_id('ctl00_Login1_Password')
vcode=browser.find_element_by_id('ctl00_Login1_vcode')


userid='這裡改成你的帳號'
userpw='這裡改成你的密碼'
user.send_keys(userid)
passwd.send_keys(userpw)
vcode.send_keys(res)


button = browser.find_element_by_id('ctl00_Login1_LoginButton')

button.click()
    