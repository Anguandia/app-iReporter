from flask import jsonify
from app.routes.routes import app


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'Status': 400, 'error': 'empty request'}), 400
