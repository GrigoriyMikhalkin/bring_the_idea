from django.forms import CharField

from .validators import *

class SkypeFormField(CharField):
    default_validators = [validate_skype]

    def clean(self, value):
        value = self.to_python(value).strip()
        return super().clean(value)
    

class TelegramFormField(CharField):
    default_validators = [validate_telegram]

    def clean(self, value):
        value = self.to_python(value).strip()
        return super().clean(value)
