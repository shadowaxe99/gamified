import ssl

from flask import Flask
from flask_login import (LoginManager, UserMixin, login_required, login_user,
                         logout_user)
from flask_principal import Permission, Principal, RoleNeed, identity_loaded
from flask_sslify import SSLify
from wtforms import Form, PasswordField, StringField, validators

app = Flask(__name__)
sslify = SSLify(app)
login_manager = LoginManager(app)
principal = Principal(app)

class LoginForm(Form):
    email = StringField('Email', [validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])

class RegistrationForm(Form):
    email = StringField('Email', [validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8),
        validators.EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Confirm Password')

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Perform login logic here
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return 'Logged in successfully'
        else:
            return 'Invalid email or password'
    return 'Login form'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Perform registration logic here
        return 'Registered successfully'
    return 'Registration form'

@app.route('/protected')
@login_required
def protected():
    return 'Protected route'

# Define roles and permissions
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

# Example of using permissions
@app.route('/admin')
@admin_permission.require(http_exception=403)
def admin():
    return 'Admin route'

@app.route('/user')
@user_permission.require(http_exception=403)
def user():
    return 'User route'

# Identity loaded callback
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Add roles to the identity
    if current_user.is_authenticated:
        if current_user.is_admin:
            identity.provides.add(RoleNeed('admin'))
        else:
            identity.provides.add(RoleNeed('user'))
