"""from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= "__all__"
class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ('user_name', 'upwd',)"""

from django import forms
from .models import Post , User

#choices = [('coding','coding') ,('data structure', 'data structure') ,('cloud computing','cloud computing')]
# choices= Category.objects.all().values_list('name','name')
# choice_list =[]

# for item in choices:
#     choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'content', 'snippet')
        widgets = {
             #'blog_id': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Write title for your blog here !!!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
             #'author': forms.Select(attrs={'class': 'form-control'}),
             #'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Write content for your blog here !!!'}),
            'snippet':forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class EditForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'content','snippet')
        widgets = {
            # 'blog_id': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'content':forms.TextInput(attrs={'class': 'form-control'}),
            'snippet':forms.TextInput(attrs={'class': 'form-control'}),
        }

# class PostForm(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields = "__all__"

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields= "__all__"
# class AuthenticationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields= ('user_name', 'upwd',)

        

