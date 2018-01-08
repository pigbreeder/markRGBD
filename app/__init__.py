from flask import Flask,render_template,redirect,url_for
from app.routes import simple_page
from flask_bootstrap import Bootstrap
def create_app(config_name=''):
        app = Flask(__name__)
        #app.config.from_object(config[config_name])
        @app.route('/')
        def home():
            # return 'home'
            # redirect(url_for('simple_page.index'))
            return redirect('/simple/video')
        Bootstrap(app)
        app.register_blueprint(simple_page, url_prefix='/simple')
        app.debug = True
        return app
