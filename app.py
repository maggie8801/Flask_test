from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/input_customer')
def input_customer():
    return render_template('input_customer.html')

@app.route('/result')
def result():
    if request == "POST":
        member_code = request.values['Name']
    return render_template('result.html', member_code)

if __name__ == '__main__':
    app.run()