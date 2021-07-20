from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser): #same default user but customisable in future
    pass #add here more feilds in the future if need arises