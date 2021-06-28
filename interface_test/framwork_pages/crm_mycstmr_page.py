# -*- coding:utf-8 -*-
'''
filename : crm_mycstmr_page.py
create by :
create time : 2020/07/31
introduce : crm我的客户页面操作类
'''

import os,sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from framework.basepage import BasePage
from framework.browser_engine import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CrmMyCustomerPage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)
    # 客户管理菜单：
    CSTMR_MANAGE="x=>//li[@data-tid='1367297927793479680']" 
    # 我的客户菜单：
    MY_CSTMR="x=>//li[@data-tid='1201411886870020098']" 

    # 我的客户页面：
    MY_CSTMR_IFRAME="id=>iframe1201411886870020098" 
    # 新增/编辑页面：
    PAGEFORM_IFRAME="x=>//iframe[@id='modalwindow']" 

    # 我的客户主表-非固定栏位-客户名称：
    CSTMR_NAME_TABLE = "x=>//html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/table/tbody" 
    # 我的客户主表-非固定栏位：
    UNFIXED_TABLE = "x=>//html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody" 

    # 新增客户按钮：
    ADD_CSTMR_BTN="id=>btnCreate0_0" 
    # 导出按钮：
    EXPORT_BTN="id=>btnExport0_3" 
    # 导入客户基本信息按钮：
    IMPORT_BTN="id=>btnCustom0_4" 
    # 更新工商信息按钮：
    UPDATE_ENTIFO_BTN="id=>btnCustom1_0" 

    # 新增/编辑页返回按钮：
    BTN_RETURN = "id=>btnReturn" 
    # 新增/编辑页定制保存按钮：
    BTN_CUSTOM_SAVE = "id=>btnValidateSave" 
    # 新增/编辑页定制保存并退出按钮:
    BTN_CUSTOM_SAVECLOSE = "id=>btnValidateClose" 
    # 新增/编辑页保存按钮：
    BTN_SAVE = "id=>btnSave"
    #新增/编辑页保存并退出按钮：
    BTN_SAVECLOSE = "id=>btnSaveClose"

    # 客户信息录入栏位：
    CSTMR_NAME="id=>_easyui_textbox_input5" # 客户名称
    CSTMR_NICKNAME="x=>//input[@id='customer_nickname']" # 客户昵称
    WEBSITE="x=>//input[@id='website']" # 官网
    TEL="x=>//input[@id='telephone']" # 电话号码
    FAX="x=>//input[@id='fax']" # 传真
    MAIL="x=>//input[@id='mail']" # 邮箱
    ZIP_NO="x=>//input[@id='zip_no']" # 邮政编码
    RELATION="id=>_easyui_textbox_input1" # 合作关系
    CSTMR_TYPE="x=>//*[@id='_easyui_textbox_input2']"  # 客户类型
    CSTMR_LEVEL="id=>_easyui_textbox_input3" # 客户级别
    INDUSTRY="id=>_easyui_textbox_input4" # 所属行业
    REMARK="x=>//input[@id='remark']" # 备注
    # 新增/编辑自定义确认提示框：
    MSG_CONFIRM = "id=>layui-layer3" # 提示框
    CONFIRM_PERMS="classname=>layui-layer-btn0" # 确定
    CANCEL_PERMS="classname=>layui-layer-btn1" # 取消

    # 删除确认提示框
    DEL_CONFIRM = "id=>layui-layer2"
    


    
    def get_masterrow_editbtn_xpath(self,n):
        '''获取主表指定行修改按钮的xpath值'''
        return f"x=>//a[@onclick=\"gridButton({n},'0','1','Edit','修改客户','mdi mdi-pencil')\"]"

    def get_masterrow_delbtn_xpath(self,n):
        '''获取主表指定行删除按钮的xpath值'''
        return f"x=>//a[@onclick=\"gridButton({n},'0','2','Delete','删除','mdi mdi-trash-can-outline')\"]"
    
    def open_mycstmr(self):
        '''进入我的客户页面'''
        print("客户管理>>",end="")
        self.click(self.CSTMR_MANAGE)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.CSTMR_MANAGE[3:]))).click()
        print("我的客户")
        self.click(self.MY_CSTMR)
        time.sleep(5)
    
    def switch_to_mycstmr(self):
        '''切换到我的客户页面'''
        print("切换到我的客户页面:",self.MY_CSTMR_IFRAME[4:])
        WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,self.MY_CSTMR_IFRAME[4:])))
        #self.switch_frame(self.myCustomerIframe)
    
    def open_master_addpage(self):
        '''打开客户新增页面'''
        print("打开新增客户页:")
        self.click(self.ADD_CSTMR_BTN)
    
    def open_master_editpage(self,n):
        '''打开主表指定行的编辑页面'''
        print(f"打开第{n}行编辑客户页面")
        edit_xpath=self.get_masterrow_editbtn_xpath(n)
        self.click(edit_xpath)
    
    def switch_pageform(self):
        '''切换到编辑页面'''
        print("切换到编辑页面")
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.find_element(self.PAGEFORM_IFRAME)))
        self.switch_frame(self.PAGEFORM_IFRAME)
    
    def input_cstmr_name(self,text):
        '''输入客户名称'''
        time.sleep(5)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of(self.find_element(self.customerName)))
        print(f"输入客户名称：{text}")
        self.input(self.CSTMR_NAME,text)
        time.sleep(5)
        cstmr_select="id=>customer_name_easyui_combobox_i5_0"
        # WebDriverWait(self.driver,10).until(EC.visibility_of(self.find_element(customerSelect)))
        customer_name=self.find_element(cstmr_select).text
        print(f"选择第一个客户:{customer_name}")
        self.click(cstmr_select)
        return customer_name

    def input_cstmr_nickname(self,text):
        '''输入客户昵称'''
        print(f"输入客户昵称：{text}")
        self.input(self.CSTMR_NICKNAME,text)
    
    def input_website(self,text):
        '''输入网址'''
        print(f"输入官网：{text}")
        self.input(self.WEBSITE,text)

    def input_tel(self,text):
        '''输入电话号码'''
        print(f"输入电话号码：{text}")
        self.input(self.TEL,text)
    
    def input_fax(self,text):
        '''输入传真'''
        print(f"输入传真：{text}")
        self.input(self.FAX,text)
    
    def input_mail(self,text):
        '''输入邮箱'''
        print(f"输入邮箱：{text}")
        self.input(self.MAIL,text)
    
    def input_zip_no(self,text):
        '''输入邮政编码'''
        print(f"输入邮政编码：{text}")
        self.input(self.ZIP_NO,text)
    
    def choice_relation(self,n):
        '''选择合作关系'''
        time.sleep(3)
        print(f"点击加载合作关系下拉")
        self.click(self.RELATION)
        relation_Select=f"id=>relation_easyui_combobox_i1_{n}"
        if self.find_element(relation_Select):
            relation=self.find_element(relation_Select).text
            print(f"选择第{n}个选项:{relation}")
            self.click(relation_Select)
            return relation
        else:
            print("无指定合作关系选项可选")
            return ""
    
    def choice_cstmr_type(self,n):
        '''选择客户类型'''
        time.sleep(3)
        print(f"点击加载客户类型下拉")
        self.click(self.CSTMR_TYPE)
        cstmr_type_select=f"id=>customer_type_easyui_combobox_i2_{n}"
        WebDriverWait(self.driver,10).until(EC.visibility_of(self.find_element(cstmr_type_select)))
        cstmr_type=self.find_element(cstmr_type_select).text
        print(f"选择第{n}个选项：{cstmr_type}")
        self.click(cstmr_type_select)
        return cstmr_type
    
    def choice_cstmr_level(self,n):
        '''选择客户级别'''
        time.sleep(3)
        print(f"点击加载客户级别下拉")
        self.click(self.CSTMR_LEVEL)
        cstmr_level_select=f"id=>customer_level_easyui_combobox_i3_{n}"
        WebDriverWait(self.driver,10).until(EC.visibility_of(self.find_element(cstmr_level_select)))
        cstmr_level=self.find_element(cstmr_level_select).text
        print(f"选择第{n}个选项：{cstmr_level}")
        self.click(cstmr_level_select)
        return cstmr_level
    
    def choice_industry(self,n):
        '''选择所属行业'''
        time.sleep(3)
        print(f"点击加载所属行业下拉")
        self.click(self.INDUSTRY)
        industry_select=f"id=>industry_easyui_combobox_i4_{n}"
        if self.find_element(industry_select):
            industry=self.find_element(industry_select).text
            print(f"选择第{n}个选项：{industry}")
            self.click(industry_select)
            return industry
        else:
            print("无指定所属行业可选")
            return ""
    
    def input_remark(self,text):
        '''输入备注'''
        time.sleep(5)
        print(f"输入备注：{text}")
        self.input(self.REMARK, text)
    
    def return_master(self):
        '''返回主页'''
        print("返回")
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.find_element(self.BTN_RETURN)))
        self.click(self.BTN_RETURN)
    
    def custom_save(self):
        '''保存'''
        print("保存")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,"btnValidateSave")))
        self.click(self.BTN_CUSTOM_SAVE)
    
    def custom_save_close(self):
        '''保存并退出'''
        print("保存并退出")
        self.click(self.BTN_CUSTOM_SAVECLOSE)
    
    def save(self):
        '''保存'''
        print("保存")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,"btnSave")))
        self.click(self.BTN_SAVE)
    
    def save_close(self):
        '''保存并退出'''
        print("保存并退出")
        self.click(self.BTN_SAVECLOSE)

    def find_confirm(self):
        '''提示框检查'''
        print("获取提示框")
        return self.find_element(self.MSG_CONFIRM)

    def add_cstmr_perms(self):
        '''确定添加客户权限'''
        print("确定添加客户权限")
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.find_element(self.CONFIRM_PERMS)))
        self.click(self.CONFIRM_PERMS)
    
    def cancel_cstmr_perms(self):
        '''取消添加客户权限'''
        print("取消添加客户权限")
        self.click(self.CANCEL_PERMS)
    
    def del_master_msg(self,n):
        '''删除主表指定行记录'''
        print(f"获取第{n}行记录")
        tab_info = self.get_cstmr_table()[n]
        print(f"第{n}行记录为：",tab_info)
        print(f"删除记录")
        del_xpath = self.get_masterrow_delbtn_xpath(n)
        self.click(del_xpath)
        print("确认删除")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.DEL_CONFIRM[4:])))
        self.click(self.CONFIRM_PERMS)
        return tab_info

    def get_cstmr_table(self):
        '''获取客户列表信息'''
        print("获取客户列表信息:")
        #固定栏位：
        data_list = []
        fix_tablelist = self.find_element(self.CSTMR_NAME_TABLE).find_elements(By.TAG_NAME,"tr")
        for fix_tr in fix_tablelist:
            fix_arr = (fix_tr.text).split( )
            data_list.append(fix_arr)
        #非固定栏位：
        i = 0
        unfix_tablelist = self.find_element(self.UNFIXED_TABLE).find_elements(By.TAG_NAME,"tr")
        for unfix_tr in unfix_tablelist:
            unfix_arr = (unfix_tr.text).split( )
            data_list[i].extend(unfix_arr)
            i += 1
        print(data_list)
        return data_list

if __name__ == '__main__':
    crmcustomer = CrmMyCustomerPage(None)
    tr_id = crmcustomer.get_mastertable_tr(123)
    print(tr_id)
    