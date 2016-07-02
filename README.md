# NCHU-python-Crawler (中興大學課程爬蟲) [![Build Status](https://travis-ci.org/jwlin/ptt-web-crawler.svg?branch=master)](https://travis-ci.org/jwlin/ptt-web-crawler)

### 功能簡介

* 輸出中興大學課程資料, JSON 格式輸出
* 過濾資料內空白、空行
* 支援 Python 3.4

輸出 JSON 格式

    {
      "course": [
        {
          "class": "1",
          "code": "1032",
          "credits": "2",
          "credits_parsed": 2,
          "department": "環境工程學系學士班",
          "discipline": "",
          "enrolled_num": "0",
          "for_dept": "環境工程學系學士班",
          "hours": "2",
          "hours_parsed": "2",
          "intern_location": [
            ""
          ],
          "intern_time": "",
          "language": "中文",
          "location": [
            "C405"
          ],
          "note": "",
          "number": "52",
          "number_parsed": 52,
          "obligatory": "選修",
          "obligatory_tf": false,
          "prerequisite": "",
          "professor": "望熙榮",
          "time": "412",
          "time_parsed": [
            {
              "day": 4,
              "time": [
                1,
                2
              ]
            }
          ],
          "title": "R程式在環工之應用 `Application of R Program on Environmental Engineering",
          "title_parsed": {
            "en_US": "Application of R Program on Environmental Engineering",
            "zh_TW": "R程式在環工之應用"
          },
          "url": "1415",
          "year": "半"
        },
        ...
      ]
    }

### 執行方式
    python3 CoursePickingHelperCrawler.py

### 資料來源 : ##### 感謝中興大學計資中心提供
* [學士班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=U)
* [通識加體育課](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=O)
* [進修部](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=N)
* [在職專班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=W)
* [碩班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=G)
* [博士班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=D)

### 範例
    
預設會將json存在這個路徑底下:

    `os.chdir('/var/www/html/Python-Crawler/nchu/json')`

若沒有這個資料夾會產生exception  併直接將json儲存在當前目底下