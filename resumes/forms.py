from django import forms

from resumes.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ["owner"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "profession": forms.Select(attrs={"class": "form-control"}),
        }
    # def clean(self):
    #
    # def save(self, commit=True, user=None):
    #     instance = super(ResumeForm, self).save(commit=True)
    #     return instance
