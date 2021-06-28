# -*- coding:utf-8 -*-
'''
filename : crm_mycstmr_page_test.py
create by :
create time : 2021/04/26
introduce : crm我的客户测试用例
'''

import unittest
import os,sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from utils.unittest_custom import TestCaseCustom as testcustom
from framwork_pages.crm_login_page import CrmLoginPage
from framwork_pages.crm_mycstmr_page import CrmMyCustomerPage
from framework.browser_engine import browser
from utils.readConfig import readConfig
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CrmMyCustomerPageTestCase(unittest.TestCase):
    '''我的客户'''
    
    def setUp(self):
        self.failureException = testcustom.failure_monitor(self)

    @classmethod
    def setUpClass(self):
        self.driver = browser.open_browser() # 打开系统
        self.login_page = CrmLoginPage(self.driver) 
        self.login_page.input_username("") # 用户名
        self.login_page.input_pwd("") # 密码
        self.login_page.click_login_btn() # 登录
        time.sleep(2)
        relogin_flag = self.login_page.get_relogin_alert() # 重复登录弹窗
        if relogin_flag is not None:
            self.login_page.keep_login() # 继续登录
        WebDriverWait(self.driver,10).until(EC.title_is(u"今天云平台客户关系管理"))
        url = readConfig.get_testServer('MASERT_URL')
        browser.open_rul(url) # url重定向
        time.sleep(3)
        self.mycstmr_page = CrmMyCustomerPage(self.driver) 
        self.mycstmr_page.open_mycstmr() # 打开我的客户页面
        self.mycstmr_page.switch_to_mycstmr() # 切换到我的客户页面

    
    @classmethod
    def tearDownClass(self):
        self.login_page.switch_default_frame() # 切换到默认页
        self.login_page.click_login_out() # 退出登录
        browser.quit_browser() # 关闭浏览器

    
    def test_01_add_customer(self):
        '''测试用例01：添加客户信息'''
        self.mycstmr_page.open_master_addpage() # 打开新增页面
        self.mycstmr_page.switch_pageform() # 切换到新增页面
        cstmr_name = self.mycstmr_page.input_cstmr_name("厦门科技") # 输入客户名称
        self.mycstmr_page.input_cstmr_nickname("Nti") # 输入客户昵称
        self.mycstmr_page.input_website("http://cloud.nti56.com") # 输入官网
        self.mycstmr_page.input_tel("0592-10293091") # 输入电话号码
        self.mycstmr_page.input_fax("092013") # 输入传真
        self.mycstmr_page.input_mail("cloudNti@163.com") # 输入邮箱
        self.mycstmr_page.input_zip_no("109293") # 输入邮编
        relation = self.mycstmr_page.choice_relation(0) # 选择合作关系
        cstmr_type = self.mycstmr_page.choice_cstmr_type(0) # 选择客户类型
        cstmr_level = self.mycstmr_page.choice_cstmr_level(0) # 选择客户级别
        industry = self.mycstmr_page.choice_industry(0) # 选择所属行业
        self.mycstmr_page.input_remark("test测试123") # 填写备注
        time.sleep(5)
        self.mycstmr_page.custom_save() # 保存
        time.sleep(3)
        falg = self.mycstmr_page.find_confirm() # 客户重复添加提示判断
        if falg:
            self.mycstmr_page.add_cstmr_perms() # 添加客户权限
        time.sleep(5)
        self.mycstmr_page.return_master() # 返回
        time.sleep(5)
        self.mycstmr_page.switch_default_frame() # 切换回主页面
        self.mycstmr_page.switch_to_mycstmr() # 切换至我的客户页面
        cstmr_data = self.mycstmr_page.get_cstmr_table() # 获取页面数据
        # 断言
        self.assertIn(cstmr_name, cstmr_data[0])
        self.assertIn("Nti", cstmr_data[0])
        self.assertIn("http://cloud.nti56.com", cstmr_data[0],"官网地址错误")
        self.assertIn("0592-10293091", cstmr_data[0])
        self.assertIn("092013", cstmr_data[0])
        self.assertIn("cloudNti@163.com", cstmr_data[0])
        self.assertIn("109293", cstmr_data[0])
        self.assertIn(relation, cstmr_data[0])
        self.assertIn(cstmr_type, cstmr_data[0])
        self.assertIn(cstmr_level, cstmr_data[0])
        self.assertIn(industry, cstmr_data[0])
        if not falg:
            self.assertIn("test测试123", cstmr_data[0])
    
    def test_02_edit_customer(self):
        '''测试用例02：修改指定客户信息'''
        self.mycstmr_page.switch_default_frame() # 切换回主页面
        self.mycstmr_page.switch_to_mycstmr() # 切换至我的客户页面
        time.sleep(3)
        self.mycstmr_page.open_master_editpage(0) # 打开主表第一行数据编辑页面
        self.mycstmr_page.switch_pageform() # 切换到编辑页面
        time.sleep(3)
        self.mycstmr_page.input_website("http://127.0.0.1") # 修改网址栏位
        time.sleep(3)
        self.mycstmr_page.save_close() # 保存并退出
        time.sleep(5)
        self.mycstmr_page.switch_default_frame()
        self.mycstmr_page.switch_to_mycstmr()
        cstmr_data = self.mycstmr_page.get_cstmr_table() # 获取页面数据
        # 断言
        self.assertIn("http://127.0.0.1", cstmr_data[0])

    def test_03_delete_customer(self):
        '''测试用例03：删除指定客户信息'''
        self.mycstmr_page.switch_default_frame() # 切换回主页面
        self.mycstmr_page.switch_to_mycstmr() # 切换至我的客户页面
        time.sleep(3)
        table_info = self.mycstmr_page.del_master_msg(0) # 删除主表第一行数据
        time.sleep(3)
        cstmr_data = self.mycstmr_page.get_cstmr_table() # 获取页面数据
        #断言
        self.assertFalse(table_info in cstmr_data)

if __name__ == '__main__':
    unittest.main()
        
    
