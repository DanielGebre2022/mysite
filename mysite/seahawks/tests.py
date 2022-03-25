from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Publisher, Book;
from .forms import AuthorForm, PublisherForm;
from django.urls import reverse_lazy, reverse
# Create your tests here.
class AuthorTest(TestCase):
    def setUp(self):
        self.type=Author(first_name='John')
    
   
    def test_typestring(self):
        self.assertEqual(str(self.type), 'John') 

    def test_tablename(self):
        self.assertEqual(str(Author._meta.db_table), 'author')

# Create your tests here.

class PublisherTest(TestCase):
    def setUp(self):
        self.type=Publisher(name='Joe')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Joe') 

    def test_tablename(self):
        self.assertEqual(str(Publisher._meta.db_table), 'publisher')

class New_Author_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='Leteletelete12')
        self.type=Author.objects.create(first_name='Brad', last_name='Pitt', email='Joe', )
        self.book=Author.objects.create(first_name='Brad', last_name='Pitt', email='Joe',  )

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newauthor'))
        self.assertRedirects(response, '/mysite/newauthor/')