# -*- coding:utf-8 -*-
'''
filename : browser_engine.py
create by :
create time : 2020/07/31
introduce : 浏览器基本操作类
'''
from selenium import webdriver
from utils.readConfig import readConfig
import win32api,win32con

class Browser(object):

    #打开浏览器
    def open_browser(self):
        browser = readConfig.get_browser_type('browserName')
        url = readConfig.get_testServer('URL')
        if browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'IE':
            self.driver = webdriver.Ie()
        self.driver.set_window_size(0.8*win32api.GetSystemMetrics(win32con.SM_CXSCREEN),0.8*win32api.GetSystemMetrics(win32con.SM_CYSCREEN)) #分辨率
        #print(url)
        self.driver.get(url)
        return self.driver

    #打开url站点
    def open_rul(self,url):
        self.driver.get(url)

    #关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    #浏览器前进操作
    def forward(self):
        self.driver.forward()

    #浏览器后退操作
    def back(self):
        self.driver.back()

    # 隐式等待
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)

browser = Browser()
if __name__ == '__main__':
    browser.open_browser()