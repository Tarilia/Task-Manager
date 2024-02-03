from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username",
                  "password1", "password2"]


class UpdateUserForm(CreateUserForm):
    def clean_username(self):
        return self.cleaned_data.get("username")
