from django_registration.forms import RegistrationForm
from users.models import CustomUser

class CustomFrorm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser #connect form to model
