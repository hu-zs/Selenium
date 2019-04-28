#PageObject 是所有页面的父类,在这个类中抽取了一些公用的函数
# 例如初始化  查找元素  获取时间  截图  读取csv函数
# 其它业务视图 在执行具体操作的时候  需要先继承这个pageObject
import time
import csv

from common.selenium_driver import logger


class PageObject(object):
    #初始化
    def __init__(self,driver):
        self.driver = driver

    #查找元素  driver.find_element(By.ID, '')

    def find_element(self, *args):

        return self.driver.find_element(*args)

    #查找多个元素
    def find_elements(self, *args):

        return self.driver.find_elements(*args)

    #获取时间
    def getTime(self):
        self.now = time.strftime('%Y%m%d%H%M%S')
        return self.now

    #截图操作.... desc 对这个图片的描述  例如登录失败
    def getScreenShot(self, desc):
        image_file = '../screenshots/' + str(desc) + '_' + self.getTime() + '.png'

        self.driver.get_screenshot_as_file(image_file)
        logger.info(str(desc) + '生成截图')

    # 封装一个读取csv文件的函数,csv文件的路径,传进一个参数表示要获取哪一行的数据
    def get_csv_data(self, csv_file, line):
        logger.info('------------ 获取csv数据 ----------')
        file = open(csv_file, 'r', encoding='utf-8-sig')

        #把csv读取的所有数据放到reader对象里面
        reader = csv.reader(file)

        # enumerate这个函数可以一行行的获取reader里面的数据,并且可以指定开始的位置
        for index, row in enumerate(reader, 1):
            if index == line:
                return row
