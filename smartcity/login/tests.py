from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY

# Create your tests here.
class LogInTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }

        self.credentials2 = {
            'username': 'doesnotexists',
            'password': 'bleh'
        }

        self.credentials3 = {
            'username': 'fakeuser',
            'password': 'this'
        }

        User.objects.create_user(**self.credentials)
        User.objects.create_user(**self.credentials3)

    def testLogin(self):
        response = self.client.post('/login/', self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_active)

    def testLoginNoUser(self):
        response = self.client.post('/login/', self.credentials2, follow=True)

        self.assertFalse(response.context['user'].is_active)

    def testLoginWithWrongPassword(self):
        response = self.client.post('/login/', {'username': 'fakeuser', 'password': 'that'}, follow=True)

        self.assertFalse(response.context['user'].is_active)

    def testLoginWithNoPassword(self):
        response = self.client.post('/login/', {'username': 'fakeuser', 'password': ''}, follow=True)

        self.assertFalse(response.context['user'].is_active)

    def testLoginWithPasswordOfAnotherUser(self):
        response = self.client.post('/login/', {'username': 'fakeuser', 'password': 'secret'}, follow=True)

        self.assertFalse(response.context['user'].is_active)
