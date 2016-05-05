from django.utils.translation import ugettext_lazy as _
from django.core.validators import _lazy_re_compile
from django.core.exceptions import ValidationError
from django.utils.encoding import force_text


def validate_skype(value):
    value = force_text(value)
    skype_regex = _lazy_re_compile(r'[a-zA-Z][\w,.-]+$')

    if skype_regex.match(value):
        return True

    raise ValidationError(_("Invalid Skype username"))


def validate_telegram(value):
    value = force_text(value)
    telegram_regex = _lazy_re_compile(r'@[a-zA-Z]\w+[a-zA-Z0-9]$')

    if telegram_regex.match(value):
        return True

    raise ValidationError(_("Invalid Telegram username"))
    

