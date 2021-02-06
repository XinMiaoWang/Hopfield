# Hopfield

* 程式執行說明：  
1、點擊選擇檔案，分別可選擇Training/Testing Dataset。  
2、迭代次數設定，可輸入大於等於1的整數。  
3、訓練過程是否加入雜訊，輸入0為否，1為是。  
4、完成1~3設定後，點擊「執行」即可顯示回想結果。  
5、迭代進度條可顯示目前迭代進度。  
  
![介面](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/1.PNG)  
  
* 程式碼簡介：
  - GUI設計  
    使用tkinter套件來完成 。createWidgets()函式會建立出使用者介面，包含文字、輸入框、按鈕等等。  
    進度條設計，會隨迭代次數的增加更新迭代進度。  
      
    ![進度條](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/2.png)  
      
  - 資料前處理  
    原始的Dataset是由空格與1組成，這樣的字串形式是無法丟到Hopfield模型進行運算的，因此我把空格的部分都填入-1。  
      
    ![資料前處理](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/3.png)  
    
  - Hopfield Neural Network 設計  
    **步驟一：網路學習**
    用自聯想的方式儲存到離散Hopfield網路上。
    - 計算Weight  
     ![](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/4.PNG)  
     ![](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/5.png)  
     ![](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/6.png)  
        
    - 計算θ  
     ![](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/7.PNG)  
  
    **步驟二：網路回想**  
      若此時有一輸入x進入此網路，我們將此時的輸入視做網路的初始輸出x (0)，緊接著，每個類神經元的後續輸出是由下式計算(非同步)。  
      ![](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/8.PNG)  
    
* 訓練過程加入雜訊  
  預設為隨機選取十分之一的點，將該點的pixel值反轉。  
    
  ![加入雜訊](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/9.png)  
  
* 繪圖  
  使用matplotlib套件裡的matshow()分別畫出原始資料、測試資料與回想結果。  
    
  ![結果](https://github.com/XinMiaoWang/Hopfield/blob/main/demo/11.png)


