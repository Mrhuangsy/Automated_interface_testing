# -*- coding:utf-8 -*-
'''
filename : crm_login_page.py
create by :
create time : 2020/07/31
introduce : crm登录页操作类
'''

import time
from framework.basepage import BasePage
from framework.browser_engine import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CrmLoginPage(BasePage):

    #用户名输入框
    USERNAME_INPUT = "id=>username_input"

    #密码输入框
    PASSWORD_INPUT = "id=>password_input"

    #登录按钮
    LOGIN_BUTTON = "id=>login_act"

    #重复登录弹框
    RELOGIN_ALERT = "id=>layui-layer3"

    #继续登录按钮
    KEEP_LOGIN = "classname=>layui-layer-btn0"

    #设置
    SETTING = "classname=>settings_group"

    #退出登录
    LOGIN_OUT = "id=>LogOut"

    #确定
    AGREE = "classname=>layui-layer-btn0"

    #登录错误弹窗
    ERROR_ALERT = "classname=>layui-layer-title"

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def open_loginpage(self):
        '''打开登录页'''
        self.driver = browser.open_browser()

    def input_username(self,username="hsy"):
        '''输入用户名'''
        print(f"输入用户名='{username}'")
        self.input(self.USERNAME_INPUT,username)

    def input_pwd(self,pwd = "hsy@12345"):
        '''输入密码'''
        print(f"输入密码='{pwd}'")
        self.input(self.PASSWORD_INPUT,pwd)

    def click_login_btn(self):
        '''点击登录'''
        print("点击登录")
        self.click(self.LOGIN_BUTTON)
    
    def get_relogin_alert(self):
        '''获取重复登录弹窗'''
        print("获取重复登录弹窗")
        return self.find_element(self.RELOGIN_ALERT)
    
    def keep_login(self):
        '''继续登录'''
        print("继续登录")
        self.click(self.KEEP_LOGIN)

    def click_login_out(self):
        '''点击退出登录'''
        print("打开设置")
        self.click(self.SETTING)
        print("点击退出")
        self.click(self.LOGIN_OUT)
        time.sleep(2)
        print("确定")
        self.click(self.AGREE)

    def get_error_alert(self):
        '''获取错误弹窗标识'''
        print("获取错误弹窗标题")
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.find_element(self.ERROR_ALERT)))
        return self.find_element(self.ERROR_ALERT).text

    def click_error_alert(self):
        '''确认错误提示'''
        print("确定")
        time.sleep(3)
        self.click(self.AGREE)
        time.sleep(5)