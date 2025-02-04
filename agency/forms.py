from django.contrib.auth.forms import UserCreationForm

from agency.models import Redactor


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = ('username', 'years_of_experience', 'password1', 'password2')

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
