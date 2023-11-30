from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Charlene", "class": "form-control"}),
        label=""
    )
    last_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Pham", "class": "form-control"}),
        label=""
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.widgets.EmailInput(attrs={"placeholder": "charlene@instawork.com", "class": "form-control"}),
        label=""
    )
    phone = forms.CharField(
        required=False, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "415-310-1619", "class": "form-control"}),
        label=""
    )
    role = forms.ChoiceField(
        choices=[('Regular', 'Regular - Can\'t delete members'), ('Admin', 'Admin - Can delete members') ],
        required=True, 
        widget=forms.widgets.RadioSelect(attrs={"class": "form-check-input"}),
        label=""
    )

    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)
        self.fields['role'].initial = 'Regular'  #Set 'Regular' as the default checked option

    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'email', 'phone', 'role']

    