from django import forms
from posts.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ("title","body","image")
        widgets = {
            'title':forms.TextInput(attrs={'class':'editable'}),
            'body' :forms.Textarea( attrs={'class':'editable medium-editor-textarea',
                                           'style':'overflow:auto;resize:none;height:100px;'}),
        } 
    
    

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text' :forms.Textarea(attrs={'class':'editable medium-editor-textarea',
                                          'style':'overflow:auto;resize:none;height:100px;'}),
        } 