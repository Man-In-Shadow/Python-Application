from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
 return "helloworld",200,{"Content-Type":"application/json"}
#直接响应
#1.直接返回响应体数据： return '字符串'
  # return "helloworld"
#2.直接返回响应体数据+状态码 return '字符串'，状态码
#   return "helloworld",666
#   return "helloworld","666 BigError" #自定义状态码含义
#3.直接返回响应体数据+状态码++响应头信息 return '字符串',状态码,响应头信息
# return "helloworld",200,{"Content-Type":"application/json"}





if __name__ == '__main__':
    app.run(debug=True)