from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname' : 'Arsalan'}
	posts = [
	{ 
		'author':{'nickname': 'John'},
		'body': 'Amazing day designing the iPhone 5C at Apple HQ'
	},
	{
		'author': {'nickname': 'Susan'},
		'body': 'The Avengers movie was so cool! Shawarma...mmmm!'
	}]
	return render_template("default.html",
		title = 'Home',
		user = user,
		posts = posts)

@app.route('/login', methods = ['GET', 'POSTS'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',
		title = 'Sign In',
		form = form,
		providers = app.config['OPENID_PROVIDERS'])
