from django import forms

from jobs.models import Jobs


class IndexForm(forms.Form):
    keywords = forms.CharField(label="Enter keywords", max_length=50)
    location = forms.CharField(label="Enter location", max_length=200)
    experience = forms.CharField(max_length=50)


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = "__all__"

    # def clean(self):
    #     super(JobsForm, self).clean()
    #
    #     # job_name = self.cleaned_data.get('job_name')
    #
    #     max_exp = self.cleaned_data.get('max_exp')
    #     min_exp = self.cleaned_data.get('min_exp')
    #
    #
    #     if len(job_name) < 6:
    #         self._errors['job_name'] = self.error_class([
    #             'error'])
    #     # return any errors if found
    #     return self.cleaned_data
