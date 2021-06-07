import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import *
from auth import *

ROWS_PER_PAGE = 10

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)

  cors = CORS(app)
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 
    'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 
    'GET,PATCH,POST,DELETE,OPTIONS')
    return response
  

  def paginate(request, selection):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * ROWS_PER_PAGE
    end = start + ROWS_PER_PAGE

    objects = [objects.format() for objects in selection]
    objects_formatted = objects[start:end]
    return objects_formatted
  
  @app.route('/actors')
  @requires_auth('get:actors')
  def get_actors(payload):
    actors = Actor.query.all()
    actors_paginate = paginate(request, actors)

    if not actors_paginate:
      abort(404)

    return jsonify({
      'success': True,
      'actors': actors_paginate
    }), 200

  @app.route('/movies')
  @requires_auth('get:movies')
  def get_movies(payload):
    movies = Movie.query.all()
    movies_paginate = paginate(request, movies)

    if not movies_paginate:
      abort(404)

    return jsonify({
      'success': True,
      'movies': movies_paginate
    }), 200

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def add_actor(payload):
    data = request.get_json()

    if 'name' not in data:
      abort(422)
    if 'age' not in data:
      abort(422)
    if 'gender' not in data:
      abort(422)

    actor = Actor(
      name=data['name'],
      age=data['age'],
      gender=data['gender']
    )
    actor.insert()

    return jsonify({
      'success': True,
      'actor': actor.format()
    }), 200

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def add_movie(payload):
    data = request.get_json()

    if 'title' not in data:
      abort(422)
    if 'release' not in data:
      abort(422)

    movie = Movie(title=data['title'], release=data['release'])
    movie.insert()

    return jsonify({
      'success': True,
      'movie': movie.format()
    }), 200

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(payload,actor_id):
    if not actor_id:
      abort(404)


    actor = Actor.query.get(actor_id)
    if not actor:
      abort(404)

    data = request.get_json()

    if 'name' in data and data['name']:
      actor.name = data['name']

    if 'age' in data and data['age']:
      actor.age = data['age']

    if 'gender' in data and data['gender']:
      actor.gender = data['gender']

    actor.update()

    return jsonify({
      'success': True,
      'actor': actor.format(),
    }), 200

  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie(payload,movie_id):
    if not movie_id:
      abort(404)


    movie = Movie.query.get(movie_id)
    if not movie:
      abort(404)

    data = request.get_json()

    if 'title' in data and data['title']:
      movie.title = data['title']

    if 'release' in data and data['release']:
      movie.release = data['release']

    movie.update()

    return jsonify({
      'success': True,
      'movie': movie.format(),
    }), 200

  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(payload, actor_id):
    if not actor_id:
      abort(404)

    actor = Actor.query.get(actor_id)
    if not actor:
      abort(404)

    actor.delete()

    return jsonify({
      'success': True,
      'deleted': actor.id
    }), 200

  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload,movie_id):
    if not movie_id:
      abort(404)

    movie = Movie.query.get(movie_id)
    if not movie:
      abort(404)

    movie.delete()

    return jsonify({
      'success': True,
      'deleted': movie.id
    }), 200

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
    }), 400

  @app.errorhandler(401)
  def not_authorized(error):
    return jsonify({
      "success": False,
      "error": 401,
      "message": "unauthorized"
    }), 401

  @app.errorhandler(403)
  def forbidden(error):
    return jsonify({
      "success": False,
      "error": 403,
      "message": "forbidden"
    }), 403

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource not found"
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
    }), 422

  @app.errorhandler(authError)
  def auth_error(authError):
    return jsonify({
      'success': False,
      'error': authError.status_code,
      'message': authError.error['description']
    }), authError.status_code

  return app

app = create_app()

if __name__ == '__main__':
    app.run()