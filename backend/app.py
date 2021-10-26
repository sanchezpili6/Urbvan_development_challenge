from flask import Flask
from flask_cors import CORS

from api.employee_routes import employee_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(employee_blueprint)

    return app


app = create_app()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000, debug=True)