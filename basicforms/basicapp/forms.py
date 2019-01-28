from django import forms
from django.core import validators # USING DJANGO BUILT IN VALIDATORS

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # WE CAN ALO VERIFY EMAIL
    verify_email = forms.EmailField(label='Confirm Email')
    text = forms.CharField(widget=forms.Textarea)
    # WE CAN ALSO ADD A BOTCATCHER FOR FORM validation
    #botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,
    #                            validators=[validators.MaxValueValidator(0)])

    # CREATE A CUSTOM VALIDATOR FOR YOUR FORM
    #def clean_botcatcher(self):
    #    botcatcher = self.cleaned_data['botcatcher']
    #    if len(botcatcher) > 0:
    #        raise forms.ValidationError("BUSTED BOT!")
    #    return botcatcher

    #  CLEAN DATA FROM FORM
    def clean(self):
        all_clean_data = super().clean() # Error super() takes atleat one arguement
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails Do not match")
