from django import forms

class Form(forms.Form):
    username = forms.CharField(max_length=100, label="Username:", error_messages={
        "required": "Your username must not be empty!",
        })
    password = forms.CharField(max_length=100, label="Password:", error_messages={
        "required": "Your password must not be empty!"
    })
    cityOfEmployment = forms.CharField(max_length=100, label="City of employment:", required=False)

    options = [('Apache', 'Apache'), ('Nginx', 'Nginx'), ('IIS', 'IIS')]
    select = forms.ChoiceField(choices=options, label="Web Server:")

    optionsRadio = [('Admin', 'Admin'), ('Engineer', 'Engineer'), ('Manager', 'Manager'), ('Guest', 'Guest')]
    radio = forms.ChoiceField(choices=optionsRadio, widget=forms.RadioSelect, label="Please specify your role:")

    optionsCheck = [('Mail', 'Mail'), ('Payroll', 'Payroll'), ('Self-service', 'Self-service')]
    check = forms.MultipleChoiceField(choices=optionsCheck, widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-class'}), label="Single Sign-on to the following:")