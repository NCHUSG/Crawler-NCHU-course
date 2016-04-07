import requests, json, jieba, operator, sys
token = 'CAACEdEose0cBAMwiApnJs2D0FOQ121qZAZBP2FqZAHGXL9kKqXUOVQBwX0g0opZC5SIZB9Cvl1jBslxFKg1f8lIGPXaFOWONNvItercyC5Fnv3VOdVpRjCJzP1mNTAc7fEezys54M5s04OZBgvtTNQp0bdDpRHsYwO3Cn9adjHPuAYIUNdfMf7csAsSBApkBYPj6rfDA5OZBgZDZD'
re = requests.get('https://graph.facebook.com/v2.5/747693215323904/posts?since=1420041600&limit=100&access_token=' + token)
#if you want to chose a specific time span, append 'since=1420041600' after 'post?' 
#cause it use Unix seconds, so 1420041600 means 2015/01/01
jo=json.loads(re.text)
count=0
corpus = []
while 'paging' in jo:
	for i in jo['data']:
		if 'message' in i and 'story' in i:
			#print('===================')
			#print('this is my full story : ' + i['message'])
			#print('with : ' + i['story'])
			#print('===================')
			corpus+=jieba.cut(i['message'])
		elif 'message' in i:
			#print('this is my post : ' + i['message'])
			corpus+=jieba.cut(i['message'])	
		#elif 'story' in i:
			#print('this is by sharing : ' + i['story'])
		count+=1		
	re = requests.get(jo['paging']['next'])
	jo=json.loads(re.text)

print('total %d posts' % count)

dic = {}
for i in corpus:
	if i not in dic :
		dic[i] = 1
	else :
		dic[i] +=1
sorted_word = sorted(dic.items(), key = operator.itemgetter(1), reverse = True)

fname = sys.argv[1]
pname = sys.argv[2]
with open(fname, 'a', encoding='UTF-8') as f:
	count=0
	f.write('\n'+pname+'`s analysis : '+'\n')
	for i in sorted_word:
		if len(i[0]) >= 2:
			print(i[0],i[1])
			f.write(str(count+1)+' :'+str(i)+'\n')
			count+=1
		if count >= 30 :
			break


