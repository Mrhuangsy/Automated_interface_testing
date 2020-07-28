#-*- coding:utf-8 -*-
'''
filename : batch_myrobot_test.py
create by :
create time : 2019/07/09
introduce : 单元测试文件
'''
import unittest
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from utils.readConfig import readConfig
from utils.configHttp import runmain
import json
from utils.otherUtils import otherutils

class BatchJavaTest(unittest.TestCase):
    '''java建权类接口测试'''
    def setUp(self):
        self.base_url = readConfig.get_http('javaurl')

    def action(self,api,heards,data,expected_response,note):
        '''建权类接口测试'''
        data = json.dumps(data).encode('utf-8')
        self.result = runmain.run_main("post", self.base_url + api, heards,data)
        print(note)
        print(api)
        print("接口请求参数：", data)
        print("接口返回结果值：", json.loads(self.result))
        self.assertEqual(json.loads(self.result)['code'], expected_response['code'])
        self.assertIsNotNone(json.loads(self.result)['data'])
        self.assertEqual(json.loads(self.result)['data'], expected_response['data'])
        self.assertEqual(json.loads(self.result)['message'], expected_response['message'])

    @staticmethod
    def getTestFunc(api,heards,data,expected_response,note):
        def func(self):
            self.action(api,heards,data,expected_response,note)
        return func

def __generateTestCases():
    print("黄思远")
    token = otherutils.getToken2()
    print('token:',token)
    usecase = otherutils.read_json_file('../datas/usecase.json')
    arglists=[]
    flag='buildPowerInterface'
    for key,values in usecase.items():
        if key == flag:
            for param in values:
                header = param.get('header',{})
                if header : header['Authorization'] = token
                arglists.append((param['api'], header, param['body'],
                                 param['expected_response'], param['note']))
        else: continue
    print("arglists::",arglists)
    for args in arglists:
        setattr(BatchJavaTest,'test_func_%s'%(flag+args[4]),
                BatchJavaTest.getTestFunc(*args))
__generateTestCases()

if __name__ == '__main__':
    unittest.main()