"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase

from tests_setup import FollowTestCase



class SimpleTest(FollowTestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class LoginUserTest(FollowTestCase):


    

class HomePageTest(FollowTestCase):

    def homeResponse(self):
        return self.client.get('')

    def test_login_redirect(self):
        response = self.homeResponse()
        self.assertEqual(response.status_code, 200)
        redirect_chain = response.redirect_chain
        self.assertEqual(len(redirect_chain),1)
        redirect = redirect_chain[0]
        self.assertEqual(redirect[1],302)
        self.assertTrue(redirect[0].find('/login/') > 0)



