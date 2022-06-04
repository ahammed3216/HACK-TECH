from django import forms

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class SignUpForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password_one=forms.CharField(widget=forms.PasswordInput())
    password_two=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data=self.cleaned_data
        username=self.cleaned_data.get('username')
        email=self.cleaned_data.get('email')
        password_one=self.cleaned_data.get('password_one')
        password_two=self.cleaned_data.get('password_two')
        print("test")
        if password_one != password_two:
            print("error")
            raise forms.ValidationError("Password must be same")
        
        return cleaned_data


class ComplaintForm(forms.Form):
    title=forms.CharField()
    institution=forms.CharField()
    roll_number=forms.CharField()
    description=forms.CharField(widget=forms.Textarea())
    

    def clean(self):
        print("hello")
        cleaned_data=self.cleaned_data
        print(cleaned_data)
        return cleaned_data
        