from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    user = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control name', 'placeholder': 'Names',
                                                        }), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control email', 'placeholder': 'Email',
                                                        }))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control textarea', 'placeholder': 'Comment',
                                                        }), required=True)

    class Meta:
        model = Comment
        fields = ['user', 'email', 'body']

