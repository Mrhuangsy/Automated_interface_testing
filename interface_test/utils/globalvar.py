#-*- coding:utf-8 -*-
'''
filename : globalvar.py
create by : 
create time : 2019/07/09
introduce : 自定义方法，项目全局变量管理get/set
'''

def __init__():
    global _global_dict
    _global_dict = {}

def set_value(name,value):
    _global_dict[name] = value

def get_value(name,defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue

def del_value(name):
    _global_dict.pop(name)