from django import forms 
from .models import File

class FileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = File
        fields = ['main_content']