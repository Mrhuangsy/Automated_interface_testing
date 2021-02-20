#-*- coding:utf-8 -*-
'''
filename : login_test.py
create by :
create time : 2020/07/20
introduce : 单元测试文件
'''
import unittest
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data
from framework.browser_engine import browser
from framework import basepage

class LoginTest(unittest.TestCase):
    '''测试ui登录'''

    def setUp(self):
        self.driver = browser.open_browser()#打开浏览器

    def tearDown(self):
        #browser.quit_browser()#退出浏览器
        pass

    def test_beauty_dialog(self):
        '''登录测试'''
        bp = basepage.BasePage(self.driver)
        bp.input("x=>//input[@type='text']","hsy")#输入账户名
        bp.input("x=>//input[@type='password']","123456")
        bp.click("x=>//button[@class='el-button btn experience_btn el-button--default']")
        bp.sleep(5)
        el = bp.find_element("x=>//span[@class='welcome header-common']")
        print(el)
        pass

if __name__ == '__main__':
    test_data.init_data()
    unittest.main()