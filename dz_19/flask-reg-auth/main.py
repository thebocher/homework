from flask import Flask, request, jsonify, session, redirect, url_for
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

from user import User

import hashlib


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://mongo_user:lolon123@cluster0.xweys.mongodb.net/dz_19?retryWrites=true&w=majority'
}
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)




def if_auth(if_ses, if_no):
    if (session.get('login') and session.get('password')):
        return if_ses
    else:
        return if_no

@app.route('/')
def index():
    return if_auth(
        if_ses=redirect(url_for('authorized')),
        if_no=redirect(url_for('unauthorized'))
    )
    
@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    form_html = """<form method="POST" action="/registration/">
    <input name="login" placeholder="Your login" type="text">
    <input name="password" placeholder="Your Password" type="password">
    <button>Register</button>
</form>"""
    if request.method == 'GET':
        return form_html
    elif request.method == 'POST':
        form = request.form
        login = form.get('login')
        password = hashlib.sha1(
            form.get('password').encode()
        ).hexdigest()
        # print(password)
        
        # return jsonify(request.form)
    # params = request.args
    # login = params.get('login')
    # password = params.get('password')
    
        if not login and not password:
            return f'No login and password provided.{form_html}'
        elif not login:
            return f'No login provided.{form_html}'
        elif not password:
            return f'No password provided.{form_html}'
        
        user = User(login=login, password=password)
        try:
            user.save()
        except:
            return f'Try another login.{form_html}'
        return 'Successfully registered.'    

@app.route('/login/', methods=['POST', 'GET'])
def login():
    form_html = """<form method="POST" action="/login/">
    <input name="login" placeholder="Your login" type="text">
    <input name="password" placeholder="Your Password" type="password">
    <button>Login</button>
</form>"""
    if request.method == 'POST':
        form = request.form
        login = form.get('login')
        password = hashlib.sha1(
            form.get('password').encode()
        ).hexdigest()

        user = User.objects.filter(login=login)
        if not user:
            return f'Invalid login.{form_html}'
        elif user[0].password != password:
            return f'Invalid password.{form_html}'
        
        session['login'] = login
        session['password'] = password
        
        return 'Login is successful.'
    elif request.method == 'GET':
        return form_html

@app.route('/logout/')
def logout():
    session.pop('login')
    session.pop('password')
    return 'You have just log out'

@app.route('/unauthorized/')
def unauthorized():
    return if_auth(
        if_ses=redirect(url_for('authorized')),
        if_no='You are not authorized'
    )

@app.route('/authorized/')
def authorized():
    return if_auth(
        if_ses='You are authorized',
        if_no=redirect(url_for('unauthorized')) 
    )



if __name__ == "__main__":
    app.run(debug=True)