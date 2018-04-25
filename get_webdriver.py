#coding:utf-8
import time  
from selenium import webdriver  
import random
'''
webdriver模拟手机行为
第一种方法是通过device name来确定我们要模拟的手机样式
第二种 可以直接指定分辨率以及UA标识，然后模拟手机
'''
  
def mobile_driver1(entity=False):
    '''
        模拟手机浏览器,这里使用device_name直接指定手机类型
    parameters
    ------
        entity 布尔型变量,决定浏览器是否以实体的形式出现,默认为False
    Return
    ------
        driver
        返回一个webdriver实体
    '''
    device_name=[
    'BlackBerry Z30', 
    'Blackberry PlayBook', 
    'Galaxy Note 3',
    'Galaxy Note II',
    'Galaxy S III', 
    'Galaxy S5',
    'Kindle Fire HDX', 
    'LG Optimus L70', 
    'Laptop with HiDPI screen', 
    'Laptop with MDPI screen', 
    'Laptop with touch', 
    'Microsoft Lumia 550', 
    'Microsoft Lumia 950', 
    'Nexus 10', 
    'Nexus 4', 
    'Nexus 5', 
    'Nexus 5X',
    'Nexus 6', 
    'Nexus 6P', 
    'Nexus 7', 
    'Nokia N9', 
    'Pixel 2',
    'Pixel 2 XL',
    'iPad', 
    'iPad Mini',
    'iPad Pro',
    'iPhone SE',
    'iPhone 5',
    'iPhone 6', 
    'iPhone 7',
    'iPhone 8',
    'iPhone 6 Plus', 
    'iPhone 7 Plus',
    'iPhone 8 Plus',
    'iPhone X'    ]
    mobile_emulation = {"deviceName":random.choice(device_name)}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('disable-infobars')
    if entity:
        chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options = chrome_options) 
    return driver

 
def mobile_driver2(entity=False):
    '''
        模拟手机浏览器,这里使用第二种方法指定分辨率以及UA标示 
    parameters
    ------
        entity 布尔型变量,决定浏览器是否以实体的形式出现,默认为False
    Return
    ------
        driver
        返回一个webdriver实体
    '''
    user_agent = [
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    ]
    mobile_emulation = {"deviceMetrics": {"width": 414, "height": 736, "pixelRatio": 6.0}, # 定义设备高宽，像素比
                    "userAgent":random.choice(user_agent) }
    chrome_options = webdriver.ChromeOptions() 
    chrome_options.add_argument('disable-infobars')
    if entity:
        chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options = chrome_options) 
    return driver


def test_driver():
    url='http://www.baidu.com'
    driver1=mobile_driver1()
    time.sleep(1)
    driver2=mobile_driver1(True)
    time.sleep(1)
    driver3=mobile_driver2()
    time.sleep(1)
    driver4=mobile_driver2(True)

    driver1.get(url)
    time.sleep(1)
    driver2.get(url)
    time.sleep(1)
    driver3.get(url)
    time.sleep(1)
    driver4.get(url)
    time.sleep(1)
    print ("driver1.title ; %s" % driver1.title)
    print ("driver2.title ; %s" % driver2.title)
    print ("driver3.title ; %s" % driver3.title)
    print ("driver4.title ; %s" % driver4.title)
    
    driver1.close()
    driver2.close()
    driver3.close()
    driver4.close()

