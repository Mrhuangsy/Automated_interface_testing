#-*- coding:utf-8 -*-
'''
filename : batch_myrobot_test.py
create by :
create time : 2019/07/09
introduce : 单元测试文件
'''
import unittest
import requests
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data
from db_fixture.mysql_db import DB
from utils.readConfig import readConfig
from utils.configHttp import runmain
import json

class BatchLoginTest(unittest.TestCase):
    '''登录测试'''
    def setUp(self):
        self.base_url = readConfig.get_http('cloudurl')

    def action(self,api,heards,data,expected_response,note):
        '''登录测试'''
        heards = json.loads(heards)
        data = json.dumps(json.loads(data)).encode('utf-8')
        expected_response = json.loads(expected_response)
        self.result = runmain.run_main("post", self.base_url + api, heards,data)
        print(note)
        print(api)
        print("接口请求参数：",data)
        print("接口返回结果值：", json.loads(self.result))
        self.assertEqual(json.loads(self.result)['isSucceed'], expected_response['isSucceed'])
        self.assertEqual(json.loads(self.result)['errmsg'], expected_response['errmsg'])

    @staticmethod
    def getTestFunc(api,heards,data,expected_response,note):
        def func(self):
            self.action(api,heards,data,expected_response,note)
        return func

def __generateTestCases():
    usecase = DB().select("cloud_test_case", {'flag': 'login'})
    arglists=[]
    flag='login'
    for row in usecase:
        print('row',row)
        if row['flag'] == flag:
            arglists.append((row['api'], row['header'],row['body'],row['expected_response'],row['note']))
        else:continue
    print(arglists)
    for args in arglists:
        setattr(BatchLoginTest,'test_func_%s'%(flag+args[4]),
                BatchLoginTest.getTestFunc(*args))
__generateTestCases()

if __name__ == '__main__':
    unittest.main()