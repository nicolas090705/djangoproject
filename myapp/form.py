from django import forms

class createNewTask(forms.Form):
    title = forms.CharField(label='titulo de tarea', max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea)

class createNewProject(forms.Form):
    name = forms.CharField(label='name', max_length=200)