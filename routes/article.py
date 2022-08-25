from app import app, db
from flask import render_template, request, redirect, flash, url_for
from models.models import *
from flask_login import current_user, login_required


@app.route('/user-article/add-post', methods=['POST', 'GET'])
@login_required
def add_new_post():
    name_article = request.form.get('name_article')
    text_article = request.form.get('text_article')
    category = request.form.get('category')

    if request.method == 'POST':
        if not (name_article or text_article):
            flash("Ви не ввели обов'язкове поле!", category='error')
            return redirect(url_for('add_new_post'))
        else:
            articles = Article(name_article=name_article, text_article=text_article, category=category,
                               author=current_user.id)

            db.session.add(articles)
            db.session.commit()
            db.session.flush()
            flash('Стаття успішно добавилась!')
            return redirect(url_for('all_post'))
    else:
        return render_template('add-post.html', users=current_user)


@app.route('/update-post/<int:id>/update', methods=['POST', 'GET'])
def update_post_by_id(id):
    update_article = Article.query.get(id)
    if request.method == 'POST':
        update_article.name_article = request.form.get('name_article')
        update_article.text_article = request.form.get('text_article')
        try:
            flash('Нові дані було внесено!', category='success')
            db.session.add(update_article)
            db.session.commit()
            return redirect(url_for('user_article'))
        except:
            flash('Сталась невідома помилка!', category='error')
            return redirect(url_for('user_article'))
    else:
        return render_template('update-post.html', update_article=update_article)


@app.route('/delete-post/<int:id>/delete', methods=['POST', 'GET'])
@login_required
def delete_post_by_id(id):
    post = Article.query.filter_by(id=id).first()

    if not post:
        flash('Пост не знайдено', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Стаття була успішно видалена!')
        return redirect(url_for('user_article'))

    return redirect(url_for('user_article'))



