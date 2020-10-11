from flask import Flask, request
from flask import render_template as rt
from Lesson17 import parser as p
from Lesson17 import parser_2 as p2
import Lesson17.db as db

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def get_vacancies():
    return rt('index.html')


@app.route('/show-data', methods=['POST'])
def result():
    choose = request.form['parse']
    if choose == 0:
        p.run()
        return rt(data=db.show())


@app.route('/contacts')
def show_contacts():
    return rt('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
