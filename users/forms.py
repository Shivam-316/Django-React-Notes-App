from django.contrib.auth.forms import UserCreationForm
from .models import Author

class AuthorCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Author
        fields = UserCreationForm.Meta.fields