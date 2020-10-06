from flask import Flask
from werkzeug.routing import BaseConverter

app=Flask(__name__)
"""

@app.route('/')
def hello_world():
    return 'hello world flask' 
    """
#给路由增加其他访问方式
#格式 @app.route('路径'，methods=['请求方式1'，'请求方式2'.....])
#常见的请求方式：GET，POST，PUT，DELETE
#如果不指定请求方式，那么默认支持的是GET
@app.route('/',methods=["POST"])
def hello_world():
    return "helloworld"



if __name__ == '__main__':
    app.run()