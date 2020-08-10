from flask import Flask, request, jsonify, session, redirect, url_for
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

from user import User



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
    
@app.route('/registration/')
def registration():
    params = request.args
    login = params.get('login')
    password = params.get('password')
    
    if not login and not password:
        return 'No login and password provided.'
    elif not login:
        return 'No login provided.'
    elif not password:
        return 'No password provided.'
    
    user = User(login=login, password=password)
    try:
        user.save()
    except:
        return f'Try another login'        
    return f'Registration completed!'

@app.route('/login/')
def login():
    params = request.args
    param_login = params.get('login')
    param_password = params.get('password')

    user = User.objects.filter(login=param_login)
    if not user:
        return 'Invalid login.'
    elif user[0].password != param_password:
        return 'Invalid password.'
    
    session['login'] = param_login
    session['password'] = param_password
    
    return 'Login is successful.'

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