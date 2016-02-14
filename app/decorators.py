# coding:utf-8
from functools import wraps
from flask.ext.login import current_user
from flask import current_app,abort


def admin_required(func):
    '''
    只允许admin权限用户访问视图route
    example::

        @app.route('/post')
        @admin_required
        def post():
            pass


    '''

    @wraps(func)
    def decorated_view(*args, **kwargs):

        if not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        if not current_user.admin:
            abort(403)
        return func(*args, **kwargs)

    return decorated_view
