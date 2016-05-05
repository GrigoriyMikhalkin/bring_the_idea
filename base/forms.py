from django.utils.translation import ugettext as _
from django import forms

from ckeditor.widgets import CKEditorWidget

from .formfields import SkypeFormField
from .models import *


class IdeaForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget)
    author = forms.CharField(required=False)
    source = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    skype = SkypeFormField(required=False)
    
    class Meta:
        model = Idea
        fields = [
            _("author"),
            _("title"),
            _("content"),
            _("source"),
            _("email"),
            _("skype"),
            _("telegram"),
        ]


class CommentForm(forms.ModelForm):
    author = forms.CharField(required=False)
    
    class Meta:
        model = Comment
        fields = [
            _("author"),
            _("content"),
        ]
