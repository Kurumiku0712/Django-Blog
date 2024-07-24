from django import forms


class PostBlogForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=1, error_messages={
        'required': 'Please enter the title!',
        'max_length': 'Title length: 1 to 50 characters.',
        'min_length': 'Title length: 1 to 50 characters.'
    })
    content = forms.CharField(min_length=1, error_messages={
        'required': 'Please enter the content!'
    })
    category = forms.IntegerField()
