from chocolate.models import Factory
from chocolate.rest import TastyFactory

from django.contrib.auth.models import User

from models import Post, Comment, Movie, Actor
from api import api

factory = Factory()
factory.register(Post)
factory.register(User)
factory.register(Comment)
factory.register(Movie)
factory.register(Actor)

tastyfactory = TastyFactory(factory, api)
