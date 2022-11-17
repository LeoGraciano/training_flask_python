from flask import Blueprint, render_template, request

views = Blueprint('account', __name__)


@views.route('login', methods=['GET', 'POST'])
def login():
    form = request.form
    print(form)
    return render_template('account/login.html')


@views.route('logout')
def logout():
    return render_template('account/logout.html')


@views.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    form = request.form
    print(form)
    return render_template('account/sign_up.html')
