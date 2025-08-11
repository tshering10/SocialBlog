from django import forms
from posts.models import Post, Comment

class PostForm(forms.ModelForm):  
    class Meta:
        model = Post
        fields = ("content",)
        widgets = {
            'content': forms.Textarea(attrs={'rows':6, 'placeholder': "Share your thoughts.... "}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {
            "comment": "",
        }
        widgets = {
            'comment': forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Comment your opinion.",
                "class": "form-control"
            })
        }
        