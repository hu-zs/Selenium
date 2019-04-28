from selenium.webdriver.common.by import By

from common.selenium_driver import logger
from data.apiUrl import BASE_URL, INDEX_URL
from pageObject.pageObject import PageObject


class LoginPage(PageObject):

    # 需要查找的元素
    login_link = (By.LINK_TEXT, '登录')
    name_input = (By.ID, 'username')
    pwd_input = (By.ID, 'password')
    code_input = (By.ID, 'captcha')
    login_btn = (By.XPATH, "//input[@class='submit']")
    tuichu_link = (By.XPATH, "//a[contains(text(),'[退出]')]")


    def loginAction(self, name, pwd):

        logger.info('--------打开首页页面---------')
        self.driver.get(BASE_URL + INDEX_URL)


        self.find_element(*self.login_link).click()
        logger.info('--------进入登录页面---------')

        self.find_element(*self.name_input).clear
        logger.info('输入用户名:' + name)
        self.find_element(*self.name_input).send_keys(name)

        self.find_element(*self.pwd_input).clear()
        logger.info('输入密码:' + pwd)
        self.find_element(*self.pwd_input).send_keys(pwd)

        self.find_element(*self.code_input).clear()
        self.find_element(*self.code_input).send_keys('ABCD')

        logger.info('----------点击登录按钮-------------')
        self.find_element(*self.login_btn).click()


    def checkLoginStatus(self):
        text = self.find_element(*self.tuichu_link).text

        if text == '[退出]':
            logger.info('-------登录成功------')
            return True
        else:
            logger.info('------登录失败,截图--------')
            self.getScreenShot('登录失败')
            return False

