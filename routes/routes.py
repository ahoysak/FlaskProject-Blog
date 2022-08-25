from app import app, db
from flask import render_template, flash, request, redirect, url_for
from models.models import *
from flask_login import current_user, login_required


@app.route('/')
def head_page_info():
    all_posts = Article.query.order_by(Article.like_count.desc())
    page = request.args.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    pages = all_posts.paginate(page=page, per_page=5)
    return render_template('head-page.html', all_posts=all_posts, pages=pages)


@app.route('/all-posts', methods=['GET'])
@login_required
def all_post():
    all_posts = Article.query.order_by(Article.like_count.desc())
    page = request.args.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    pages = all_posts.paginate(page=page, per_page=5)
    return render_template('all-posts.html', all_posts=all_posts, pages=pages)


@app.route('/user-article', methods=['GET'])
@login_required
def user_article():
    author = current_user.get_id()
    article = Article.query.filter(Article.author == author)
    all_posts = article.all()
    return render_template('user-article.html', all_posts=all_posts)


@app.route('/create-comment/<int:post_id>/user', methods=['POST'])
@login_required
def create_comment(post_id):
    text_comment = request.form.get('text_comment')

    if not text_comment:
        flash('Помилка!', category='error')
    else:
        article = Article.query.get(post_id)
        if article:
            comment = Comment(text_comment=text_comment, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            flash('Коментар успішно добавлено!', category='success')
            db.session.commit()
        else:
            flash('Помилка,стаття не існує', category='error')

    return redirect(url_for('all_post'))


@app.route('/delete-comment/<int:comment_id>')
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Немає коментаря', category='error')
        return redirect(url_for('all_post'))
    else:
        db.session.delete(comment)
        db.session.commit()
        flash('Коментар успішно видалено!', category='success')

    return redirect(url_for('user_article'))


@app.route('/like-article/<int:post_id>', methods=['GET'])
@login_required
def like_article(post_id):
    post = Article.query.get(post_id)
    like = Like.query.filter_by(author=current_user.id, post_id=post_id).first()

    if not post:
        flash('Не можливо поставити лайк.', category='error')
    elif like:
        db.session.delete(like)
        post.like_count = post.like_count - 1
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        post.like_count = post.like_count + 1
        db.session.commit()

    return redirect('/all-posts')



