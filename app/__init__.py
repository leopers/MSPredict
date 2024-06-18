from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.secret_key = '4567832476789749376812794382617294381479848712897489127489721894798127897198247981724897124481628912469846102342547'
    
    with app.app_context():
        from . import routes

        # Register Blueprints
        app.register_blueprint(routes.main_bp)

        return app
