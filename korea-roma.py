import os
import sys
import urllib.request
import json
from flask import Flask,render_template,request as rq
app = Flask(__name__,template_folder='template')

@app.route("/")
def main():
        return render_template("index.html")
@app.route("/korea-roma",methods=['POST'])
def roma():
    name = rq.form['name']
    client_id = "gEZpPdzcj3ZwppjiIev_" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "Xu_L3MD0M3" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(name)
    url = "https://openapi.naver.com/v1/krdict/romanization?query=" + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        json_dict = json.loads(response_body.decode('utf-8'))
        result = json_dict['aResult'][0]
        name_items = result['aItems']
        names = [name_item['name'] for name_item in name_items]
    return render_template("roma.html",names=names)
if __name__ == '__main__':
        app.run(host="192.168.219.100",port="4000",use_reloader=True, debug=True)
