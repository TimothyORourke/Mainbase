from posts.models import Post
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
    
    text = forms.CharField(label="", widget=forms.Textarea(attrs={
        "rows":4, 
        "style" : "resize:none;width:100%;", 
        "placeholder" : "Post something..."}
    ))
