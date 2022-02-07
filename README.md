# FCU Information System Automation Script
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
+ 確認你的Chrome瀏覽器是哪一個版本，例如:我是97開頭的我就去裝97開頭的版本，若版本不是97的就下載解壓後取代我專案裡面的chromedriver.exe
+ 確認環境沒問題後即可執行程式
+ 最後，請確認執行程式時是在虛擬環境中，若不在的話，請在程式當前路徑下使用CMD並輸入```.venv\Scripts\activate.bat```後Enter
+ 祝各位搶課成功
## 影片
[完整播放清單](https://youtube.com/playlist?list=PLkpg2E7EV2RnE99FYN-Xp306nfjEBgbAD)  
[環境安裝及設定教學](https://youtu.be/toN67sgujtU)  
[MyFcuLogin.py腳本示範影片](https://youtu.be/zDYV-ikjutE)  
[逢甲選課系統2.0.py腳本示範影片](https://youtu.be/aPssjrIFcZI)(因網站未開放選課，所以會出現連結找不到之報錯)
## 使用方法
```python 逢甲選課系統2.0.py ```  
即可執行逢甲選課系統2.0.py這個檔案
執行範例如圖:  
![](https://github.com/balsi2001/FCU/blob/main/image.png)
## 逢甲選課系統2.0.py功能及環境需球(繼承[逢甲幹課程式](https://github.com/zephyrxvxx7/FCU-grabbed-class))
### 環境需求
 + selenium
 + chromedriver
 + python
 + ddddocr 
### V.0129.1
- [x] 登錄選課系統並輸入驗證碼功能
- [x] 搶課(xpath沒改的話)

## MyFcuLogin.py功能及環境需求
### 環境需求
 + selenium
 + chromedriver
 + python
### V.0130.1
 - [x] 個人修習紀錄
 - [x] 就學優待申請
