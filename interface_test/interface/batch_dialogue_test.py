#-*- coding:utf-8 -*-
'''
filename : batch_dialog_manager_test.py
create by : 
create time : 2019/07/09
introduce : 单元测试文件
'''
import unittest
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture.mysql_db import DB #mysql数据库
from utils.readConfig import readConfig as cf #配置文件读取
from utils.configHttp import runmain as rq #接口请求

class BatchDialogueTest(unittest.TestCase):
    '''批量测试机器人对话'''
    def setUp(self):
        print("对话测试开始前准备")
        self.base_url = cf.get_http("roboturl")
        self.result = {}
    
    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def action(self,payload,expectResults):
        '''测试闲聊机器人对话管理接口'''
        payload = payload.rstrip("&")
        url = self.base_url + payload
        self.result = rq.run_main("get",url)
        realResults = self.result['data']['response'][0] if self.result['data'].get('response') else ''
        self.assertEqual(self.result['code'],200)
        self.assertIsInstance(self.result['data'],dict)
        self.assertEqual(realResults,expectResults)

    @staticmethod
    def getTestFunc(payload,expectResults):
        def func(self):
            self.action(payload,expectResults)
        return func

def __generateTestCases():
    db = DB()
    usecase = db.select("myusecase")
    arglists = []
    for i in range(len(usecase)):
        payload = ""
        expectResults = ""
        for key ,value in usecase[i].items():
            if key not in ['id','expectResults']:
                payload += f"@{key}={value}&"
            elif key in ['expectResults']:
                expectResults = value
        payload = payload.rstrip("&")
        arglists.append((payload,expectResults))
    #print(arglists)
    for args in arglists:
        setattr(BatchDialogueTest,'test_func_%s_%s'%(args[0],args[1]),
                BatchDialogueTest.getTestFunc(*args))
    db.close()
__generateTestCases()

if __name__ == '__main__':
    unittest.main()