import json

from tornado import testing

import examples.app


class SimpleStatusTests(testing.AsyncHTTPTestCase):

    def get_app(self):
        return examples.app.make_app(debug=True)

    def test_that_content_type_is_set(self):
        response = self.fetch('/status')
        self.assertEqual(response.code, 200)
        self.assertTrue(
            response.headers['Content-Type'].startswith('application/json'))

    def test_that_application_name_is_included(self):
        response = self.fetch('/status')
        self.assertEqual(response.code, 200)
        body = json.loads(response.body.decode('utf-8'))
        self.assertEqual(body['name'], examples.app.name)

    def test_that_application_version_is_included(self):
        response = self.fetch('/status')
        self.assertEqual(response.code, 200)
        body = json.loads(response.body.decode('utf-8'))
        self.assertEqual(body['version'], examples.app.version)

    def test_that_application_status_is_included(self):
        response = self.fetch('/status')
        self.assertEqual(response.code, 200)
        body = json.loads(response.body.decode('utf-8'))
        self.assertEqual(body['status'], 'ok')
