from flask import Flask,render_template,g,session
from flask_cors import CORS

def creat_app():
    app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/backend/static")
    # 防止跨域攻击
    CORS(app)
    # 注册蓝图
    from . import main
    from .main.user_opt import user_opt
    from .main.customer_opt import customer_opt
    app.register_blueprint(main.main)
    app.register_blueprint(user_opt, url_prefix="/user_opt") #注册蓝图，并指定对应的前缀（url_prefix）
    app.register_blueprint(customer_opt)
    # app.register_blueprint(customer_opt, url_prefix="/customer_opt")
    app.config["SECRET_KEY"] = "hello"
    app.debug = True
    # db.init_app(app)
    return app

