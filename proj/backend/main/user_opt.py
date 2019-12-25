from flask import Blueprint, render_template

user_opt = Blueprint('user_opt', __name__)

@user_opt.route('/user/<username>', methods=['GET'])
def iamuser(username):
    # return 'I am {} ,is user'.format(username)
    return render_template('hello.html')