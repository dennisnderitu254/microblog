from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'nickname':'Dennis'} # Real User
	posts = [ #Fake array of posts
		{
			'author':{'nickname':'John'},
			'body': 'Beautiful day in portland!'
		},
		{
			'author':{'nickname':'Susan'},
			'body':'The Avengers movie was so cool!'
		}


	]

	return render_template("index.html",
		                   title='Home',
		                   user=user,
		                   posts=posts)

