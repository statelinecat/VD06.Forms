from flask import render_template, redirect, url_for, request
from app import app

profiles = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        if name and city and hobby and age:
            age = int(age)
            if age > 0:
                profiles.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
                return redirect(url_for('index'))
    return render_template('index.html', profiles=profiles)
