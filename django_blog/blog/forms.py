from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import Profile
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=13, required=True)
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email','phone')

class ProfileForm(forms.ModelForm):
    class meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name']

class UpdateProfileInfo(forms.ModelForm):
    class meta:
        model = Profile
        fields = ['first_name', 'last_name','email', 'phone', 'bio', 'Profile_picture']

#task 3 
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > 5500: # this enforces max length
            raise forms.ValidationError("Comment is too long (max 5500 characters).")

        return content
    

# task 4
from .models import Post
from taggit.forms import TagWidget
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'tags': TagWidget(), #Use TagWidget
        }