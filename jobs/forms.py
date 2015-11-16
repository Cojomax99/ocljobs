from django import forms


class QueryForm(forms.Form):
    description = forms.CharField(
        label='Job Description',
        widget=forms.TextInput(attrs={
            "placeholder": "Filter by title, benefits, companies, expertise"
        }))
    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(attrs={
            "placeholder": "Filter by city, state, zip code or country"
        })
    )
    full_time = forms.BooleanField(label='Full Time Only')
