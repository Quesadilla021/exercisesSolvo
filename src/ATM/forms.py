# forms.py
from django import forms
from ATM.models import account

class WithdrawalForm(forms.Form):
    amount = forms.IntegerField(label='Enter the amount to withdraw', min_value=2000, step_size=2000)

class AccountForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ['name', 'pin_code', 'money']