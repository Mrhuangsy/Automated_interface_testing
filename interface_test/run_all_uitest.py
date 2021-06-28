#-*- coding:utf-8 -*-
'''
filename : run_AllUITest.py
create by : 
create time : 2021/04/26
introduce : 执行自动化UI测试总入口，具体操作包括：
            1、执行指定单元测试文件
            2、生成测试报告
            3、发送测试报告邮件通知
'''
import os,sys
parentdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,parentdir)
import HTMLTestRunnerCN as HTMLTestRunner
import unittest
import time
from db_fixture import test_data
from utils.readConfig import readConfig
from utils.configEmail import sendemail
from utils.log import logger
from utils.otherUtils import otherutils
import utils.globalvar as globalvar
 
report_path = os.path.join(parentdir, 'report\\')
on_off = readConfig.get_email('on_off')
 
class AllUITest:#定义一个类AllUITest
    def __init__(self):#初始化一些参数和数据

        now = time.strftime("%Y-%m-%d %H_%M_%S")
        self.fn = now + '_uitest_result.html'#定义自动化测试文件名
        now_day = time.strftime("%Y-%m-%d")
        self.folder = report_path+'reportUItest_'+now_day+'\\' #新建一个文件加
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        self.caseListFile = os.path.join(parentdir, "caselist_ui.txt")#配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(parentdir, "framwork_test_case")#真正的测试断言文件路径
        self.caseList = []
 
    def set_case_list(self):
        """
        读取caselist_ui.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):# 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))#读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()
 
    def set_case_suite(self):
        """
        :return:
        """
        logger.info("获取测试用例......")
        self.set_case_list()#通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:#从caselist元素组中循环取出case
            case_name = case.split("/")[-1]#通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name+".py")#打印出取出来的名称
            logger.info(f"测试用例文件：{case_name}.py")
            #批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)#将discover存入suite_module元素组
            print('suite_module:'+str(suite_module))
            logger.info('suite_module:'+str(discover))
        if len(suite_module) > 0:#判断suite_module元素组是否存在元素
            for suite in suite_module:#如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:#从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        logger.info("获取测试用例结束......")
        return test_suite#返回测试集
 
    def run(self):
        """
        run test
        :return:
        """
        start_time = time.time()
        try:
            logger.info("自动化测试开始......")
            print("自动化测试开始......")
            
            suit = self.set_case_suite()#调用set_case_suite获取test_suite

            if suit is not None:#判断test_suite是否为空 

                filename = self.folder + self.fn
                fp = open(filename, 'wb')#打开result/20181108/report.html测试报告文件，如果不存在就创建
                #调用HTMLTestRunner
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试内容:客户关系管理系统UI自动化测试')
                logger.info("运行测试用例......")
                myresult = runner.run(suit)
                otherutils.writeIntoModel(myresult.result,self.folder)#写入word报告
                logger.info("运行测试用例结束......")
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.info("test error:"+str(ex))
            print("test error:",str(ex))
 
        finally:
            logger.info("自动化测试结束......")
            print("自动化测试结束......")
            fp.close()

        end_time = time.time()
        exec_time = (end_time - start_time)*1000
        logger.info(f"耗时{exec_time}ms")
        #判断邮件发送的开关
        logger.info("发送测试报告......")
        print("发送测试报告......")
        if on_off == 'on':
            sendemail.send(self.fn)
            logger.info("测试报告发送成功，请打开邮箱查看......")
            print("测试报告发送成功，请打开邮箱查看......")
        else:
            logger.info("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")
        logger.info("=="*20)

if __name__ == '__main__':
    AllUITest().run()
