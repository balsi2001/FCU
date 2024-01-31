# FCU Information System Automation Script
 - [x] .py
## 免責聲明
+ 利用```逢甲選課系統2.0.py```搶課來賣等非正當行為皆與本人無關
## 帳號密碼統一於config.ini檔案內設定
![更改帳號密碼即可](https://github.com/balsi2001/FCU/blob/main/%E5%9C%96%E7%89%87.png)  
不要動到上面的[data]  
 + 更改圖中帳號、密碼之部分即可
## 環境安裝  
+ 先到GitHub下載我的壓縮檔或clone下來
+ 解壓縮後在專案當前目錄開啟CMD
+ 輸入```cd FCU```後Enter
+ 輸入```python -m venv .venv```後Enter 
+ 輸入```.venv\Scripts\activate.bat```後Enter
+ 輸入``` pip install  -r requirements.txt```後Enter
+ 確認環境沒問題後即可執行程式
+ 最後，請確認執行程式時是在虛擬環境中，若不在的話，請在程式當前路徑下使用CMD並輸入```.venv\Scripts\activate.bat```後Enter
+ 若執行出現環境問題，請依照下方步驟執行後並重新下載或clone此專案，並重複上述步驟，完成環境的安裝:  
 + 輸入```pip uninstall selenium```後Enter
 + 輸入```pip uninstall ddddocr```後Enter
 + 刪除整份專案
## 安裝步驟
![](https://github.com/balsi2001/FCU/blob/main/%E5%AE%89%E8%A3%9D%E6%AD%A5%E9%A9%9F-1.png)
![](https://github.com/balsi2001/FCU/blob/main/安裝步驟-2.png)
![](https://github.com/balsi2001/FCU/blob/main/安裝步驟-3.png)
![](https://github.com/balsi2001/FCU/blob/main/安裝步驟-4.png)
## 影片
[完整播放清單](https://youtube.com/playlist?list=PLkpg2E7EV2RnE99FYN-Xp306nfjEBgbAD)  
[環境安裝及設定教學](https://youtu.be/toN67sgujtU) (現在不需要chromedriver了，只需要chrome瀏覽器就可以)   
[逢甲選課系統2.0.py測試1影片](https://youtu.be/aPssjrIFcZI)(因網站未開放選課，所以會出現連結找不到之報錯)  
[逢甲選課系統2.0.py測試2影片](https://youtu.be/SznJQvBNjVY)(經選課系統開放，使用程式後確認可正常執行)  
[逢甲選課系統2.0.py示範影片](https://youtu.be/84aGE_nhS34)(退選後成功用程式加選)
## 使用方法
```python 逢甲選課系統2.0.py ```  
即可執行逢甲選課系統2.0.py這個檔案
執行範例如圖:  
![](https://github.com/balsi2001/FCU/blob/main/image.png)
## 逢甲選課系統2.0.py功能及環境需球(繼承[逢甲幹課程式](https://github.com/zephyrxvxx7/FCU-grabbed-class))
### 環境需求
 + selenium
 + chrome瀏覽器
 + python（務必安裝3.9之前的版本-也可以直接點擊後面連結下載：https://www.python.org/downloads/release/python-3912/ ）  
 + ddddocr 
### V.0129.1
- [x] 自動登入選課系統並輸入驗證碼功能
- [x] 自動選課(xpath沒改的話)
- [x] 自動判別驗證碼

## MyFCULogin.py功能及環境需求
### 環境需求
 + selenium
 + chromedriver
 + python
### V.0130.1
 - [x] 個人修習紀錄
 - [x] 就學優待申請
