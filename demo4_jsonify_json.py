

from flask import Flask

app=Flask(__name__)




from flask import jsonify
@app.route('/')
#通过jsonify返回json数据
#格式jsonify(dict)
#简化格式jsonify(key1=value1，key2=value2，....)

def jsonify_json():
    return jsonify(value="helloworld")

if __name__ == '__main__':
    app.run()