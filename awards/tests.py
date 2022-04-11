from django.test import TestCase
from .models import *

# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='charles')
        self.post = Project.objects.create(id=1, title='test post', photo='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, url='http://ur.coml')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Project))

    def test_save_post(self):
        self.post.save_post()
        post = Project.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Project.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Project.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Project.search_project('test')
        self.assertTrue(len(post) < 1)