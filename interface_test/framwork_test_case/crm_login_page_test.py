# -*- coding:utf-8 -*-
'''
filename : crm_login_page_test.py
create by :
create time : 2020/07/31
introduce : crm登录用例
'''

import unittest
import os,sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from framwork_pages.crm_login_page import CrmLoginPage
from framework.browser_engine import browser

class testCrmLoginPage(unittest.TestCase):
    '''crm-登录'''
    # def setUp(self):
    #     self.driver = browser.open_browser() #打开系统
    #     self.loginPage = crmLoginPage(self.driver) #初始化引擎
        

    # def tearDown(self):
    #     #self.loginPage.clickLoginOut() # 退出登录
    #     browser.quit_browser() #关闭浏览器

    
    @classmethod
    def setUpClass(self):
        self.driver = browser.open_browser() #打开系统
        self.login_page = CrmLoginPage(self.driver) #初始化引擎
        
    @classmethod
    def tearDownClass(self):
        browser.quit_browser() #关闭浏览器
        

    def test_01_wrong_username_login(self):
        '''错误用户名登录'''
        self.login_page.input_username("") #用户名
        self.login_page.input_pwd("") #密码
        self.login_page.click_login_btn() #登录
        assert_error_str = "失败"
        result_error_str = self.login_page.get_error_alert()#错误弹窗
        self.assertEqual(result_error_str,assert_error_str)
        self.login_page.click_error_alert()#关闭错误弹窗
    
    def test_02_wrong_pwd_login(self):
        '''错误密码登录'''
        self.login_page.input_username("chency") #用户名
        self.login_page.input_pwd("123456") #密码
        self.login_page.click_login_btn() #登录
        assert_error_str = "失败"
        result_error_str = self.login_page.get_error_alert()#错误弹窗
        self.assertEqual(result_error_str,assert_error_str)
        self.login_page.click_error_alert()#关闭错误弹窗
    
    def test_03_user_injection_login(self):
        '''用户名SQL注入登录测试'''
        self.login_page.input_username("attacker 'or'1=1") #用户名模仿SQL注入
        self.login_page.input_pwd("") #使用正确密码
        self.login_page.click_login_btn() #登录
        assert_error_str = "失败"
        result_error_str = self.login_page.get_error_alert()#错误弹窗
        self.assertEqual(result_error_str,assert_error_str)
        self.login_page.click_error_alert()#关闭错误弹窗

    def test_04_pwd_injection_login(self):
        '''密码SQL注入登录测试'''
        self.login_page.input_username("hsy") #使用正确用户名
        self.login_page.input_pwd("attackerpwd 'or'1=1") #密码模仿SQL注入
        self.login_page.click_login_btn() #登录
        assert_error_str = "失败"
        result_error_str = self.login_page.get_error_alert()#错误弹窗
        self.assertEqual(result_error_str,assert_error_str) 
        self.login_page.click_error_alert()#关闭错误弹窗

    def test_05_nomal_login(self):
        '''正常登录'''
        self.login_page.input_username("chency") #用户名
        self.login_page.input_pwd("") #密码
        self.login_page.click_login_btn() #登录
        time.sleep(2)
        relogin_flag = self.login_page.get_relogin_alert() #重复登录弹窗
        if relogin_flag is not None:
            self.login_page.keep_login() #继续登录
        assert_title = "今天云平台客户关系管理"
        time.sleep(10)
        result_title = self.login_page.get_title() #标题
        self.assertEqual(result_title,assert_title)
        self.login_page.click_login_out() # 退出登录

if __name__ == '__main__':
    unittest.main()
    