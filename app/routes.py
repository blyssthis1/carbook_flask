from flask import render_template, flash, redirect
from app import app, db
from app.forms import RegisterForm, SignInForm, ContactUsForm, CarInfoForm
from app.models import User, Car
from flask_login import current_user, login_user, logout_user, login_required



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
        make = form.make.data
        model = form.model.data
        year = form.year.data
        price= form.price.data
        color = form.color.data
        c= Car(make=make, model=model, year=year, price=price, color=color, user_id=current_user.id)
        c.commit()
        flash(f"Thank you! Successfully submitted! We'll get back to you soon!")
        return redirect('/')
    return render_template('carinfo.jinja', carinfoform=form, title = 'CarInfo')


#def commit(self):
    # db.session.add(self)
    # db.session.commit()



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
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username or Password was incorrect, try again')
            return redirect('/signin')
        flash(f'{username} successfully signed in!')
        login_user(user_match, remember=form.remember_me.data)
        return redirect('/')
    return render_template('signin.jinja', sign_in_form=form, title = 'Signin')



@app.route('/signup', methods= ['GET', 'POST'])
def signup():
    form = RegisterForm()
    print(form.errors)
    if form.validate_on_submit():
        
        username= form.username.data
        email= form.email.data
        password= form.password.data
        first_name= form.first_name.data
        last_name = form.last_name.data
        u = User(username=username,email=email,password_hash='', first_name=first_name, last_name=last_name)
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {username} already exists, try again')
            return redirect('/signup')
        elif email_match:
            flash(f'Email {email} already exists, try again')
            return redirect('/signup')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Request to register {username} successful')
            return redirect('/')
    return render_template('signup.jinja', sign_up_form= form, title = 'Sign Up Today')


@app.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect('/')


@app.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    cars = user_match.cars
    return render_template('user.jinja', user=user_match, cars=cars)
