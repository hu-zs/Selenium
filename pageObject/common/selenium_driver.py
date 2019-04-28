#只要别调用我这个函数,我就可以给他提供一个driver

import  logging
from logging import config
from selenium import webdriver

#配置日志... logging是python里面操作日志的模块
config.fileConfig('../config/log.conf')

#获取打印日志的对象
logger = logging.getLogger()


#获取驱动的函数
def selenium_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver