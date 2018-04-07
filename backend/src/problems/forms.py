from django import forms

from pagedown.widgets import PagedownWidget

from .models import Problem, TestCase
from tags.models import Tag

class ProblemForm(forms.ModelForm):
	statement = forms.CharField(widget=PagedownWidget(show_preview=False))
	datetime = forms.DateField(widget=forms.DateTimeInput())
	class Meta:
		model = Problem
		fields = [
			"title", 
			"problem_code",
			"statement",
			"tags",
			"datetime",
		]

	def __init__(self, *args, **kwargs):
		super(ProblemForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

		self.fields['datetime'].widget.attrs.update({'class': 'form-group form-control datetimepicker', 'value':'10/05/2016'})

class TestCaseForm(forms.ModelForm):
	class Meta:
		model = TestCase
		fields = [
			"input", 
			"output",
			"sample",
			"weight",
			"explanation",
		]

	def __init__(self, *args, **kwargs):
		super(TestCaseForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
