from tastypie.resources import ModelResource
from tastypie.api import Api
from tastypie import fields
from models import Post, Comment


class PostResource(ModelResource):

    class Meta:
        queryset = Post.objects.all()


class CommentResource(ModelResource):

    post = fields.ForeignKey("blog.api.PostResource", attribute="post")

    class Meta:
        queryset = Comment.objects.all()


api = Api(api_name="v1")
api.register(PostResource())
api.register(CommentResource())
