from flask import Flask,render_template
from app.routes import simple_page
from flask_bootstrap import Bootstrap
def create_app(config_name=''):
        app = Flask(__name__)
        #app.config.from_object(config[config_name])
        Bootstrap(app)
        app.register_blueprint(simple_page, url_prefix='/simple')
        app.debug = True
        return app
