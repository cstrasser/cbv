from django import forms

class BookForm(forms.Form):
    title       = forms.CharField(max_length = 50)
    name        = forms.CharField(max_length = 25)
    email       = forms.EmailField(max_length = 25)
    status      = forms.BooleanField()
    notes       = forms.CharField(widget = forms.Textarea)


