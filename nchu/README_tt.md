# NCHU-python-Crawler - ParseVersion (中興大學課程爬蟲-**自行parse版本**) [![Build Status](https://travis-ci.org/jwlin/ptt-web-crawler.svg?branch=master)](https://travis-ci.org/jwlin/ptt-web-crawler)

### 功能簡介

* Parse 教務處課程資訊網頁的資料, __JSON__ 格式輸出
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
    
    1. 學士班
        * `python3 required.py https://onepiece.nchu.edu.tw/cofsys/plsql/crseqry_home fileName.json U [ C10 | C20 C30 U11 U12 U13 U21 U23 U24 U28 U29 U30F U30G U30H U31 U32 U33A U33B U34 U35 U36 U37 U38B U38A U39 U40 U42 U43 U44 U51 U52 U53B U53A U54A U54B U56 U61B U61A U62A U62B U63 U64A U64B U65 U66 ]`
    2. 體育課
        * `python3 https://onepiece.nchu.edu.tw/cofsys/plsql/crseqry_home fileName.json U [ C10 | C20 C30 U11 U12 U13 U21 U23 U24 U28 U29 U30F U30G U30H U31 U32 U33A U33B U34 U35 U36 U37 U38B U38A U39 U40 U42 U43 U44 U51 U52 U53B U53A U54A U54B U56 U61B U61A U62A U62B U63 U64A U64B U65 U66 ]`
    3. 通識課
        * `python3 https://onepiece.nchu.edu.tw/cofsys/plsql/crseqry_gene fileName.json U [ C10 | C20 C30 U11 U12 U13 U21 U23 U24 U28 U29 U30F U30G U30H U31 U32 U33A U33B U34 U35 U36 U37 U38B U38A U39 U40 U42 U43 U44 U51 U52 U53B U53A U54A U54B U56 U61B U61A U62A U62B U63 U64A U64B U65 U66 ]`

### 資料來源 :  <h4>感謝中興大學計資中心提供</h4>
* [學士班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=U)
* [通識加體育課](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=O)
* [進修部](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=N)
* [在職專班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=W)
* [碩班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=G)
* [博士班](https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=D)

### 範例
    
預設會將json存在這個路徑底下:

    os.chdir('/var/www/html/Python-Crawler/nchu/json')

若沒有這個資料夾會產生exception  併直接將json儲存在當前目底下