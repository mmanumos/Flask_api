from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase):
    """ extends TestCase """

    def create_app(self):
        """ extended method """
        
        app.config['TESTING'] = True
        """ TESTING ENVIRONMET IS ENABLED """ 

        app.config['WTF_CSRF_ENABLED'] = False
        """ CROSS SITE REQUEST FORGERY TOKEN is disabled """
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
 
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)
    
    def test_hello_post(self):
        """ Validate that post it's not will be allowed """
        response = self.client.post(url_for('hello'))
        self.assertTrue(response.status_code, 405)

    def test_auth_blueprint_exits(self):
        """ Validate if the blueprint is registered """
        self.assertIn('auth', self.app.blueprints)


    def test_auth_login_get(self):
        """ Validate if exists route into blueprint """
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_auth_login_template(self):
        """ Validate if is the correct template for the route """
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        """ Validate if post is working for login """
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertRedirects(response, url_for('index'))
