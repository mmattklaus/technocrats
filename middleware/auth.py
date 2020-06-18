from functools import wraps
from flask import session, redirect, url_for, request, flash


def auth(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Access to this resource is protected. Please login.", "danger")
            return redirect(url_for('login'))

    return wrap


def guest(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' not in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('home', next=request.url))

    return wrap
