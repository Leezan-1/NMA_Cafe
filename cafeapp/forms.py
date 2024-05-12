from django import forms
from django.core.validators import RegexValidator
from .models import Customer

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern = r'^9(8|7)\d{8}$'

usernameValidator = RegexValidator(
    regex=f"({email_pattern})|({mobile_pattern})",
    message="Enter a valid email or mobile number.",
)

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=25, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Email or mobile number'}),
        validators=[usernameValidator],
        error_messages={
            'required': 'Username is required!',
            'max_length': 'Max length is 25!',
        }
    )

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
