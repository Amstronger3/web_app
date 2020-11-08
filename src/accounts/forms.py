from django.forms import ModelForm

from accounts.models import Profile


class ProfileBaseForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', 'nickname')
        # fields = '__all__'
        
        
class PublicationBaseForm(ModelForm):
    class Meta:
        model = Publication
        fields = ('date', 'author', 'body', 'description', 'comment')
        # fields = '__all__'


class ProfileAddForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass
