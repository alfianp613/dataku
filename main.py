########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db

########################################################################################
# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/shop') # profile page that return 'profile'
@login_required
def shop():
    return render_template('Data-Shop.html', name=current_user.name)

@main.route('/shop/scrapping')
def scrapping():
    return render_template('E-Commerce-Data-Scrapping.html')


@main.route('/shop/cleaning')
def cleaning():
    return render_template('Cleaning-Data.html')

@main.route('/shop/vis')
def vis():
    return render_template('Visualisasi-Data.html')

@main.route('/shop/dashboard')
def dashboard():
    return render_template('Pembuatan-Dashboard.html')

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode