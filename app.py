
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/") # "/" => 루트지정
                # 경로지정
def hello(): #메소드
    return "<h1>서버가 html도 보내주나??</h1>"
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>첫번째 줄!!!</h1>
    <h2>두번째 줄!!!</h2>
    """

@app.route("/html_file")
def html_file():
    return render_template("html_file.html") # 폴더는 반드시 templates 이름으로 생성
                                             # 폴더 안에 html_file.html 생성
                                             
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", people=name)
    
@app.route("/cube/<int:num>")
def cube(num):
    triple = num**3
    return render_template("cube.html", triple=triple, num=num)

    
@app.route('/lunch')
def lunch() :
    menu = ['삼겹살','짜장면','피자','치킨']
    choice = random.choice(menu)
    return render_template("lunch.html",choice=choice)
    
@app.route('/lotto')
def lotto() :
    number = range(1,46)
    pick = random.sample(number,6)
    sort_pick = sorted(pick)
    return render_template("lotto.html",sort_pick = sort_pick)
    #url이름과 html의 이름을 통일 시킬 것
    
@app.route('/naver')
def naver() :
    return render_template("naver.html")