from flask import Flask, request
from flask import render_template as rt
from Lesson17 import parser as p
from Lesson17 import parser_2 as p2


# import Lesson17.db as db

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


@app.route('/pro-task')
def pro_form():
    return rt('pro-task.html')


@app.route('/show-pro-task', methods=['POST'])
def show():
    surname = request.form['surname']
    name = request.form['name']
    middle_name = request.form['middle-name']
    number = request.form['tel']
    email = request.form['email']
    password = request.form['password']

    db.pro_task_table(surname, name, middle_name, number, email, password)

    data = db.pro_task_show()
    return rt('show-pro-task.html', data=data)


@app.route('/contacts')
def show_contacts():
    return rt('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)