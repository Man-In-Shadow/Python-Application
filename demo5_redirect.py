

from flask import Flask,redirect,url_for

app=Flask(__name__)



#重定向
#格式 return redirect("address")address可本地，可互联
#重定向的代号是302
#重定向是两次请求
#页面跳转到pornhub
#return redirect("http://www.pronhub.com")
@app.route('/')
def hello_world():
    return "haha"


#反解析
#格式：url_for('视图函数名'，key=value)顺带传个参数
@app.route('/adaaaffasaf')
def fuc1():
    return "hello,1"

@app.route('/test')
def fuc2():
    des=url_for('fuc1')
    return redirect(des)

if __name__ == '__main__':
    app.run(debug=True)