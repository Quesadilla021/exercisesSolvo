# forms.py
from django import forms
from ATM.models import Account
from djgentelella.widgets import core as gentelella_widgets


class AccountValidationForm(forms.Form):
    account_name = forms.CharField(widget=gentelella_widgets.TextInput, max_length=200, label='Account Name')
    pin_code = forms.IntegerField(widget=gentelella_widgets.NumberInput, label='PIN')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(AccountValidationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        account_name = cleaned_data.get("account_name")
        pin_code = cleaned_data.get("pin_code")

        try:
            account = Account.objects.get(user=self.user, name=account_name, pin_code=pin_code)
        except Account.DoesNotExist:
            raise forms.ValidationError("Nombre de cuenta o PIN incorrecto.")

        return cleaned_data


class WithdrawalForm(forms.Form):
    amount = forms.IntegerField(widget=gentelella_widgets.NumberInput, label='Enter the amount to withdraw', min_value=2000, step_size=2000)

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'pin_code', 'money', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'pin_code': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your PIN code'}),
            'money': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the amount'}),
            'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select your account'}),
        }