# 框架介绍<br>
本框架采用的是python的unittest+HTMLTestRunner模块搭建成的接口自动化测试环境。
集成了测试用例数据库维护和本地json文件维护两种方法，支持同时生成html和word两种测试报告
# 搭建准备<br>
## 1、安装mysql，如果选择json文件维护测试用例，则1、2步骤可忽略<br>
## 2、创建myusecase表，用来保存测试用例<br>
## 3、安装python3<br>
## 4、python3安装好后，终端执行 pip install -r requirements.txt 命令，用来加载所需要的模块<br><br>

### pip国内镜像源 https://pypi.tuna.tsinghua.edu.cn/simple/ 例：
 `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ Django `

### 可以一键执行requirements.txt：
 ` pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt`

# 自动化接口测试环境搭建参考<br>
  https://blog.csdn.net/alvin_lam/article/details/79669555 <br><br>

   https://blog.csdn.net/songlh1234/article/details/84317617<br><br>

# 批量执行多个测试用例参考<br>
 https://blog.csdn.net/xm_csdn/article/details/77158979 <br><br>

# selenium web自动化测试框架搭建参考<br>
https://blog.csdn.net/a836586387/article/details/88899936?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param<br><br>
https://blog.csdn.net/sinat_34817187/article/details/82018099?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.channel_param<br><br>

# 主要代码目录<br>
>---datas **存放测试用例数据文件**<br>
>---db_fixture **存放mysql数据库操作文件**<br>  
>>--mysql_db.py **数据库常用操作方法**<br>
>>--test_data.py **这里维护测试用例至数据库**<br>

>---framework **存放selenium操作浏览器常用封装方法**<br>
>>--basepage.py **网页基本操作类，包括各类元素标签的操作方法**<br>
>>--browser_engine.py **浏览器基本操作类，包括打开/关闭浏览器、前进后退等**<br>

>---framwork_pages **根据页面对象模型（PO）方法，存放所有UI Page类**<br>

>---framwork_test_case **根据页面对象模型（PO）方法，存放所有UI 测试用例**<br>

>---interface **存放单元测试文件，根据实际场景自定义测试流程**<br>  
>>--batch_cloud_test.py<br>  
  --batch_java_test.py<br>  
  --login_test.py<br> 
  ...... 

>---log **存放日志文件**<br>  
>>--logs<br>  

>---report **分日期存放测试报告**<br>  
>---utils **工具包**<br>  
>>--configEmail.py **发送邮件**<br>  
>>--configHttp.py **封装接口请求方法**<br>  
>>--globalvar.py **项目全局变量存取（get/set）方法**<br> 
>>--log.py **日志记录方法**<br>  
>>--otherUtils.py **定义获取token、读取数据文件、写入word报告等方法**<br>  
>>--readConfig.py **读取配置文件**<br> 
>>--unittest_custom.py **unittest定制类，如重写断言失败的相关方法，实现自动截图功能**<br>
 
>---caselist_ui.txt **UI测试集，解除注释即可执行相应测试文件**<br>  
>---caselist.txt **接口测试集，解除注释即可执行相应测试文件**<br>  
>---config.ini **配置文件,设置数据库连接参数、邮件发送参数等**<br>  
>---HTMLTestRunner.py **测试报告模板**<br>  
>---HTMLTestRunnerCN.py **UI测试报告模板(汉化版)**<br> 
>---run_AllTest.py **执行接口自动化测试入口**<br>  
>---run_all_uitest.py **执行UI自动化测试入口**<br>  

# 配置文件config.ini说明<br>
[EMAIL]
serveraddrs = smtp.qq.com 这个是qq邮箱的smtp地址，使用其它邮箱的可以百度查一下对应的smtp地址

# selenium隐式等待常用方法
```
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

base_url = "http://www.baidu.com"
driver = webdriver.Firefox()
driver.implicitly_wait(5)
'''隐式等待和显示等待都存在时，超时时间取二者中较大的'''
locator = (By.ID,'kw')
driver.get(base_url)

WebDriverWait(driver,10).until(EC.title_is(u"百度一下，你就知道"))
'''判断title,返回布尔值'''

WebDriverWait(driver,10).until(EC.title_contains(u"百度一下"))
'''判断title，返回布尔值'''

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
'''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'su')))
'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''

WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element(by=By.ID,value='kw')))
'''判断元素是否可见，如果可见就返回这个元素'''

WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.mnav')))
'''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''

WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'.mnav')))
'''判断是否至少有一个元素在页面中可见，如果定位到就返回列表'''

WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='u1']/a[8]"),u'设置'))
'''判断指定的元素中是否包含了预期的字符串，返回布尔值'''

WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'#su'),u'百度一下'))
'''判断指定元素的属性值中是否包含了预期的字符串，返回布尔值'''

#WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
'''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
#注意这里并没有一个frame可以切换进去

WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#swfEveryCookieWrap')))
'''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''
#注意#swfEveryCookieWrap在此页面中是一个隐藏的元素

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='u1']/a[8]"))).click()
'''判断某个元素中是否可见并且是enable的，代表可点击'''
driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]").click()
#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wrapper']/div[6]/a[1]"))).click()

#WebDriverWait(driver,10).until(EC.staleness_of(driver.find_element(By.ID,'su')))
'''等待某个元素从dom树中移除'''
#这里没有找到合适的例子

WebDriverWait(driver,10).until(EC.element_to_be_selected(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]")))
'''判断某个元素是否被选中了,一般用在下拉列表'''

WebDriverWait(driver,10).until(EC.element_selection_state_to_be(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]"),True))
'''判断某个元素的选中状态是否符合预期'''

WebDriverWait(driver,10).until(EC.element_located_selection_state_to_be((By.XPATH,"//*[@id='nr']/option[1]"),True))
'''判断某个元素的选中状态是否符合预期'''
driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()

instance = WebDriverWait(driver,10).until(EC.alert_is_present())
'''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
print instance.text
instance.accept()

driver.close()
```

# Selenium无法定位元素的九种解决方案
https://www.jianshu.com/p/83087c24ab19

# Python编码规范建议
https://www.cnblogs.com/liangmingshen/p/9273413.html
```

总体原则，新编代码必须按下面命名风格进行，现有库的编码尽量保持风格。
1 尽量单独使用小写字母‘l’，大写字母‘O’等容易混淆的字母。
2 模块命名尽量短小，使用全部小写的方式，可以使用下划线。
3 包命名尽量短小，使用全部小写的方式，不可以使用下划线。
4 类的命名使用CapWords的方式，模块内部使用的类采用_CapWords的方式。
5 异常命名使用CapWords+Error后缀的方式。
6 全局变量尽量只在模块内有效，类似C语言中的static。实现方法有两种，一是__all__机制;二是前缀一个下划线。
7 函数命名使用全部小写的方式，可以使用下划线。
8 常量命名使用全部大写的方式，可以使用下划线。
9 类的属性（方法和变量）命名使用全部小写的方式，可以使用下划线。
9 类的属性有3种作用域public、non-public和subclass API，可以理解成C++中的public、private、protected，non-public属性前，前缀一条下划线。
11 类的属性若与关键字名字冲突，后缀一下划线，尽量不要使用缩略等其他方式。
12 为避免与子类属性命名冲突，在类的一些属性前，前缀两条下划线。比如：类Foo中声明__a,访问时，只能通过Foo._Foo__a，避免歧义。如果子类也叫Foo，那就无能为力了。
13 类的方法第一个参数必须是self，而静态方法第一个参数必须是cls。

```