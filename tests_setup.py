__author__ = 'jackdreilly'

from django.test import TestCase

from django.test.client import Client


class FollowClient(Client):

    def __init__(self,*args,**kwargs):
        super(FollowClient,self).__init__(*args,**kwargs)


    def get(self, path, data={}, follow=True, **extra):
        return super(FollowClient,self).get(path,data,follow,**extra)

class FollowTestCase(TestCase):
    client_class = FollowClient
