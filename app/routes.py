from flask import render_template
from app import app
#from app.forms import RegisterForm


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


# @app.route('/signin')
# def signin():
#     # form = RegisterForm()
#     return render_template('signin.jinja', title = 'Sign in')


@app.route('/howdoesitwork')
def howdoesitwork():
    return render_template('howdoesitwork.jinja', title = 'How does it work?')

@app.route('/join')
def join():
    return render_template('join.jinja', title = 'Join Today')

@app.route('/rentacar')
def rentacar():
    return render_template('rentacar.jinja', title = 'RentaCar')

@app.route('/contactus')
def contactus():
    return render_template('contactus.jinja', title = 'Contact Us')
