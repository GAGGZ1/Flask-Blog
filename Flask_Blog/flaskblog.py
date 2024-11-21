from flask import Flask,render_template,url_for

app = Flask(__name__)

posts=[
    {
        'author':'corey schafer',
        'title':'blog post 1',
        'content':'First post Content',
        'date_posted':'April 20, 2018'
    },
    {
        'author':'Jane Smith',
        'title':'blog post 2',
        'content':'Second post Content',
        'date_posted':'May 15, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
