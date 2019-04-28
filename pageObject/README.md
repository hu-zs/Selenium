# selenium自动化框架的封装
## PO模式介绍
###  PO模式====pageObject
#### Page Object模式是使用Selenium的广大同行最为公认的一种设计模式。在设计测试时，把元素和方法按照页面抽象出来，分离成一定的对象，然后再进行组织。
####  创建一个对象来对应页面的一个应用。故我们可以为每个页面定义一个类，并为每个页面的属性和操作构建模型。体现在对界面交互细节的封装，测试在更上层使用页面对象，在底层的属性或者操作的更改不会中断测试。减少代码重复，提高测试代码的可读性和可维护性。　　
#### Web自动化测试框架（WebTestFramework）是基于Selenium框架且采用PageObject设计模式进行二次开发形成的框架。
#### web测试时,建议强烈推荐使用_谷歌或_火狐浏览器。
#### PageObject设计模式：是将某个页面的所有"元素（包含控件）属性"及"元素操作"封装在1个类(Class)里面~~~~
#### 目的: 测试代码与被测页面对象代码分离，后期如果有页面元素发生了更改,只需要修改相应页面对象的代码(即对应Class文件),而不需要修改测试代码
#### 尽量采用xpath方式来寻找页面元素,而不建议使用name,Link等方法; xpath是基于页面元素所处区域,一般不会发生变化,测试代码基本不受干扰.
#### 将页面元素属性信息与代码分离，即与被测对象代码分离，目的也是为了进一步降低后续因页面变化带来的维护成本
#### ------------------我是分割线-----------------


### 框架目录介绍
####	1.config配置目录的使用
		* log.config 配置日志输出格式的文件
		* 创建logs目录用来存放生成的日志
			日志是给写代码的人员看,观察代码执行的情况
			测试报告-->运行结果
####	2.common目录创建
		* selenium_driver来获取公用的驱动driver
			配置日志,并获取到输出日志的对象logger
			获取浏览器驱动
####	3.pageObject的抽取-->基准的视图
		* 初始化__init__()的操作,主要是获取驱动driver
		* 使用可变参数封装查找单个或者多个元素find_element()的函数
		* getTime()获取格式化的时间
		* getScreenShot()获取截图的操作
		* get_csv_data()读取csv文件的数据
	
	---------------------------------------------------

####	4.业务视图businessPage的编写
     * loginPage
			(By.xxx,'')找控件
			登录的操作
			判断是否成功的状态
####	5.data-->apiUrl.py
		* 记录用到的所有路径
####	6.创建了一个测试用例的基类MyUnit
		setup tearDown
####	7.测试用例类
		testXxx()

####	8.run.py进行运行

pageObject
├── businessPage   --- 业务视图
│   └── loginPage.py   ---登录
├── common         --- 公用的目录
│   ├── myunit.py   --- unittest 初始化和结束
│   └── selenium_driver.py --- 配置日志模块和获取驱动
├── config       -- 配置目录
│   └── log.conf   --- 配置设置
├── data          --- 数据目录
│   ├── apiUrl.py   ---- URL路径
│   └── user.csv    ---- 用户名和密码文件
├── logs           --- 日志目录
├── pageObject     --- 基准的视图目录
│   └── pageObject.py  --基准的视图
├── reports        --- 存放结果的HTML目录
├── run_test_case  --- 运行目录
│   ├── HTMLTestRunner.py  --- 生成HTML方法
│   └── run_case.py     --- 运行目录
├── screenshots    --- 生成的截图
├── test_case      --- 测试用例目录
    └── testLoginPage.py   --- 测试方法
