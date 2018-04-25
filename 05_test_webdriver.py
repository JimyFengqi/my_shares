#coding:utf-8
import time  
from selenium import webdriver  

'''
chromeoptions 是一个方便控制 chrome 启动时属性的类。通过 selenium 的源码，可以看到，chromeoptions 主要提供如下的功能：
*设置 chrome 二进制文件位置 (binary_location)
*添加启动参数 (add_argument)
*添加扩展应用 (add_extension, add_encoded_extension)
*添加实验性质的设置参数 (add_experimental_option)
*设置调试器地址 (debugger_address)

'''



mobile_emulation = {"deviceName":device_name} 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-infobars')#chorme启动后不提示黄色边框
chrome_options.add_argument('--headless')#这一个是取消user-agent的标示,有这个参数,就没有实体浏览器了

#添加user-agent,模仿手机行为
chrome_options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1" ')


#通过添加add_experimental_option,增加mobile_emulation选项,然后使webdriver模拟手机行为
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("http://www.baidu.com")
time.sleep(1.5)  
print (driver.title)
driver.close()

