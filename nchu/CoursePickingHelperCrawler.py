import requests, json, os

try:
    os.chdir('/var/www/html/Python-Crawler/nchu/json')
    #means cd path
except:
    print('path error, the file will be dump into the current directory')

degree = ['U', 'G', 'D', 'N', 'O', 'W']

try:
	for i in degree:
		re = requests.get('https://onepiece.nchu.edu.tw/cofsys/plsql/json_for_course?p_career=' + i)
		re.raise_for_status()#if request has something wrong, like status code 4xx or 5xx, then it will raise an exception.

		fname = i + '.json'
		with open(fname, 'w', encoding='UTF-8') as f:
			json_str = json.dumps(re.json(), ensure_ascii=False, sort_keys=True)
			#re.json() will check whether 're' is type of json
			#json.dumps will return string.
			f.write(json_str)#f.write only accept and write string into files.

	#print('requests success!!')
except ValueError as e:
	print(e);	

except Exception as e:
	print('requests fail!!')
	print(e)
