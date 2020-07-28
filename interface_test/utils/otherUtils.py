# -*- coding:utf-8 -*-
'''
filename : otherUtils.py
create by :
create time : 2020/07/20
introduce : 未分类自定义方法
'''
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture.mysql_db import DB
from utils.readConfig import readConfig
from utils.configHttp import runmain
import json,time
from collections import OrderedDict
from mailmerge import MailMerge



class otherUtils():

    #登录获取token-请求参数从数据库中取得
    def getToken(self):
        usecase = DB().select("cloud_test_case", {'flag': ('login', 'get_token')})
        session_key = ''
        token = ''
        # login:
        for _row in usecase:
            print('_row:', _row)
            if _row['flag'] == 'login':
                _heards = json.loads(_row['header'])
                _data = json.dumps(json.loads(_row['body'])).encode('utf-8')
                print( 'heards:', type(_heards), 'data:', type(_data))
                login_result = runmain.run_main("post", readConfig.get_http('cloudurl') + _row['api'], _heards, _data)
                if json.loads(login_result)['errmsg'] == 'OK':
                    session_key = json.loads(login_result)['json']['guid']
                    break
        # get token
        for __row in usecase:
            if __row['flag'] == 'get_token':
                __heards = json.loads(__row['header'])
                __data = json.dumps(json.loads(__row['body'].replace('s_key', session_key))).encode('utf-8')
                getToken_result = runmain.run_main("post", readConfig.get_http('cloudurl') + __row['api'], __heards,
                                                   __data)
                if json.loads(getToken_result)['errmsg'] == 'OK':
                    token = json.loads(getToken_result)['json']
                    break
        return token

    #读取json文件
    def read_json_file(self,fn):
        with open(fn,'r',encoding='utf-8') as f:
            json_file = json.load(f,object_pairs_hook=OrderedDict)
        return json_file

    #登录获取token - 请求参数从json文件中取得
    def getToken2(self):
        usecase = self.read_json_file('../datas/usecase.json')
        javaurl = readConfig.get_http('javaurl')
        session_key = ''
        token = ''
        for key,value in usecase.items():
            if key == 'login':
                for param in value:
                    api = param.get('api','')
                    heards = param.get('header',{})
                    data = json.dumps(param.get('body',{})).encode('utf-8')
                    login_result = runmain.run_main("post", javaurl + api, heards,
                                                    data)
                    if json.loads(login_result)['code'] == 0 and json.loads(login_result)['message']=='登录成功':
                        session_key = json.loads(login_result)['data']['sessionKey']
                        break
            if key == 'getToken' and session_key != '':
                for _param in value:
                    _api = _param.get('api','')
                    _heards = _param.get('header',{})
                    _body = _param.get('body', {})
                    if _body: _body['token']['sessionKey'] = session_key
                    _data = json.dumps(_body).encode('utf-8')
                    getToken_result = runmain.run_main("post", javaurl + _api, _heards,
                                                    _data)
                    if json.loads(getToken_result)['code'] == 0 and json.loads(getToken_result)['message'] == '验证成功':
                        token = json.loads(getToken_result)['data']
                        break
            if token != '':break

        return token

    def writeIntoModel(self,test_result):
        '''
        使用MailMerge模块，可以在docx文件里设置邮件合并的域属性，然后根据域属性填入相应的值即可
        :param test_result:
        :return:
        '''
        datetimetemplate = "../report/testModel.docx"
        document = MailMerge(datetimetemplate)
        number = 0
        result=''
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        test_result_date = []

        for suit_result in test_result:
            number += 1
            if suit_result[0] == 0:
                result = '通过'
            elif suit_result[0] == 1:
                result = '失败'
            elif suit_result[0] == 2:
                result = '执行错误'
            des_list = suit_result[2].split('\n')
            suit_result_dict = {"Single_NO":str(number),
                                "Single_Description":des_list[0],
                                "Single_api":des_list[1],
                                "Single_Result":result,
                                "Single_Note":""}
            test_result_date.append(suit_result_dict)

        document.merge_rows("Single_NO",test_result_date)
        document.write("../report/"+now+"_output.docx")


otherutils = otherUtils()
if __name__ == '__main__':  # 测试一下
    # token = otherutils.getToken2()
    # print(token)
    datetimetemplate = "../report/testModel.docx"
    document = MailMerge(datetimetemplate)
    print(document.get_merge_fields())
    document.merge(From='hsy199523@163.com',Title="自动化测试报告")
    document.write("../report/output.docx")