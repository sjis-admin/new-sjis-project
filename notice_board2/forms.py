from django import forms
from .models import Grade, NoticeBoard
from tinymce.widgets import TinyMCE
from django.core.exceptions import ValidationError
import bleach

class NoticeBoardForm(forms.ModelForm):
    target_grades = forms.ModelMultipleChoiceField(
        queryset=Grade.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = NoticeBoard
        fields = ['title', 'content', 'target_grades', 'attachment']
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30})
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        # Sanitize content
        cleaned_content = bleach.clean(
            content,
            tags=['p', 'strong', 'em', 'u', 'h1', 'h2', 'h3', 'ul', 'ol', 'li', 'br', 'span'],
            attributes={
                'p': ['class'],
                'span': ['class'],
            }
        )
        return cleaned_content

class NoticeBoardAdminForm(NoticeBoardForm):
    class Meta:
        model = NoticeBoard
        fields = '__all__'
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30})
        }
