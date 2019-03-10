
import unittest
from api.app import create_app


class IndexTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app('development')
        self.client = self.app.test_client

    def test_index(self):
        response = self.client().get('/api/v1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual({'data': 'Hello Test'}, response.json)
