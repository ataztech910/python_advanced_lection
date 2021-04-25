from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

# flask run --host=0.0.0.0

@app.route('/')
def hello_world():
    return 'Всем привет!'

@app.route('/another_route')
def another_route():
    return 'Еще один путь!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/template')
def template():
    name = 'Суперпользователь'
    return render_template('template.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Login'
    else:
        return 'Login form'

@app.route('/check_login', methods=['POST', 'GET'])
def check_login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('template.html', error=error)

def valid_login(username, password):
    return True
def log_the_user_in(username):
    return True

def get_current_user():
    return { 
        "username" : "test",
        "theme": "test theme",
        "image": "test image"
        }

def url_for(name, filename):
    return "test"

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }