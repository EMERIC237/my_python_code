from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'your title'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={

        "placeholder": 'your description',
        "rows":20,
        "cols": 40,
        "class": "my_new_class"
        }
        ))
    price = forms.DecimalField(initial=155.5)

    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "SB" not in title:
            raise forms.ValidationError("this is not a valid title")
        else:
            return title
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("gmail.com"):
            raise forms.ValidationError("This is not a valid email")

class RawproductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'your title'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={

        "placeholder": 'your description',
        "rows":20,
        "cols": 40,
        "class": "my_new_class"
        }
        ))
    price = forms.DecimalField(initial=155.5)
