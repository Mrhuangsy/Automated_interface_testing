#框架介绍<br>
本框架采用的是python的unittest+HTMLTestRunner模块搭建成的接口自动化测试环境。
集成了测试用例数据库维护和本地json文件维护两种方法，支持同时生成html和word两种测试报告
#搭建准备<br>
##1、安装mysql，如果选择json文件维护测试用例，则1、2步骤可忽略<br>
##2、创建myusecase表，用来保存测试用例<br>
##3、安装python3<br>
##4、python3安装好后，终端执行 pip install -r requirements.txt 命令，用来加载所需要的模块<br><br>

#自动化接口测试环境搭建参考<br>
##https://blog.csdn.net/alvin_lam/article/details/79669555 <br><br>

##https://blog.csdn.net/songlh1234/article/details/84317617<br><br>

#批量执行多个测试用例参考<br>
##https://blog.csdn.net/xm_csdn/article/details/77158979 <br><br>


#主要代码目录<br>
>---datas **存放测试用例数据文件**<br>
>---db_fixture **存放mysql数据库操作文件**<br>  
>>--mysql_db.py **数据库常用操作方法**<br>
>>--test_data.py **这里维护测试用例至数据库**<br>

>---interface **存放单元测试文件，根据实际场景自定义测试流程**<br>  
>>--batch_cloud_test.py<br>  
  --batch_java_test.py<br>  
  --login_test.py<br> 
  ...... 

>---log **存放日志文件**<br>  
>>--logs<br>  

>---report **存放测试报告**<br>  
>---utils **工具包**<br>  
>>--configEmail.py **发送邮件**<br>  
>>--configHttp.py **封装接口请求方法**<br>  
>>--log.py **日志记录方法**<br>  
>>--otherUtils.py **定义获取token、读取数据文件、写入word报告等方法**<br>  
>>--readConfig.py **读取配置文件**<br> 
 
>---caselist.txt **测试集，解除注释即可执行相应测试文件**<br>  
>---config.ini **配置文件,设置数据库连接参数、邮件发送参数等**<br>  
>---HTMLTestRunner.py **测试报告模板**<br>  
>---run_AllTest.py **执行自动化测试**<br>  

#配置文件config.ini说明<br>
[EMAIL]
serveraddrs = smtp.qq.com 这个是qq邮箱的smtp地址，使用其它邮箱的可以百度查一下对应的smtp地址
