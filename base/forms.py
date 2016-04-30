from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext as _


class IdeaForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget)
    author = forms.CharField(required=False)
    
    class Meta:
        model = Idea
        fields = [
            _("author"),
            _("title"),
            _("content"),
            #_("source"),
        ]


class CommentForm(forms.ModelForm):
    author = forms.CharField(required=False)
    
    class Meta:
        model = Comment
        fields = [
            _("author"),
            _("content"),
        ]
