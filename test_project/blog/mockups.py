from chocolate.models import ModelFactory
from chocolate.rest import TastyFactory

from django.contrib.auth.models import User

from models import Post, Comment, Movie, Actor
from api import api

factory = ModelFactory()
factory.register(Post)
factory.register(User)
factory.register(Comment)
factory.register(Movie)
factory.register(Actor)

tastyfactory = TastyFactory(api)
