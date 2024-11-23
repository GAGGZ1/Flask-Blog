from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='cc1954a0b2fa7878e90d95eb1bfbcae8'

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

@app.route("/register", methods=["POST",'get'])
def register():
    form =RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login" , methods=["POST",'get'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password','danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True, port=5001)
