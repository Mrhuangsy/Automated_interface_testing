#-*- coding:utf-8 -*-
'''
filename : login_test.py
create by :
create time : 2020/07/20
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

class LoginTest(unittest.TestCase):
    '''测试登录接口'''

    def setUp(self):
        self.db = DB()
        self.base_url = readConfig.get_http("cloudurl")
        self.table_name = "cloud_test_case"
        self.usecase = self.db.select(self.table_name,{'flag':'login'})
        self.result = {}

    def tearDown(self):
        self.db.close()
        #print(self.result)

    def test_beauty_dialog(self):
        '''登录测试'''
        heards = {"Content-Type":"application/json","appCode":"CRM"}
        data = '{"username": "hsy","userpswd": "6b210b0574e5dd3d099cf44fe5b9745f","islogin": true }'
        self.result = runmain.run_main("post",self.base_url+'platform/Login/GetLogin?',heards,json.dumps(json.loads(data)).encode('utf-8'))
        print("结果：",json.loads(self.result)['errmsg'])
        self.assertEqual(json.loads(self.result)['isSucceed'], True)

if __name__ == '__main__':
    test_data.init_data()
    unittest.main()