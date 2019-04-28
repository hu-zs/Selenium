import unittest

from businessPage.loginPage import LoginPage
from common.myunit import MyUnit
from common.selenium_driver import logger


class TestLoginPage(MyUnit):

    csv_file = '../data/user.csv'

    def testLogin01(self):
        l = LoginPage(self.driver)

        row = l.get_csv_data(self.csv_file,1)
        logger.info('读取的数据是:' + str(row))

        l.loginAction(row[0],row[1])

        #断言
        self.assertTrue(l.checkLoginStatus())

    def testLogin03(self):
        l = LoginPage(self.driver)

        row = l.get_csv_data(self.csv_file, 3)
        logger.info('读取的数据是:' + str(row))

        # 错误的用户名 和 密码
        l.loginAction('aaaaa', '12334')

        # 断言
        self.assertTrue(l.checkLoginStatus())


