from django import forms
from .models import Profile

from PIL import Image

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'profile_banner', 'bio']

    def save(self):
        profile = super(ProfileForm, self).save()

        # TODO: Remove old images from storage if they exist.

        # Resize the profile picture.
        if self.files.get('profile_pic'):
            profile_image = Image.open(profile.profile_pic)
            width_offset = profile_image.height / 2
            cropped_profile_image = profile_image.crop((profile_image.width / 2 - width_offset, 0, 
                                    profile_image.width / 2 + width_offset, profile_image.height))
            resized_profile_image = cropped_profile_image.resize((400, 400), Image.ANTIALIAS)
            resized_profile_image.save(profile.profile_pic.path)

        # Resize the profile banner.
        if self.files.get('profile_banner'):
            banner_image = Image.open(profile.profile_banner)
            height_offset = banner_image.height - ((360 / 1080) * banner_image.width)
            cropped_banner_image = banner_image.crop((0, banner_image.height / 2 - height_offset, 
                                   banner_image.width, banner_image.height / 2 + height_offset))
            resized_banner_image = cropped_banner_image.resize((1080, 360), Image.ANTIALIAS)
            resized_banner_image.save(profile.profile_banner.path)

        return profile