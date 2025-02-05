from django import forms
from django.contrib.auth.forms import UserCreationForm

from agency.models import Redactor, Topic, Newspaper


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = ('username', 'email', 'first_name', 'last_name',
                  'years_of_experience', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 '
                         'bg-white border rounded-md focus:border-blue-500 '
                         'focus:outline-none focus:ring'
            })

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get('username')

        if username and not username.isascii():
            self.add_error(
                'username',
                'Username must contain only Latin characters'
            )
        return cleaned_data


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ["title", "topic", "content", "publishers"]
        widgets = {
            "topic": forms.CheckboxSelectMultiple,
            "publishers": forms.CheckboxSelectMultiple,
        }
