# -*- coding:utf-8 -*-
'''
filename : basepage.py
create by :
create time : 2020/07/31
introduce : 网页基本操作类
'''
import time
import os,sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from random import choice
from framework.browser_engine import browser
from utils.log import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    #查找元素
    def find_element(self,selector):
        try:
            element = ''
            if '=>' not in selector:
                return self.driver.find_element_by_id(selector)
            selector_by = selector.split('=>')[0]
            selector_value = selector.split('=>')[1]
            if selector_by == 'id':
                try:
                    element = self.driver.find_element_by_id(selector_value)
                    #打印日志
                    logger.info('获取元素成功！')
                except NoSuchElementException as e:
                    #打印日志
                    logger.error('根据ID获取元素失败，'+e)

            elif selector_by == 'n' or selector_by == 'name':
                element = self.driver.find_element_by_name(selector_value)
            elif selector_by == 'css_selector':
                element = self.driver.find_element_by_css_selector(selector_value)
            elif selector_by == 'classname':
                element = self.driver.find_element_by_class_name(selector_value)
            elif selector_by == 'l' or selector_by == 'link_text':
                element = self.driver.find_element_by_link_text(selector_value)
            elif selector_by == 'p' or selector_by == 'partial_link_text':
                element = self.driver.find_element_by_partial_link_text(selector_value)
            elif selector_by == 't' or selector_by == 'tag_name':
                element = self.driver.find_element_by_tag_name(selector_value)
            elif selector_by == 'x' or selector_by == 'xpath':
                try:
                    element = self.driver.find_element_by_xpath(selector_value)
                    #打印日志
                    logger.info(f"获取元素[{selector_value}]成功！")
                except NoSuchElementException as e:
                    #打印日志
                    print('no such element::>',e)
                    logger.error(f'no such element::>{e}')

            elif selector_by == 's' or selector_by == 'selector_selector':
                element = self.driver.find_element_by_css_selector(selector_value)
            else:
                raise NameError("Please enter a valid type of targeting elements.")
            logger.info('获取元素成功aaa！')
            return element
        except:
            return None

    #输入
    def input(self,selector,text):
        el = self.find_element(selector)
        # print('el:',el)
        try:
            if el:
                el.clear()
            el.send_keys(text)
            #打印日志
            logger.info(f"输入：{text}")
        except NameError as e:
            #打印日志
            logger.error(f"输入出错：{e}")
            print('el2:',el)

    #休眠等待
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        #打印日志
        logger.info(f"休眠等待{seconds}...")

    #点击
    def click(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            #打印日志
            logger.info("点击")
        except NameError as e:
            #打印日志
            logger.error(f"点击操作出错：{e}")
            

    #切到iframe
    def switch_frame(self,selector):
        iframe = self.find_element(selector)
        try:
            self.driver.switch_to_frame(iframe)
            #打印日志
            logger.info("切换标签页")
        except NameError as e:
            #打印日志
            logger.error(f"切换标签页出错{e}")
    
    #切换到默认 frame
    def switch_default_frame(self):
        try:
            self.driver.switch_to_default_content()
            logger.info("切换到默认标签页")
        except NameError as e:
            logger.error(f"切换标签页出错{e}")

    # 处理标准下拉选择框，随机选择
    def select(self,selector):
        select = self.find_element(selector)
        try:
            options_list = select.find_elements_by_tag_name('option')
            del options_list[0]
            s = choice(options_list)
            Select(select).select_by_visible_text(s.text)
            #打印日志
            logger.info("选中下拉值")
        except NameError as e:
            #打印日志
            logger.error(f"选中下拉值出错{e}")

    #执行js
    def execute_js(self,js):
        self.driver.execute_script(js)

    # 模拟回车键
    def enter(self,selector):
        e = self.find_element(selector)
        e.send_keys(Keys.ENTER)
    
    # 模拟空格键
    def space(self,selector):
        e = self.find_element(selector)
        e.send_keys(Keys.SPACE)

    #模拟鼠标左击
    def leftclick(self,element):
        ActionChains(self.driver).click(element).perform()

    # 截图

    # 获取网页标题
    def get_title(self):
        return self.driver.title


if __name__ == '__main__':
    driver = browser.open_browser()
    bp = BasePage(driver)
    aa = bp.find_element("classname=>layui-layer-title")
    print(aa)