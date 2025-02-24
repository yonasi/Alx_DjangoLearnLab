from django import forms
from .models import AdminProfile, LibrarianProfile, MemberProfile

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['phone_number', 'address']

class LibrarianProfileForm(forms.ModelForm):
    class Meta:
        model = LibrarianProfile
        fields = ['phone_number', 'address', 'hire_date']

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['phone_number', 'address', 'membership_id', 'date_of_birth']