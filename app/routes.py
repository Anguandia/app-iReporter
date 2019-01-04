import os
from flask import request, jsonify
from app import create_app
from .validation import Validation


config_name = os.getenv('FLASK_ENV')
app = create_app('TESTING')


@app.route('/')
@app.route('/api/v1')
@app.route('/api/v1/')
def home():
    return jsonify({
      'create or get all flags': '/red_flags',
      'get or delete single flag': '/red_flags/id',
      'edit flag': '/red_flags/id/field'
      })


@app.route('/api/v1/<resource>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
@app.route(
  '/api/v1/<resource>/<id>', methods=['GET', 'POST', 'PATCH', 'DELETE']
  )
@app.route(
  '/api/v1/<resource>/<id>/<action>',
  methods=['GET', 'POST', 'PATCH', 'DELETE']
  )
def wrongURL(resource, methods=['get'], id=None, action=None):
    if Validation().validateRoute(resource):
        res = Validation().validateRoute(resource)
    elif request.method not in methods:
        res = [405, 'error', 'wrong method']
    return jsonify({'Status': res[0], res[1]: res[2]}), res[0]
