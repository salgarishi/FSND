import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import *

class AgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency"
        self.database_path = "postgresql://postgres:123!@#@{}/{}".format(
                             'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_actors_paginated(self):

        res = self.client().get('/actors?page=1', headers={'Authorization': 'Bearer ' + Casting_Assistant_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_actors_paginated404(self):

        res = self.client().get('/actors?page=1000', headers={'Authorization': 'Bearer ' + Casting_Assistant_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')


    def test_get_actors_paginated_without_autherization401(self):

        res = self.client().get('/actors?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Authorization header is expected.')
    

    
    def test_create_new_actor(self):
        
        json_actor = {
            'name' : 'Keanu Reaves',
            'age' : 58,
            'gender' : 'male'
        } 

        res = self.client().post('/actors',json = json_actor, headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    
    def test_create_new_actor422(self):
        
        json_actor = {
            'name' : 'Keanu Reaves',
            'age' : 58
        } 

        res = self.client().post('/actors',json = json_actor, headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'unprocessable')
    

    
    def test_create_new_actor_without_permission403(self):
        
        json_actor = {
            'name' : 'Keanu Reaves',
            'age' : 58,
            'gender' : 'male'
        } 

        res = self.client().post('/actors',json = json_actor, headers={'Authorization': 'Bearer ' + Casting_Assistant_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Permission not found.')
    

    def test_create_new_actor_without_autherization401(self):
        
        json_actor = {
            'name' : 'Keanu Reaves',
            'age' : 58,
            'gender' : 'male'
        } 

        res = self.client().post('/actors',json = json_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Authorization header is expected.')

    def test_update_actor(self):
        
        json_actor = {
            'age' : 59
        } 

        res = self.client().patch('/actors/2',json = json_actor, headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_update_actor404(self):
        
        json_actor = {
            'age' : 59,
        } 

        res = self.client().patch('/actors/1000',json = json_actor, headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')

    def test_update_actor_without_permission403(self):
        
        json_actor = {
            'age' : 59
        } 

        res = self.client().patch('/actors/1',json = json_actor, headers={'Authorization': 'Bearer ' + Casting_Assistant_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Permission not found.')
    
    def test_update_actor_without_autherization401(self):
        
        json_actor = {
            'age' : 59
        } 

        res = self.client().patch('/actors/1',json = json_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Authorization header is expected.')
    
    def test_delete_actor(self): 

        res = self.client().delete('/actors/1', headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_actor404(self):

        res = self.client().delete('/actors/1000', headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')

    def test_delete_actor_without_autherization401(self):

        res = self.client().delete('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Authorization header is expected.')

    def test_delete_actor_without_permission403(self):

        res = self.client().delete('/actors/1', headers={'Authorization': 'Bearer ' + Casting_Assistant_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Permission not found.')


    """Movies Test"""

    def test_get_movies_paginated(self):

        res = self.client().get('/movies?page=1', headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_movies_paginated404(self):

        res = self.client().get('/movies?page=1000', headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')


    def test_get_movies_paginated_without_autherization401(self):

        res = self.client().get('/movies?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Authorization header is expected.')
    

    
    def test_create_new_movie(self):
        
        json_movie = {
            'title' : 'Inception',
            'release': '2010'
        } 

        res = self.client().post('/movies',json = json_movie, headers={'Authorization': 'Bearer ' + Executive_Producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    
    def test_create_new_movie422(self):
        
        json_movie = {
            'title' : 'Inception'
        } 

        res = self.client().post('/movies',json = json_movie, headers={'Authorization': 'Bearer ' + Executive_Producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'unprocessable')
    

    
    def test_create_new_movie_without_permission403(self):
        
        json_movie = {
            'title' : 'Inception',
            'release': '2010'
        } 

        res = self.client().post('/movies',json = json_movie, headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Permission not found.')
    

    def test_create_new_movie_without_autherization401(self):
        
        json_movie = {
            'title' : 'Inception',
            'release': '2010'
        } 

        res = self.client().post('/movies',json = json_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Authorization header is expected.')

    def test_update_movie(self):
        
        json_movie = {
            'release' : '2009'
        } 

        res = self.client().patch('/movies/2',json = json_movie, headers={'Authorization': 'Bearer ' + Executive_Producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_update_movie404(self):
        
        json_movie = {
            'release' : '2009'
        } 

        res = self.client().patch('/movies/1000',json = json_movie, headers={'Authorization': 'Bearer ' + Executive_Producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')

    def test_update_movie_without_permission403(self):
        
        json_movie = {
            'release' : '2009'
        } 

        res = self.client().patch('/movies/1',json = json_movie, headers={'Authorization': 'Bearer ' + Casting_Assistant_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Permission not found.')
    
    def test_update_movie_without_autherization401(self):
        
        json_movie = {
            'release' : '2009'
        } 

        res = self.client().patch('/movies/1',json = json_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Authorization header is expected.')
    
    def test_delete_movie(self): 

        res = self.client().delete('/movies/1', headers={'Authorization': 'Bearer ' + Executive_Producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_movie404(self):

        res = self.client().delete('/movies/1000', headers={'Authorization': 'Bearer ' + Executive_Producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')

    def test_delete_movie_without_autherization401(self):

        res = self.client().delete('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Authorization header is expected.')

    def test_delete_movie_without_permission403(self):

        res = self.client().delete('/movies/1', headers={'Authorization': 'Bearer ' + Casting_Director_Token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Permission not found.')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
