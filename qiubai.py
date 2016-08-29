#coding='utf-8'
#作者：王凯盛
#2016-8-25 仍有编码问题
#爬糗百的段子
import re
import requests
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class spider():
	def getUrl(self,old_url,total_page):
		all_links=[]
		for i in range(1,total_page+1):
			new_url=re.sub('/page/\d','/page/%d'%i,old_url,re.S)
			all_links.append(new_url)
		return all_links  

	def getSource(self,url):
		
		header={
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
				}
		payload = {
					's': '4907062', 
					}
		
		
		html=requests.get(url,headers=header,params=payload)
		
		return html.text
	
	def getContent(self,source):
		content=re.findall('<div class="content">(.*?)</div>',source,re.S)
		return content
	
	def saveFile(self,info):
		f=open('info.txt','a')
		for each in info:
			f.writelines(each.decode('utf-8'))
			
		f.close()
	
if __name__=='__main__':
	contents=[]
	url_qiubai='http://www.qiushibaike.com/text/page/1/'
	total_page=20
	qiubaiSpider=spider()
	links=qiubaiSpider.getUrl(url_qiubai,total_page)
	for link in links:
		print('准备爬取'+link)
		a=qiubaiSpider.getSource(link)
		content=qiubaiSpider.getContent(a)
		#print('准备爬取'+link)
		for x in content:
			contents.append(x.encode('utf-8'))		
			print(x)
		time.sleep( 1 )
	qiubaiSpider.saveFile(contents)
		
		
		

		
	
