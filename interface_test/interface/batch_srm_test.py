#-*- coding:utf-8 -*-
'''
filename : batch_srm_test.py
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
import utils.globalvar as globalvar

class BatchSrmTest(unittest.TestCase):
    '''供应商管理移动端接口测试'''
    def setUp(self):
        self.base_url = readConfig.get_http('cloudurl')

    def action(self,api,heards,data,expected_response,note):
        '''供应链移动端接口测试'''
        data = json.dumps(data).encode('utf-8')
        self.result = runmain.run_main("post", self.base_url + api, heards,data)
        print(note)
        print(api)
        print("接口请求参数：", json.loads(data.decode('utf-8')))
        self.result = json.loads(self.result)
        print("接口返回结果值：", self.result)
        #print("1:",json.loads(self.result)['json'],"::2:",expected_response['json'])
        self.assertEqual(self.result['errcode'], expected_response['errcode'])
        self.assertIsNotNone(self.result['json'])
        #self.assertEqual(self.result['json'], expected_response['json'])
        if self.result['json'] is not None and isinstance(self.result['json'],dict):
            if self.result['json'].keys() in ['allTotal','result']:
                self.assertGreaterEqual(self.result['json']['allTotal'],0)
                self.assertGreaterEqual(self.result['json']['result'].len(),0)
        self.assertEqual(self.result['errmsg'], expected_response['errmsg'])

    @staticmethod
    def getTestFunc(api,heards,data,expected_response,note):
        def func(self):
            self.action(api,heards,data,expected_response,note)
        return func

def __generateTestCases():
    print("黄思远")
    # token = otherutils.getToken_net('cloudurl')
    token = globalvar.get_value("tokens")
    print('token:',token)
    usecase = otherutils.read_json_file(parentdir+'/datas/usecase_srm.json')
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
        setattr(BatchSrmTest,'test_func_%s'%(flag+args[4]),
                BatchSrmTest.getTestFunc(*args))
__generateTestCases()

if __name__ == '__main__':
    unittest.main()