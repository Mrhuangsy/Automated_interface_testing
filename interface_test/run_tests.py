#-*- coding:utf-8 -*-
'''
filename : run_tests.py
create by : 
create time : 2019/07/09
introduce : 执行自动化接口测试，测试入口，一次性会执行所有单元测试文件，不能设置只执行指定单元测试文件。
            其它操作包括：
            1、生成测试报告
            2、发送测试报告邮件通知
'''
import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data
from utils.configEmail import sendemail
from utils.log import logger
 
 
# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
 
if __name__ == "__main__":
      
  start_time = time.time()
  logger.info("自动化测试开始......")
  test_data.init_data() # 初始化接口测试数据

  now = time.strftime("%Y-%m-%d %H_%M_%S")
  fn = now + '_result.html'
  filename = './report/' + fn
  fp = open(filename, 'wb')
  runner = HTMLTestRunner(stream=fp,
              title='Guest Manage System Interface Test Report',
              description='Implementation Example with: ')
  runner.run(discover)
  fp.close()
  end_time = time.time()
  exec_time = (end_time - start_time)* 1000
  logger.info(f"耗时{exec_time}ms")
  logger.info("自动化测试结束......")
  
  #发送邮件
  logger.info("发送邮件......")
  sendemail.send(fn)
  logger.info("发送邮件完成......")
  logger.info("=="*20)