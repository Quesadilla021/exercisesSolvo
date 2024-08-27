from django import forms
from djgentelella.forms.forms import GTForm
from djgentelella.widgets import core as genwidgets

from Holidays.models import Holiday


class HolidayForm(GTForm, forms.ModelForm):

    class Meta:
        model = Holiday
        fields = '__all__'
        widgets = {
            "name": genwidgets.Select()
        }