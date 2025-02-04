from django.test import TestCase
from django.test.client import Client

from agency.forms import CustomUserCreationForm


class TestAuthentication(TestCase):
    def setUp(self):
        self.client = Client()

    def test_non_ascii_username(self):
        form_data = {
            'username': 'ハロー・ワールド',
            'years_of_experience': 5,
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        form = CustomUserCreationForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertEqual(
            form.errors['username'][0],
            'Username must contain only Latin characters'
        )
