from django.contrib.auth.hashers import make_password
from django.forms import Form

from shop.models import User


class RegisterForm(Form):
    class Meta:
        model = User
        exclude = [
            'is_staff',
            'is_superuser',
            'is_active',
            'image'
        ]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)
