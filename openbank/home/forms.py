from django import forms

from home.models import AccountMore


class MoreAccountNew(forms.ModelForm):
    class Meta:
        model = AccountMore
        fields = '__all__'