import unittest

from common.selenium_driver import logger, selenium_driver


class MyUnit(unittest.TestCase):
    def setUp(self):
        logger.info('-------开始执行------')
        self.driver = selenium_driver()


    def tearDown(self):
        logger.info('-------测试结束,关闭浏览器------')
        self.driver.quit()