import pandas as pd 
import operator

a_plus_list=[]
a_list=[]
a_reduce_list=[]
b_plus_list=[]
b_list=[]
b_reduce_list=[]
c_plus_list=[]
c_list=[]
c_reduce_list=[]
d_plus_list=[]
d_list=[]
d_reduce_list=[]
no_rank_list=[]
def print_list(all_list):
    #sorted(mylist,cmp=lambda x,y:  cmp(int(x['code']),int(y['code']) )   ,reverse=True)#python3 里面没有cmp方法了,因此这种排序方法废弃
    for mylist in all_list:
        mylist=sorted(mylist,key=operator.itemgetter('code'))
        for a in mylist:
            print ("当前股票 %s 股票名字 %s 评级为 %s:   .............. i = %d" % (a['code'],a['code_name'],a['rank'],mylist.index(a)+1))
f= open('new_result1.txt','r')


for line in f.readlines():
	try:
		tmp={}
		tmp['code']=line.split(' ')[1]
		tmp['code_name']=line.split(' ')[3]
		tmp['rank']=line.split(' ')[5]
		#code_list.append(code)

		if 'A+' == tmp['rank']:
		 a_plus_list.append(tmp)
		elif 'A' == tmp['rank']:
		 a_list.append(tmp)
		elif 'A-' == tmp['rank']:
		 a_reduce_list.append(tmp)
		elif 'B+' == tmp['rank']:
		 b_plus_list.append(tmp)
		elif 'B' == tmp['rank']:
		 b_list.append(tmp)
		elif 'B-' == tmp['rank']:
		 b_reduce_list.append(tmp)    
		elif 'C+' == tmp['rank']:
		 c_plus_list.append(tmp)
		elif 'C' == tmp['rank']:
		 c_list.append(tmp)
		elif 'C-' == tmp['rank']:
		 c_reduce_list.append(tmp)         
		elif 'D+' == tmp['rank']:
		 d_plus_list.append(tmp)
		elif 'D' == tmp['rank']:
		 d_list.append(tmp)
		elif 'D-' == tmp['rank']:
		 d_reduce_list.append(tmp)
		else:
		 no_rank_list.append(tmp)
		 print (line)
	except Exception as e:
		print (e)
		print (line+"当前未评级")
		continue
        
      
print ("len(a_plus_list) =%d,len(a_list) =%d,len(a_reduce_list) =%d" % (len(a_plus_list),len(a_list),len(a_reduce_list)))
print ( "len(b_plus_list) =%d,len(b_list) =%d,len(b_reduce_list) =%d" % (len(b_plus_list),len(b_list),len(b_reduce_list)))
print ( "len(c_plus_list) =%d,len(c_list) =%d,len(c_reduce_list) =%d" % (len(c_plus_list),len(c_list),len(c_reduce_list)))
print ( "len(d_plus_list) =%d,len(d_list) =%d,len(d_reduce_list) =%d" % (len(d_plus_list),len(d_list),len(d_reduce_list)))
print ( "len(no_rank_list) =%d" % len(no_rank_list) )

all_list=[a_plus_list,a_list,a_reduce_list,b_plus_list,b_list,b_reduce_list,c_plus_list,c_list,c_reduce_list,d_plus_list,d_list,d_reduce_list]
print_list (all_list)

print (','.join(a['code'] for a in a_plus_list ))



'''

my_code_data=pd.DataFrame()
my_code_data['code']=code_list
my_code_data['code_name']=code_name_list
my_code_data['rank_list']=rank_list
#print(my_code_data)
print ("len(code_list) =%d,len(code_name_list) = %d" % (len(code_list),len(code_name_list))     )
for i in range(len(code_list)):
	print ("code: %s...name:%s" % (code_list[i],code_name_list[i]))

'''
