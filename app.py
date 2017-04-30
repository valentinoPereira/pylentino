from flask import Flask, render_template
from article_data import Articles

# Articles = Articles()

app = Flask(__name__)

@app.route('/')
def tinohome():
	return render_template('home.html')

@app.route('/about')
def aboutme():
	return render_template('about.html')

@app.route('/articles')
def articlesfunction():
	return render_template('articles.html', articles= Articles())

@app.route('/article/<string:id>')
def article(id):
	return render_template('article.html', id=id)

if __name__ == '__main__':
	app.run(host= '0.0.0.0', debug=True)