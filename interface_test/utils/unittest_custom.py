#-*- coding:utf-8 -*-
'''
filename : unittest_custom.py
create by : 
create time : 2021/06/10
introduce : 自定义类似TestCase的failureException方法功能，添加断言失败截图功能
'''

import unittest,random,traceback
import os,sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

SCREENSHOT_DIR = ".\\report\\reportUItest_%s" % time.strftime("%Y-%m-%d")
class TestCaseCustom(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self,methodName)

    def failure_monitor(self):
        test_case = self

        class AssertionErrorPlus(AssertionError):
            def __init__(self,msg):
                try:
                    cur_method = test_case._testMethodName # 当前test函数名称
                    unique_code = time.strftime("%Y-%m-%d %H_%M_%S") # 生成随机编码，区别同一个test中的不同截图
                    file_name = f"{cur_method}_{unique_code}.png"
                    test_case.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR,file_name)) # 截图生成png
                    print('失败截图已保存到：%s' % file_name)
                    msg += '\n失败截图已保存到：%s' % file_name
                except BaseException:
                    print("截图失败：%S" % traceback.format_exc())
                super(AssertionErrorPlus, self).__init__(msg)
        return AssertionErrorPlus