from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models import CharField

from .formfields import SkypeFormField, TelegramFormField
from .validators import *


class SkypeField(CharField):
    default_validators = [validate_skype]
    description = "Skype"

    def __init__(self, *args, **kwargs):
        self.min_length = 6
        self.max_length = 32
        kwargs["max_length"] = kwargs.get("max_length", self.max_length)

        super().__init__(*args, **kwargs)
        self.validators.append(MinLengthValidator(self.min_length))
        self.validators.append(MaxLengthValidator(self.max_length))

    def formfield(self, **kwargs):
        defaults = {
            'form_class': SkypeFormField,
            'min_length': self.min_length,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
    

class TelegramField(CharField):
    default_validators = [validate_telegram]
    description = "Telegram"

    def __init__(self, *args, **kwargs):
        self.min_length = 6
        self.max_length = 33
        kwargs["max_length"] = kwargs.get("max_length", self.max_length)

        super().__init__(*args, **kwargs)
        self.validators.append(MinLengthValidator(self.min_length))
        self.validators.append(MaxLengthValidator(self.max_length))

    def formfield(self, **kwargs):
        defaults = {
            'form_class': TelegramFormField,
            'min_length': self.min_length,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
