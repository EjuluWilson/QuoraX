from django_registration.forms import RegistrationForm
from users.models import CustomUser

class CustomForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser #connect form to model
