##从flsk模块导入了Flask类
from flask import Flask
from werkzeug.routing import BaseConverter
##创建flask对象
##参数1：__name__，如果从当前文件启动，那么值是__main__,
# 如果是其他模块调用运行的，那么值是模块的名字
#参数2：static_url_path,表示静态资源的访问地址,默认为none，现为/static（根据变量3得出）
#参数3：static_folder,用来存储静态资源的，默认的名字是static
#参数4：template_folder,模板文件夹，默认值是templates
app=Flask(__name__)



#使用app，通过路由绑定一个视图函数

#在访问路由的时候指定参数,要将该参数作为视图函数的参数
#不注明参数类型的，默认为path（字符串）
#自定义参数类型（自定义转换器）
#如果系统提供的的int，float等满足不了需求的时候，我们需要自定义
#自定义转换器的格式：
#1.定义类，继承自BaseConverter
#2. 重写__init__ 方法
#3.初始化父类成员变量
class MyRegexConverter(BaseConverter):
    def __init__(self,map,regex):
        super(MyRegexConverter,self).__init__(map)
        self.regex=regex







#4.将转换器类添加到系统默认的转换器列表中
app.url_map.converters["mine"]=MyRegexConverter
@app.route('/')
#注意：视图函数一定要有返回值
def hello_world():
    return 'hello world flask'


#接受三位整数
@app.route('/<mine("\d{3}"):num>')
def get_three(num):
    return "the 3 number is %s"%num
#接受手机号
@app.route('/<mine("1[3-9]\d{9}"):num>')
def get_phone(num):
    return "the phone number is %s" % num

#使用'/<mine('规则'):obj>'其实传递了两个参数 参数1：url_map（自动映射）,参数2：括号中写的规则




#判断是否直接使用当前模块运行程序
if __name__ == '__main__':


    #查看可访问的地址
    print(app.url_map)



    #运行app程序
    #参数1：host，如果我们不指定，默认值为127.0.0.1
    #参数2：port，如果我们不指定，默认值为5000
    #参数3：debug，调试模式，如果不指定，默认值是false
        #设置成true有两个好处
          #1.如果在运行过程中，直接改动代码了，不需要重新启动程序只需要ctrl+s即可保存部署程序
          #2.如果程序报错了，会有友情提示


    app.run(debug=True)
