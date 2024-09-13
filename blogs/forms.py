from django import forms
from .models import blogPost, Category

choices = Category.objects.all().values_list('category_name','category_name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = blogPost
        fields = ('title', 'title_tag', 'author','category', 'body', 'image')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'userjs', 'type':'hidden'}),
            'category' : forms.Select(choices=choice_list , attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }

  
class EditForm(forms.ModelForm):
    class Meta:
        model = blogPost
        fields = ('title', 'title_tag','category','body', 'image')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            # 'image' : forms.ImageField(attrs={'class':'form-control'}),
        }
