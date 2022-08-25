from app import app, db
from routes.routes import *
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from flask import flash, redirect, request, url_for, render_template


@app.route('/authorization', methods=['POST', 'GET'])
def authorization():
    email_user = request.form.get('email_user')
    password = request.form.get('password')
    if current_user.is_authenticated:
        return redirect("/all-posts")

    if email_user and password:
        users = Users.query.filter_by(email_user=email_user).first()
        if users and check_password_hash(users.password, password):
            login_user(users)
            flash('Вітаємо!', category='success')
            return redirect('/all-posts')
        else:
            flash('Помилка,ви ввели не вірні дані!', category='error')
            return redirect(url_for('authorization'))

    else:
        return render_template('authorization.html')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    flash('Ви вийшли з аккаунту.')
    logout_user()
    return redirect(url_for('head_page_info'))


@app.after_request
def redirect_login_page(response):
    if response.status_code == 401:
        flash('Спочатку авторизуйтесь', category='error')
        return redirect(url_for('authorization') + '?next' + request.url)
    return response
