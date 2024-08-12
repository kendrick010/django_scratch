from django import forms
from .models import Product

class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(label="Enter title", widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))
    email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name",
        "id": "my-id-name",
        "rows": 10,
        "cols": 120
    }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else: raise forms.ValidationError("Not valid title")


class RawProductForm(forms.Form):
    title = forms.CharField(label="Enter title", widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name",
        "id": "my-id-name",
        "rows": 10,
        "cols": 120
    }))
    price = forms.DecimalField(initial=199.99)