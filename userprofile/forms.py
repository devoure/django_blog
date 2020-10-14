from django import forms
from userprofile.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        #meta class defines the n=behaviour of a class
        model = UserProfile
        fields = ('likes_cheese', 'favourite_hamster_name')


