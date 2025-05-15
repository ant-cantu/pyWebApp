# web_app.py
from flask import Flask, render_template
import datetime

app = Flask(__name__)
current_time = datetime.datetime.now()

@app.route('/')
def home():
    page_title = "Welcome to My Web App"
    return render_template('home.html', 
                           title=page_title, 
                           time=current_time)

@app.route('/about')
def about_me_page():
    page_title = "About Me"
    return render_template('about.html', 
                           title=page_title,
                           time=current_time)

@app.route('/greet/<name>')
def greet_user(name):
    page_title = f"Hello {name.capitalize()}!"
    return render_template('greet.html', 
                           user_name_in_template=name.capitalize(),
                           title=page_title,
                           time=current_time)

if __name__ == "__main__":
    app.run(debug=True)