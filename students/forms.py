
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["name", "age", "email"]

    # Custom validation for the age field
    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 5:
            raise forms.ValidationError("Age must be at least 5.")

        if age > 100:
            raise forms.ValidationError("Age cannot be above 100.")

        return age


    # Custom validation for email
    def clean_email(self):
        email = self.cleaned_data["email"]

        valid_emails = ["@example.com", "@gmail.com", "@test.com"]

        for sample in valid_emails:
            if email.endswith(sample):
                break
        else:
            raise forms.ValidationError("Email not recognized.")

        return email