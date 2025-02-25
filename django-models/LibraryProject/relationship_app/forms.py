from django import forms
from .models import AdminUserProfile, LibrarianUserProfile, MemberUserProfile

class AdminUserProfileForm(forms.ModelForm):
    class Meta:
        model = AdminUserProfile
        fields = ['phone_number', 'address']

class LibrarianUserProfileForm(forms.ModelForm):
    class Meta:
        model = LibrarianUserProfile
        fields = ['phone_number', 'address', 'hire_date']

class MemberUserProfileForm(forms.ModelForm):
    class Meta:
        model = MemberUserProfile
        fields = ['phone_number', 'address', 'membership_id', 'date_of_birth']