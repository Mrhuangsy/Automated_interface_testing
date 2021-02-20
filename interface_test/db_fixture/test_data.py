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
import uuid
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
        'flag':'select_all_service',
        'api':'MicroManagement/SelectMicroServices',
        'header':'',
        'body':'',
        'expected_response':'',
        'note':'查询所有服务测试'}
  ]
}
 
# Inster table datas
def init_data():
  DB().init_data(datas)
 

if __name__ == '__main__':
  init_data()