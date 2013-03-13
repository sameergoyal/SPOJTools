from django import forms

class CompareUsersForm(forms.Form):
	user1 = forms.CharField(widget=forms.widgets.TextInput())
	user2 = forms.CharField(widget=forms.widgets.TextInput())
	
