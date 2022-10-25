from flask import Flask, render_template
from pm25 import get_pm25
app = Flask(__name__)

# 首頁


@app.route('/')
@app.route('/<name>')
def index(name='GUEST'):
    date = get_date()

    return render_template('./index.html', name=name, date=date)


@app.route('/date')
def get_date():
    from datetime import datetime
    date = datetime.now()

    return date.strftime('%Y-%m-%d %H:%M:%S')

# <type:id>


@app.route('/book/<int:id>')
def get_book(id):
    try:
        books = {1: "Python", 2: "HTML", 3: "CSS"}

        return books[id]
    except Exception as e:
        print(e)
        return '書籍編號錯誤!'

# http://127.0.0.1:5000/sum/x=10&y=20


@app.route('/sum/x=<a>&y=<b>')
def get_sum(a, b):
    total = eval(a)+eval(b)
    return f'{a}+{b}={total}'

# url: bmi/
# function : get_bmi(height,weight)
# return 'BMI:25.5'


@app.route('/bmi/name=<name>&height=<height>&weight=<weight>')
def get_bmi(name, height, weight):
    try:
        bmi = eval(weight)/(eval(height)/100)**2

        return '%s BMI:%2.f' % (name, bmi)
    except:
        return '參數輸入錯誤!'


@app.route('/stock')
def get_stock():

    stocks = [
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]

    return render_template('./stock.html', date=get_date(), stocks=stocks)


@app.route('/pm25')
def pm25():
    columns, values = get_pm25()

    print(columns, values)


# pm25()
if __name__ == '__main__':
    pm25()
    app.run(debug=True)
