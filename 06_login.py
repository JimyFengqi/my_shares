# -*- coding: utf-8 -*-

'''
输入一次账号之后,获得其cookies然后之后的访问就可以免登录了
'''

from selenium import webdriver
from requests import Session
#import requests
from time import sleep
from get_webdriver import mobile_driver1 as mb

req = Session()
req.headers.clear() 
html1=req.get('https://www.zhihu.com/').text#没有登陆之前,没有获取到cookies的时候,获取到的网页内容
f1=open('html1.html','w')
f1.write(html1)

#采用chromedriver,本机需要安装chromedriver,他的版本跟谷歌浏览器版本不同步可能会报错
#wd = webdriver.Chrome() 
wd = mb()
zhihuLogInUrl = 'https://www.zhihu.com/signin'
username=input('请输入你的账号')
password=input("请输入你的密码")
print (zhihuLogInUrl)
wd.get(zhihuLogInUrl)
wd.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').click()
wd.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(username) 
wd.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(password)
sleep(10) #手动输入验证码 
wd.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button').submit() 
sleep(10)#等待Cookies加载
cookies = wd.get_cookies()#获取到cookies
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])#将cookie写入到 requests的session里面
    print (req.cookies)
wd.close()
html2=req.get('https://www.zhihu.com/').text
f2=open('html2.html','w')
f2.write(html2)
f1.close()
f2.close()