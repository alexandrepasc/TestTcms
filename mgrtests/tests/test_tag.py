from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from mgrtests.models import Tag


class TestTag(TestCase):

    def setUp(self):
        user = User.objects.create_user('user', 'user@mail.com')
        user.set_password('123qwe')
        user.save()

        Tag.objects.create(
            id='ea97b6e8-4cdf-4c9d-bf82-2aadf5c8bf9d',
            name='test',
            description='desc',
            created_by=user,
            created_at=1568197168577
        )

    def test_name_content(self):
        tag = Tag.objects.get(id='ea97b6e8-4cdf-4c9d-bf82-2aadf5c8bf9d')
        expected_name = f'{tag.name}'
        assert expected_name == 'test'

    def test_new_tag_no_auth(self):
        path = reverse('newTag')

        self.client.post(path, {'name': 'newTag', 'description': 'new description'})

        try:
            new_tag = Tag.objects.get(name='newTag')
        except Tag.DoesNotExist:
            new_tag = None

        self.assertEquals(new_tag, None)

    def test_new_tag(self):
        path = reverse('newTag')

        self.client.post('/login', {'username': 'user', 'password': '123qwe'})

        self.client.post(path, {'name': 'newTag', 'description': 'new description'})

        try:
            new_tag = Tag.objects.get(name='newTag')
        except Tag.DoesNotExist:
            new_tag = None

        self.assertNotEquals(new_tag, None)
        self.assertEquals(new_tag.description, 'new description')
