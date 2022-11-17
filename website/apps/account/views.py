from flask import Blueprint, render_template

views = Blueprint('account', __name__)


@views.route('login', methods=['GET', 'POST'])
def login():
    context = {
        'test': 'Testando'
    }
    return render_template('account/login.html', **context)


@views.route('logout')
def logout():
    return render_template('account/logout.html')


@views.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template('account/sign_up.html')
