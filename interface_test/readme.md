#搭建准备<br>
##1、安装mysql，<br>
##2、创建myusecase表，用来保存测试用例<br>
##3、安装python3<br>
##4、python3安装好后，终端执行 pip install -r requirements.txt 命令，用来加载所需要的模块<br><br>

#自动化接口测试环境搭建参考<br>
##https://blog.csdn.net/alvin_lam/article/details/79669555 <br><br>

##https://blog.csdn.net/songlh1234/article/details/84317617<br><br>

#批量执行多个测试用例参考<br>
##https://blog.csdn.net/xm_csdn/article/details/77158979 <br><br>


#主要代码目录<br>
>---db_fixture **存放mysql数据库操作文件**<br>  
>>--mysql_db.py<br>  
>>--test_data.py<br>  

>---interface **存放单元测试文件**<br>  
>>--batch_dialog_manager_test.py<br>  
  --batch_myrobot_test.py<br>  
  --dialog_manager_test.py<br>  

>---log **存放日志文件**<br>  
>>--logs<br>  

>---report **存放测试报告**<br>  
>---utils **工具包**<br>  
>>--configEmail.py<br>  
>>--configHttp.py<br>  
>>--log.py<br>  
>>--readConfig.py<br> 
 
>---caselist.txt **测试集**<br>  
>---config.ini **配置文件**<br>  
>---HTMLTestRunner.py **测试报告模板**<br>  
>---run_AllTest.py **执行自动化测试**<br>  

#配置文件config.ini说明<br>
[EMAIL]
serveraddrs = smtp.qq.com 这个是qq邮箱的smtp地址，使用其它邮箱的可以百度查一下对应的smtp地址
