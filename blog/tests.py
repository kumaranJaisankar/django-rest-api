from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post,Category
# Create your tests here.


class Test_create_post(TestCase):

    @classmethod 
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(username='test_user1',password='kumaran123')
        test_post = Post.objects.create(category_id = 1,title='post',excerpt = 'bla bla bla',content='bla bla bla',author_id=1,slug='post-title',status='published')
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        title = f'{post.title}'
        status= f'{post.status}'
        self.assertEquals(author,'test_user1')
        self.assertEquals(title,'post')
        self.assertEquals(content,'Post content')
        self.assertEquals(str(post),'post title')
        self.assertEquals(str(cat),'django')