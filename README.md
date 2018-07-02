# hospital_chatbot_preprocess
為hospital_chatbot的資料前處理部分，目的在結構化主訴以及為其分群
* [input csv file](https://drive.google.com/open?id=1X-KZ8BpUlMSTF645GtsHREtLibdvXcAt)
* [columns description](https://drive.google.com/open?id=1CyHV_F2go8RAE_vlemtM4ybkNAuEZ5XZ)

## 環境
1. python 3
2. jupyter notebook

## 程式架構
### parse.py
* 由於原始的csv編碼格式有些問題，因此需要重新編碼並輸出需要的欄位

### export_csv.ipynb
* 將parse.py的輸出作為輸入，最後輸出主訴的**症狀**、**部位**、**時間**及**分群結果**
* 其斷詞、詞性分析皆是使用jieba並根據自訂義的辭典來斷詞的
    1. ./userdict/symptom.txt : 症狀辭典
    2. ./userdict/position.txt : 部位辭典
    3. ./userdict/time.txt : 時間辭典
    4. ./userdict/others.txt : 其他