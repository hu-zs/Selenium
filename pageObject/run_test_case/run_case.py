import unittest

import time

from run_test_case import HTMLTestRunner
from test_case.testLoginPage import TestLoginPage

if __name__ == '__main__':
    #测试套件
    suite = unittest.TestSuite()

    #加载
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLoginPage))


    #运行器
    file = open('../reports/' + time.strftime('%Y-%m-%d %H_%M_%S') + '.html', mode='wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='测试登陆', description='宝淘登录的测试报告')

    runner.run(suite)
