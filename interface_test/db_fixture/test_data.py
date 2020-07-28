#-*- coding:utf-8 -*-
'''
filename : test_data.py
create by : 
create time : 2019/07/09
introduce : 编写测试用例，并保存到指定数据库表
'''
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture.mysql_db import DB
 
# create data
'''
cloud_test_case：测试用例表
flag：测试标签，自定义，测试用例编写时，主要用于测试范围判断
api：接口地址
header：请求头
body：请求参数
expected_response：预期返回值
note：备注
'''
datas = {
  'cloud_test_case':[
      {
        'flag':'login',
        'api':'platform/Login/GetLogin?',
        'header':'{"Content-Type":"application/json","appCode":"CRM"}',
        'body':'{"username": "hsy","userpswd": "","islogin": true}',
        'expected_response':'{"errcode": 0,"isSucceed": true,"errmsg": "OK","json": {"encrypt": "","guid": ""}}',
        'note':'登录接口测试'},
      {
        'flag':'login',
        'api':'platform/Login/GetLogin?',
        'header':'{"Content-Type":"application/json","appCode":"CRM"}',
        'body':'{"username": "hsy1","userpswd": "","islogin": true}',
        'expected_response':'{"errcode": 102,"isSucceed": false,"errmsg": "Error:对不起，该用户不存在！","json": "对不起，该用户不存在！"}',
        'note':'登录接口测试-反例'},
      {
        'flag':'get_token',
        'api':'oauth2/token',
        'header':'{"Content-Type":"application/json","appCode":"CRM"}',
        'body':'{"sessionKey": "s_key","appCode": "CRM","clientId": "","localLanguage": "zh-CN"}',
        'expected_response':'{"errcode": 0,"isSucceed": true,"errmsg": "OK","json": ""}',
        'note':'获取token'}
,
      {
        'flag':'select_all_service',
        'api':'MicroManagement/SelectMicroServices',
        'header':'{"Content-Type":"application/json","Authorization":"token"}',
        'body':'{"queryStr": "1=1","footer": "","pager": {"page": 1,"rows": 20,"sort": "apiUrl","order": "asc"},"isData": false}',
        'expected_response':'{ "errcode": 0, "isSucceed": true, "errmsg": "OK", "json": {} } }',
        'note':'查询所有服务测试'}
  ]
}
 
# Inster table datas
def init_data():
  DB().init_data(datas)
 

if __name__ == '__main__':
  init_data()