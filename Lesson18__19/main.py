from flask import Flask, request
from flask import render_template as rt
from Lesson18__19 import parser as p
from Lesson18__19 import parser2 as p2
from Lesson18__19 import ORM


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def get_vacancies():
    return rt('index.html')


@app.route('/show-data', methods=['POST'])
def result():
    choose = int(request.form['parse'])
    if choose == 0:
        new_data = p.run()
        for i in new_data:
            ORM.add_data(i['link'], i['model'], i['price'], i['old_price'])
        return rt('show-data.html', data=new_data)

    elif choose == 1:
        new_data = p2.run()
        for i in new_data:
            ORM.add_data(i['link'], i['model'], i['price'], i['old_price'])
        return rt('show-data.html', data=new_data)


@app.route('/contacts')
def show_contacts():
    return rt('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)