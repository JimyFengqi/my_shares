import re,os,sqlite3

import tushare as ts
import time
import pandas as pd
from urllib import request, parse
import requests
from bs4 import BeautifulSoup


class DbManager(object):
	def __init__(self):
		self.dbname=os.getcwd()+'/'+"tusharedb.sqlite3"
		print(self.dbname)
		self.db = sqlite3.connect(self.dbname)
		self.cursor = self.db.cursor()
		self.tablename= 'tushare_list'
		self.initDB(self.tablename)
	def initDB(self,tablename):        
		if not os.path.exists(self.dbname) or os.path.getsize(self.dbname) < 10:
			create_novel_tableString = """
			CREATE TABLE IF NOT EXISTS %s(
			id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
			"code" text NOT NULL,
			"codeName" text NOT NULL,
			"codeRank" text NOT NULL
			)""" % tablename
			print(create_novel_tableString)

			self.cursor.execute(create_novel_tableString)
			self.db.commit()  
			print('DB file not exist, create a new.')

	def addOneData(self,code, codeName, codeRank):
		'''  添加普通用户    '''
		insertData = self.cursor.execute("""INSERT INTO tushare_list 
				(code, codeName, codeRank) VALUES 
				('{0}', '{1}', '{2}')
				""".format(code, codeName, codeRank))
		self.db.commit()


mydb=DbManager()
#获取股票代码以及名字
def get_shares_code():
	basic=ts.get_stock_basics()
	data= basic.iloc[0:-1,0:1]   #得到前面两列内容

	code_list=basic.index.tolist()#通过其索引得到股票代码
	#code_name=basic['name'].tolist()#得到里面的name元素,即股票名称

	c= data.to_dict(orient='dict')  #将df数据转换为dict数据
	return c['name']



def get_rank(code):
	curenttime= int(float( '%.3f' % time.time() )*1000)
	baseurl='http://m.emoney.cn/sosoSD/Handlers/SosoHisHandler.ashx?callback=jQuery1610785045987796412_%s&Type=S&Code=%s&Key=sds&_=%s' % (curenttime,code,curenttime)
	#print(baseurl)

	Referer= 'http://m.emoney.cn/sosoSD/test_pub.html?sc=%s' % code
	headers = {
	    'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0)Gecko/20100101 Firefox/60.0',
	    'Referer': Referer,
	    'Connection': 'keep-alive',
	    'Host':'m.emoney.cn'
	    }
	try:
		page = requests.get(baseurl,headers=headers)
		content=re.split('{|}|,|:|\'',page.text) #通过re的split方法直接切割字符串
		t_code,t_rank =  content[5],content[14]
		return t_code,t_rank 
	except:
		print('[%s] 处理错误' % code)
		return 'error','error'

codelists=get_shares_code()

for code,codeName in codelists.items():
	t_code,t_rank=get_rank(code)
	if t_code == code:
		mydb.addOneData(code,codeName,t_rank)
		print(code,codeName,t_rank)
	else:
		print('[%s %s] 没有找到匹配的内容， 找的的内容为：[%s ,%s]' % (code,codeName,t_code,t_rank))


