from django.test import TestCase
from django.core.exceptions import ValidationError

from agency.forms import TopicForm, ArticleForm, CustomUserCreationForm
from agency.models import Redactor, Topic, Newspaper


class ModelTestCase(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='John',
            last_name='Doe',
            years_of_experience=5
        )

        self.topic1 = Topic.objects.create(name='Technology')
        self.topic2 = Topic.objects.create(name='Politics')

    def test_redactor_str_method(self):
        self.assertEqual(str(self.redactor), 'John Doe')

    def test_redactor_years_of_experience_validation(self):
        try:
            self.redactor.full_clean()
        except ValidationError:
            self.fail("Redactor validation failed unexpectedly")

        with self.assertRaises(ValidationError):
            invalid_redactor = Redactor(
                username='invaliduser',
                password='testpass',
                years_of_experience=-1
            )
            invalid_redactor.full_clean()

        with self.assertRaises(ValidationError):
            invalid_redactor = Redactor(
                username='invaliduser',
                password='testpass',
                years_of_experience=101
            )
            invalid_redactor.full_clean()

    def test_topic_str_method(self):
        self.assertEqual(str(self.topic1), 'Technology')

    def test_newspaper_creation_with_multiple_topics(self):
        newspaper = Newspaper.objects.create(
            title='Test Newspaper',
            content='Test content'
        )

        newspaper.topic.add(self.topic1, self.topic2)
        newspaper.publishers.add(self.redactor)

        self.assertEqual(newspaper.topic.count(), 2)
        self.assertEqual(newspaper.publishers.count(), 1)

        self.assertIn(newspaper, self.topic1.articles.all())
        self.assertIn(newspaper, self.topic2.articles.all())
        self.assertIn(newspaper, self.redactor.published_articles.all())


class FormsTestCase(TestCase):
    def setUp(self):
        self.user = Redactor.objects.create_user(
            username='testuser',
            password='testpassword',
            years_of_experience=5
        )
        self.topic = Topic.objects.create(name='Test Topic')

    def test_custom_user_creation_form_valid(self):
        form_data = {
            'username': 'newuser',
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'years_of_experience': 3,
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid_username(self):
        form_data = {
            'username': 'юзернейм',
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'years_of_experience': 3,
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_topic_form_valid(self):
        form_data = {'name': 'New Topic'}
        form = TopicForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_article_form_valid(self):
        form_data = {
            'title': 'Test Article',
            'content': 'Test content',
            'topic': [self.topic.id],
            'publishers': [self.user.id]
        }
        form = ArticleForm(data=form_data)
        self.assertTrue(form.is_valid())