from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
@login_required
def index():

    user = {'nickname': 'Dennis'}
    posts = [
        {
            'author': {'nickname': 'Roman Reigns'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'John Cena'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@app.before_request
def before_request():
  g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
@iod.loginhandler
def login():
  if g.user is not None and g.user.is_authenticated:
    return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
      session['remember_me'] = form.remember_me.data
      return iod.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))