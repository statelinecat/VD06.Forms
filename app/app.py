from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        return render_template('index.html', name=name, city=city, hobby=hobby, age=age)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)