from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm, SignInForm, ContactUsForm, CarInfoForm


@app.route('/')
def index():
    cdn ={
        'cars':('Hondas', 'Toyotas'),
        'models': ['Prelude', 'Accord', "Camry", 'Prius']
    }
    return render_template('index.jinja', cdn=cdn, title ='Home' )



@app.route('/about')
def about():
    return render_template('about.jinja', title = 'About')

@app.route('/howdoesitwork')
def howdoesitwork():
    return render_template('howdoesitwork.jinja', title = 'How does it work?')

@app.route('/carinfo', methods=['GET', 'POST'])
def carinfo():
    form = CarInfoForm()
    if form.validate_on_submit():
        flash(f"Thank you! Successfully submitted! We'll get back to you soon!")
        return redirect('/')
    return render_template('carinfo.jinja', carinfoform=form, title = 'CarInfo')

@app.route('/contactus')
def contactus():
    form = ContactUsForm()
    if form.validate_on_submit():
        flash(f"Thank you! Successfully submitted! We'll get back to you soon!")
        return redirect('/')
    return render_template('contactus.jinja', contactusform=form, title = 'Contact Us')

@app.route('/signin', methods= ['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        flash(f'{form.username} successfully signed in!')
        return redirect('/')
    return render_template('signin.jinja', sign_in_form=form, title = 'Sign in')

@app.route('/signup', methods= ['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Request to register {form.username} successful')
        return redirect('/')
    return render_template('signup.jinja', sign_up_form= form, title = 'Sign Up Today')


# @app.route('/signup', methods= ['GET', 'POST'])
# def signup():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         flash(f'Request to register {form.username} successful')
#         return redirect('/')
#     return render_template('signup.jinja', form=form, title = 'Signup')


# @app.route('/signin', methods= ['GET', 'POST'])
# def signin():
#     form = SigninForm()
#     if form.validate_on_submit():
#         flash(f'{form.username} successfully signed in!')
#         return redirect('/')
#     return render_template('signin.jinja', sign_in_form=form, title = 'Signin')
