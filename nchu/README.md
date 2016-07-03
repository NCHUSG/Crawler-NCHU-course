# NCHU-python-Crawler (中興大學課程爬蟲)

* 輸出中興大學課程資料, JSON 格式輸出
* 過濾資料內空白、空行
* 支援 Python 3.4

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

```
sudo apt-get update
sudo apt-get install python3 python3-dev
```

### Installing

```
git clone git@github.com:NCHUSG/Python-Crawler.git
pip3 install -r requirements.txt
```

## Deployment

Add additional notes about how to deploy this on a live system
1. Use Crontab to make crawler automatically run in background

	* `crontab -e`

2. Paste the command below into the bottom of the crontab file :

	* `* * * * * python3 required.py https://onepiece.nchu.edu.tw/cofsys/plsql/crseqry_home fileName.json U [ C10 | C20 C30 U11 U12 U13 U21 U23 U24 U28 U29 U30F U30G U30H U31 U32 U33A U33B U34 U35 U36 U37 U38B U38A U39 U40 U42 U43 U44 U51 U52 U53B U53A U54A U54B U56 U61B U61A U62A U62B U63 U64A U64B U65 U66 ]`

	* 體育課 ( parse PE class )`* * * * * python3 https://onepiece.nchu.edu.tw/cofsys/plsql/crseqry_home fileName.json U [ C10 | C20 C30 U11 U12 U13 U21 U23 U24 U28 U29 U30F U30G U30H U31 U32 U33A U33B U34 U35 U36 U37 U38B U38A U39 U40 U42 U43 U44 U51 U52 U53B U53A U54A U54B U56 U61B U61A U62A U62B U63 U64A U64B U65 U66 ]`

	* 通識課 ( for General Edu class )`* * * * * python3 https://onepiece.nchu.edu.tw/cofsys/plsql/crseqry_gene fileName.json U [ C10 | C20 C30 U11 U12 U13 U21 U23 U24 U28 U29 U30F U30G U30H U31 U32 U33A U33B U34 U35 U36 U37 U38B U38A U39 U40 U42 U43 U44 U51 U52 U53B U53A U54A U54B U56 U61B U61A U62A U62B U63 U64A U64B U65 U66 ]`

### Result
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

## Built With

* python3.4

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Contributors

* **邱冠喻** - *Initial work* - [Pastleo](https://github.com/chgu82837)
* **戴均民** - *Initial work* - [taichunmin](https://github.com/taichunmin)
* **黃川哲** - *Initial work* - [CJHwong](https://github.com/CJHwong)
* **張泰瑋** [david](https://github.com/david30907d)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* 感謝[黃川哲](https://github.com/CJHwong)大大開的坑，讓學弟學了不少的Python，學長們的 code 也讓我受益良多~