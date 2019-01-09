from app import app
from flask import render_template

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