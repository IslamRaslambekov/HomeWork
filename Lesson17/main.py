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
    choose = int(request.form['parse'])
    if choose == 0:
        p.run()
        data = db.show()
        return rt('show-data.html', data=data)

    elif choose == 1:
        p2.run()
        data = db.show()
        return rt('show-data.html', data=data)

    elif choose == 2:
        db.drop()
        data = db.show()
        return rt('show-data.html', data=data)




@app.route('/contacts')
def show_contacts():
    return rt('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
