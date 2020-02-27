from django import forms
from .models import Class

class TeacherSearchForm(forms.Form):
    """Form to search teacher"""

    teacher = forms.CharField(label='Teacher', max_length=30)
    teacher.widget.attrs.update({'class': 'form-control'})
    teacher.widget.attrs.update({'required': True})
    teacher.widget.attrs.update({'placeholder': 'Type teacher\'s Name'})
    '''
    teacher = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search Teacher Name:"})
        )
    
    def save(self, query):
        teacher = Class.objects.filter_teachers(query)
        return teacher
    '''

    def make_search(self, teacher_name):
        teacher_list = Class.manager.filter_by_teachers(teacher_name)
        print(teacher_list)
        return teacher_list
