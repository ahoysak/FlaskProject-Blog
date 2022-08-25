from app import app, db
from routes.login import *
from models.models import Users
from werkzeug.security import generate_password_hash
from flask import render_template, request, redirect, flash, url_for


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    user_name = request.form.get('user_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')
    password_check = request.form.get('password_check')
    email_user = request.form.get('email_user')

    if request.method == 'POST':
        if password != password_check:
            flash('Паролі не сходяться', category='error')
            return redirect(url_for('registration'))
        if not (user_name or last_name or password or email_user):
            flash("Ви не ввели одне з обов'язкових полів!")
            return redirect('/')
        else:
            hashing_password = generate_password_hash(password)
            users = Users(user_name=user_name, last_name=last_name, password=hashing_password, email_user=email_user)

            db.session.add(users)
            db.session.flush()
            db.session.commit()
            flash('Реєстрація пройшла успішно!', category='success')

            return redirect(url_for('authorization'))

    else:
        return render_template('registration.html')

