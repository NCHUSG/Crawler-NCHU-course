import requests, json, os
from pyquery import PyQuery as pq
try:
    os.chdir('email')
    #means cd path
except:
    print('path error, the file will be dump into the current directory')

team = {"投資理財有風險屁屁買賣沒保險":["劉冠閎", "沈柏瑋", "莊士賢"],
"宇鈞均YEE隊":["王韋鈞", "王鈞硯", "林軒宇"],
"sisker":["陳盈達", "范浩翔", "林師漢"],
"室友好carry隊":["張軒譯"],
"資工對不對":["洪浩祐", "李家駿", "劉鴻文"],
"儒儒修不修":["張泰瑋", "黃翔宇", "林佑如"]
}
email=[]

try:
	re = requests.get('http://140.116.82.70/itsa_scoreboard/')
	d=pq(re.text)
	ac_number=0
	for i in d('tr'):
		print(d(i).text())
		with open('itsa.txt', 'a', encoding='UTF-8') as f:
			print('in')
			f.write(d(i).text())
		# for j in team.keys():			
		# 	if d(i).text() == j:
		# 		print(d(i))
			# 	dtar=d(iv).parent()
			# 	email.append(dtar.children(j+' '+dtar.children('td:eq(1)')+' 'dtar.children('td:eq(2)'))
		# if len(email) == len(team) :
		# 	break
		
	# $.each($('td'),function(ik,iv){
	# 	if($(iv).text()=='投資理財有風險屁屁買賣沒保險'){
	#         $tar=$(iv).parent()
	# 		$tar.children('td:eq()')	        
	#         '''
	#         $.each($tar.children(),function(jk,jv){
	#             if(jk==2){
	#                 console.log($(jv).text())
	# }
	#         })
	# 		'''
	#     }
	# })


	# fname = i + '.txt'
	# 	with open(fname, 'a', encoding='UTF-8') as f:
	# 		f.write('''主任教安：

 #   下列是有參加競賽的學弟
	# 			''')				
	# 	with open(fname, 'a', encoding='UTF-8') as f:
	# 		for i in email:
	# 			f.write(i)

	# 	with open(fname, 'a', encoding='UTF-8') as f:
	# 		f.write('所有人都有解出'+str(ac_number)+'題')
	# 		f.write()
	# 		f.write('學生泰瑋敬上')
	# print('email scrpit finished!!')
except Exception as e:
	print('email scrpit fail!!')
	print(e)

