from flask import Flask, request
from flask import render_template as rt
from Lesson16.api import find_vacancies as fv

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def get_vacancies():
    return rt('index.html')


@app.route('/result', methods=['POST'])
def result():
    search = request.form['search']
    if request.form['city']:
        city = str(request.form['city']).capitalize()
        params = {'text': f'{search} AND {city}', 'only_with_salary': True, 'per_page': 100}
    else:
        params = {'text': search, 'only_with_salary': True, 'per_page': 100}

    data = fv(params)

    return rt('result.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
