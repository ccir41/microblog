from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Shishir'}
	#return render_template('index.html')
	posts = [
		{
			'author' : {'username':'XYZ'},
			'body' : 'It is so cold at Dang'
		},
		{
			'author' : {'username':'ABC'},
			'body' : 'It is so hot at Butwal'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, rembember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)
