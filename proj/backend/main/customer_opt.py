from flask import Blueprint

customer_opt = Blueprint('customer_opt', __name__)

@customer_opt.route('/customer/<username>', methods=['GET'])
def iamcustomer(username):
    return 'I am {name} ,is customer'.format(name=username)