from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('login')
def login():
    return "<h1>Login</h1>"


@auth.route('logout')
def logout():
    return "<h1>Login</h1>"


@auth.route('sign-up')
def sign_up():
    return "<h1>Sign-up</h1>"


@auth.route('sign-in')
def sign_in():
    return "<h1>Sign-in</h1>"