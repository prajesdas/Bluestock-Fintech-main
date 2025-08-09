from django import forms
from .models import IpoInfo
from .widgets import CustomClearableFileInput

class IPOForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company_logo'].widget = CustomClearableFileInput(ipo_instance=self.instance)

    def clean_company_logo(self):
        logo = self.cleaned_data.get('company_logo')
        if 'company_logo-clear' in self.data:
            if self.instance.pk:
             
                if self.instance.company_logo:
                    self.instance.company_logo.delete(save=False)
                logo = None
        return logo

    class Meta:
        model = IpoInfo
        fields = '__all__'
        widgets = {
            'status': forms.Select(choices=IpoInfo.STATUS_CHOICES),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email Address', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
