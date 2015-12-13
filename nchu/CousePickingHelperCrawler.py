import requests, json, os

try:
    os.chdir('json')
    #means cd path
except:
    print('path error, the file will be dump into the current directory')

degree = ['U', 'G', 'D', 'N', 'O', 'W']

try:
	for i in degree:
		re = requests.get('https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=' + i)

		fname = i + '.json'
		with open(fname, 'w', encoding='UTF-8') as f:
			f.write(re.text)

	print('requests success!!')
except Exception as e:
	print('requests fail!!')
	print(e)
