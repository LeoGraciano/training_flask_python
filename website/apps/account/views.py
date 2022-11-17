from flask import Blueprint, render_template

views = Blueprint('account', __name__)


@views.route('login')
def login():
    return render_template('account/login.html')


@views.route('logout')
def logout():
    return render_template('account/logout.html')


@views.route('sign-up')
def sign_up():
    return render_template('account/sign_up.html')
