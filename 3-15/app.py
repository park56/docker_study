from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>index<h1>"

# 일반적인 라우트 방식입니다.
@app.route('/board')
def board():
    return "그냥 보드"

# URL 에 매개변수를 받아 진행하는 방식입니다.
@app.route('/board/<article_idx>')
def board_view(article_idx):
    return article_idx

# 위에 있는것이 Endpoint 역활을 해줍니다.
@app.route('/boards',defaults={'page':'index'})
@app.route('/boards/<page>')
def boards(page):
    return page+"페이지입니다."

app.run(host="0.0.0.0",port=8080, debug=True)