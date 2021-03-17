from app import HelloWorld
from flask import Flask
from flask_restful import Api
import pytest
from controller import hello_world

app = Flask(__name__)
api = Api(app)
api.add_resource(hello_world.HelloWorld, '/')

@pytest.fixture
def root():
    app.config['TESTING'] = True
    response = app.test_client().get('/')
    return response