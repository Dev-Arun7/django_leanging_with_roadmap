
from django import forms
from .models import Student
from django.contrib.auth import get_user_model
from .models import StaffProfile



class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["name", "age", "email", "image", "document"]

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
    

    # Validate upload document
    def clean_document(self):
        document = self.cleaned_data.get("document")

        # No document uploaded? That's okay.
        if not document:
            return document

        # Allow only pdf
        if not document.name.lower().endswith(".pdf"):
            raise forms.ValidationError("Only PDF files are allowed.")

        # Allow max file size = 5MB
        if document.size > 5 * 1024 * 1024:
            raise forms.ValidationError("File  size cannot exceed 5 MB.")

        return document


User = get_user_model()


# Edit basic Django User details
class UserAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


# Edit additional StaffProfile details
class StaffProfileForm(forms.ModelForm):

    class Meta:
        model = StaffProfile
        fields = [
            "phone",
            "address",
            "date_of_birth",
            "gender",
            "image",
        ]

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={"type": "date"}
            ),
        }
